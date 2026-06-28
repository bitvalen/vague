# Vague Theme Ports

This repository contains multi-IDE ports of the popular Neovim colorscheme, vague.nvim.

The goal of this project is to bring the same clean, muted, and distraction-free dark aesthetics of vague.nvim to other mainstream development environments.

Currently supported ide:
- Visual Studio Code

Future plans:
- Zed
- Webstorm

## Requirements
Before running the installation setup, ensure your system meets the following prerequisites:
1. Operating System: Linux (Ubuntu, Fedora, Arch, Flatpak/Snap installations supported).
2. Python: Python 3.x installed and available in your system path.
3. Build Tools: make utility installed.
4. Text Editor: VS Code, VSCodium, or VS Code OSS installed.

## Setup Steps for VS Code

The repository uses a smart automated setup process that detects your VS Code ecosystem (whether installed traditionally, via Snap, or via Flatpak) and installs the theme seamlessly.

### 1. Clone the Repository
Open your terminal and clone the project to your local machine:
```bash
git clone https://github.com/bitvalen/vague.git
cd vague
```

### 2. Install the Theme
Run the automated Makefile target. This will check your workspace configuration, copy the required assets, and register the extension internally:
```bash
make install
```

### 3. Activate the Theme

1. Open (or restart) VS Code.
2. Open the Command Palette via Ctrl + Shift + P (or Cmd + Shift + P on macOS).
3. Type Preferences: Color Theme and hit Enter.
4. Select Vague Theme from the dropdown list.

## Uninstalling

If you ever need to remove the theme and clean up your extensions.json configuration registry file, run the uninstall rule:
```bash
make uninstall
```

## Repository Architecture
A quick look at how the installer pieces fit together:

- Makefile: The main execution entrypoint handles OS verification, directories, and target orchestration.

- register_theme.py: A Python utility helper that carefully modifies VS Code’s extension registry without breaking your settings.

- themes/: Holds the actual JSON color tokens for the editor interface.