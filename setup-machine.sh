#!/bin/bash

# Gemini Environment: Machine Setup Script
# Automates the installation of essential tools and configurations
# for a new developer machine (macOS/Darwin focused).

set -e

echo "--- Starting Machine Setup ---"

# 1. Homebrew Check
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# 2. Install Core Tools (CLI)
echo "Installing core tools via Homebrew..."
brew install node glow nano

# Attempt to install Podman, but do not fail if it's restricted
echo "Attempting to install optional sandbox dependency: Podman..."
brew install podman || echo "Warning: Could not install Podman. Sandbox will not be available."
brew install --cask podman-desktop || echo "Warning: Could not install Podman Desktop."

# 3. Configure Nano (Markdown Support)
echo "Configuring Nano..."
mkdir -p "$HOME/.nano"
# Check if nano highlights already exist via Homebrew
if [ -d "/opt/homebrew/share/nano" ]; then
    echo 'include "/opt/homebrew/share/nano/*.nanorc"' > "$HOME/.nanorc"
fi

# 4. Python Environment & Testing Suite
echo "Installing Python testing dependencies..."
# Ensure pip is up to date
python3 -m pip install --upgrade pip
# Install global/user testing tools
python3 -m pip install pytest pytest-mock vcrpy python-dotenv

# 5. Shell Configuration (Zsh)
echo "Updating ~/.zshrc..."
ZSHRC="$HOME/.zshrc"
touch "$ZSHRC"

# Add Path if not present
PYTHON_BIN_PATH="$HOME/Library/Python/$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')/bin"

if ! grep -q "$PYTHON_BIN_PATH" "$ZSHRC"; then
    echo "Adding Python bin to PATH..."
    echo "export PATH=\"\$PATH:$PYTHON_BIN_PATH\"" >> "$ZSHRC"
fi

# Set Editor/Visual
if ! grep -q "EDITOR=\"/opt/homebrew/bin/nano\"" "$ZSHRC"; then
    echo "Configuring EDITOR/VISUAL to nano..."
    echo 'export VISUAL=nano' >> "$ZSHRC"
    echo 'export EDITOR="/opt/homebrew/bin/nano"' >> "$ZSHRC"
fi

# 6. Workbench Linking
echo "Linking the Gemini Workbench..."
WORKBENCH_DIR="$HOME/projects/gemini-workbench"
if [ -d "$WORKBENCH_DIR" ]; then
    if ! grep -q "$WORKBENCH_DIR/bin" "$ZSHRC"; then
        echo "Adding Workbench bin to PATH..."
        echo "export PATH=\"\$PATH:$WORKBENCH_DIR/bin\"" >> "$ZSHRC"
    fi
    echo "Running Workbench setup script..."
    bash "$WORKBENCH_DIR/setup-workbench.sh"
else
    echo "⚠️ Warning: gemini-workbench not found at $WORKBENCH_DIR. Clone it and run setup-workbench.sh manually."
fi

echo "--- Machine Setup Complete ---"
echo "Please restart your terminal or run: source ~/.zshrc"
