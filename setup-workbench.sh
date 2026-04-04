#!/bin/bash

# Gemini Workbench: Setup Script
# Automates the installation of the workbench on a new machine.

set -e

echo "Starting Gemini Workbench setup..."

# 1. Prerequisite Check
echo "Checking prerequisites..."
IS_SANDBOX=false
if [ "$GEMINI_SANDBOX" = "1" ] || [ "$GEMINI_CLI" = "1" ] || [ -f /.dockerenv ] || [ -f /run/.containerenv ]; then
    IS_SANDBOX=true
    echo "Running inside a sandbox environment. Skipping Podman-specific checks."
fi

for cmd in node npm git gemini; do
    if ! command -v $cmd &> /dev/null; then
        echo "Error: $cmd is not installed."
        case $cmd in
            node|npm) echo "Please install Node.js/npm (e.g., 'brew install node')." ;;
            git) echo "Please install Git (e.g., 'brew install git')." ;;
            gemini) echo "Please install the Gemini CLI via npm." ;;
        esac
        exit 1
    fi
done

if [ "$IS_SANDBOX" = false ]; then
    if ! command -v podman &> /dev/null; then
        echo "Error: Podman is not installed. Please install Podman Desktop or podman CLI."
        exit 1
    fi
fi
echo "Prerequisites met."

# 2. Workspace Root Detection
WORKBENCH_ROOT=$(cd "$(dirname "$0")" && pwd)
PROJECTS_ROOT=$(dirname "$WORKBENCH_ROOT")

# 3. Symlink Skills and Session Log
SKILLS_DIR="$HOME/.gemini/skills"
echo "Setting up skills and session log in $HOME/.gemini..."
mkdir -p "$SKILLS_DIR"

# Standardize Session Log Storage
WORKBENCH_SESSION_LOG="$WORKBENCH_ROOT/session_log"
mkdir -p "$WORKBENCH_SESSION_LOG"
ln -sfn "$WORKBENCH_SESSION_LOG" "$HOME/.gemini/session_log"
echo "Linked $HOME/.gemini/session_log -> $WORKBENCH_SESSION_LOG"

# Link skills from the workbench itself
echo "Checking workbench skills..."
for skill in "$WORKBENCH_ROOT/skills"/*; do
    if [ -d "$skill" ]; then
        SKILL_NAME=$(basename "$skill")
        echo "Linking workbench skill: $SKILL_NAME"
        ln -sfn "$skill" "$SKILLS_DIR/$SKILL_NAME"
    fi
done

# Standardize Commands Storage
COMMANDS_DIR="$HOME/.gemini/commands"
echo "Setting up custom commands in $HOME/.gemini/commands..."
mkdir -p "$COMMANDS_DIR"

# Link commands from the workbench itself
echo "Checking workbench commands..."
if [ -d "$WORKBENCH_ROOT/commands" ]; then
    for cmd in "$WORKBENCH_ROOT/commands"/*; do
        if [ -e "$cmd" ]; then
            CMD_NAME=$(basename "$cmd")
            echo "Linking workbench command: $CMD_NAME"
            ln -sfn "$cmd" "$COMMANDS_DIR/$CMD_NAME"
        fi
    done
fi

# Standardize Policy Storage
POLICIES_DIR="$HOME/.gemini/policies"
echo "Setting up safety policies in $HOME/.gemini/policies..."
mkdir -p "$POLICIES_DIR"

# Link policies from the workbench itself
echo "Checking workbench policies..."
if [ -d "$WORKBENCH_ROOT/policies" ]; then
    for policy in "$WORKBENCH_ROOT/policies"/*; do
        if [ -f "$policy" ]; then
            POLICY_NAME=$(basename "$policy")
            echo "Linking workbench policy: $POLICY_NAME"
            ln -sfn "$policy" "$POLICIES_DIR/$POLICY_NAME"
        fi
    done
fi

# Scan sibling projects for skills/ directories and link them
echo "Scanning sibling projects for additional skills..."
for project in "$PROJECTS_ROOT"/*; do
    if [ -d "$project/skills" ]; then
        echo "Found skills in: $(basename "$project")"
        for skill in "$project/skills"/*; do
            if [ -d "$skill" ]; then
                SKILL_NAME=$(basename "$skill")
                echo "Linking project skill: $SKILL_NAME"
                ln -sfn "$skill" "$SKILLS_DIR/$SKILL_NAME"
            fi
        done
    fi
done

# 4. Register Projects
echo "Registering projects with Gemini CLI..."
for project in "$WORKBENCH_ROOT" "$PROJECTS_ROOT"; do
    if ! gemini project list | grep -q "$project"; then
        echo "Adding $project to Gemini CLI..."
        gemini project add "$project"
    else
        echo "Project $project already registered."
    fi
done

# Ensure Git trusts these directories (prevents "dubious ownership" errors)
for dir in "$WORKBENCH_ROOT" "$PROJECTS_ROOT"; do
    if ! git config --global --get-all safe.directory | grep -q "$dir"; then
        echo "Configuring Git safe.directory for $dir..."
        git config --global --add safe.directory "$dir"
    fi
done

# 5. Conductor Default Check
echo "Ensuring Conductor is initialized for registered projects..."
for project in "$WORKBENCH_ROOT" "$PROJECTS_ROOT"; do
    if [ -d "$project" ]; then
        if [ ! -d "$project/conductor" ]; then
            echo "Conductor not found in $(basename "$project")."
            # Launch the interactive setup script
            bash "$WORKBENCH_ROOT/bin/conductor-init" "$project" || true
        else
            echo "Conductor already initialized in $(basename "$project")."
        fi
    fi
done

if [ "$IS_SANDBOX" = false ]; then
    # Remove existing container to ensure new environment variables are applied
    CONTAINER="gemini-sandbox-container"
    if podman ps -a --format "{{.Names}}" | grep -q "^$CONTAINER$"; then
        echo "Removing existing container $CONTAINER..."
        podman rm -f "$CONTAINER"
    fi

    # 6. Build Sandbox Image
    BUILD_SANDBOX=true
    if [[ "$1" == "--no-build" ]]; then
        BUILD_SANDBOX=false
    fi

    if [ "$IS_SANDBOX" = false ] && [ "$BUILD_SANDBOX" = true ]; then
        echo "Building Podman sandbox image..."
        bash "$WORKBENCH_ROOT/bin/build-sandbox"
    elif [ "$BUILD_SANDBOX" = false ]; then
        echo "Skipping sandbox image build as requested."
    fi
# 7. Configure PATH Instructions
echo ""
echo "--- Setup Complete ---"
echo "To finish the setup, add the workbench 'bin' directory to your PATH."
echo ""
echo "Add this to your ~/.zshrc or ~/.bashrc:"
echo "export PATH=\"\$PATH:$WORKBENCH_ROOT/bin\""
echo ""
echo "Then, restart your terminal or run: source ~/.zshrc (or ~/.bashrc)"
echo ""
echo "Finally, make sure to authenticate by running: gemini login"
echo "----------------------"
