#!/bin/bash

# Gemini Workbench: Setup Script
# Automates the installation of the workbench on a new machine.

set -e

echo "Starting Gemini Workbench setup..."

# 1. Prerequisite Check
echo "Checking prerequisites..."
for cmd in node npm podman git gemini; do
    if ! command -v $cmd &> /dev/null; then
        echo "Error: $cmd is not installed. Please install it before running this script."
        exit 1
    fi
done
echo "Prerequisites met."

# 2. Workspace Root Detection
WORKBENCH_ROOT=$(cd "$(dirname "$0")" && pwd)
PROJECTS_ROOT=$(dirname "$WORKBENCH_ROOT")

# 3. Symlink Skills
SKILLS_DIR="$HOME/.gemini/skills"
echo "Setting up skills in $SKILLS_DIR..."
mkdir -p "$SKILLS_DIR"

for skill in "$WORKBENCH_ROOT/skills"/*; do
    if [ -d "$skill" ]; then
        SKILL_NAME=$(basename "$skill")
        echo "Linking skill: $SKILL_NAME"
        ln -sfn "$skill" "$SKILLS_DIR/$SKILL_NAME"
    fi
done

# 4. Register Projects
echo "Registering projects with Gemini CLI..."
gemini project add "$WORKBENCH_ROOT"
gemini project add "$PROJECTS_ROOT"

# 5. Build Sandbox Image
echo "Building Podman sandbox image..."
bash "$WORKBENCH_ROOT/bin/build-sandbox"

# 6. Configure PATH Instructions
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
