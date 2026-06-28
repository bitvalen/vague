.ONESHELL:
SHELL = /bin/bash

THEME_NAME   := vague-theme
PUBLISHER_ID := bitvalen.vague-theme

# ── OS check ──────────────────────────────────────────────────────────────────
OS := $(shell uname -s)
ifneq ($(OS), Linux)
$(error Unsupported OS: $(OS). Only Linux is supported)
endif

# ── Detect VS Code extensions directory ───────────────────────────────────────
EXTENSIONS_DIR := $(shell \
    if [ -d "$(HOME)/.vscode/extensions" ]; then \
        echo "$(HOME)/.vscode/extensions"; \
    elif [ -d "$(HOME)/snap/code/current/.vscode/extensions" ]; then \
        echo "$(HOME)/snap/code/current/.vscode/extensions"; \
    elif [ -d "$(HOME)/.var/app/com.visualstudio.code/data/vscode/extensions" ]; then \
        echo "$(HOME)/.var/app/com.visualstudio.code/data/vscode/extensions"; \
    elif [ -d "$(HOME)/.vscode-oss/extensions" ]; then \
        echo "$(HOME)/.vscode-oss/extensions"; \
    fi)

INSTALL_PATH    := $(EXTENSIONS_DIR)/$(THEME_NAME)
EXTENSIONS_JSON := $(EXTENSIONS_DIR)/extensions.json

.PHONY: install uninstall

install:
	@set -e
	
	if ! command -v python3 &> /dev/null; then
		echo "  [ERROR] python3 could not be found. Please install Python 3 to continue."
		exit 1
	fi

	echo "[1/4] Checking environment..."
	if [ -z "$(EXTENSIONS_DIR)" ]; then
		echo "  [ERROR] VS Code extensions directory not found. Is VS Code installed?"
		exit 1
	fi
	echo "  [OK] OS            : $(OS)"
	echo "  [OK] Extensions dir: $(EXTENSIONS_DIR)"
	echo "  [OK] Install path  : $(INSTALL_PATH)"
	echo "  [OK] Registry file : $(EXTENSIONS_JSON)"

	echo "[2/4] Copying theme files..."
	if [ -d "$(INSTALL_PATH)" ]; then
		echo "  [INFO] Existing installation found, removing..."
		rm -rf "$(INSTALL_PATH)"
		echo "  [OK] Removed old installation"
	fi
	cp -r "$(CURDIR)" "$(INSTALL_PATH)"
	echo "  [OK] Copied $(CURDIR) -> $(INSTALL_PATH)"
	echo "  [OK] Files installed:"
	find "$(INSTALL_PATH)" -not -path '*/.*' | sed 's|$(INSTALL_PATH)||' | sed 's|^|         |'

	echo "[3/4] Registering in extensions.json..."
	python3 register_theme.py "$(EXTENSIONS_JSON)" "$(INSTALL_PATH)" "$(PUBLISHER_ID)" "$(THEME_NAME)" "install"

	echo "[4/4] Verifying installation..."
	if [ -f "$(INSTALL_PATH)/package.json" ]; then
		echo "  [OK] package.json found"
	else
		echo "  [ERROR] package.json missing — something went wrong"
		exit 1
	fi
	if [ -f "$(INSTALL_PATH)/themes/theme.json" ]; then
		echo "  [OK] themes/theme.json found"
	else
		echo "  [ERROR] themes/theme.json missing — something went wrong"
		exit 1
	fi
	echo ""
	echo "  All done! Restart VS Code and select 'Vague Theme' from Color Themes."

uninstall:
	@set -e
	echo "[1/2] Removing theme files..."
	if [ -z "$(EXTENSIONS_DIR)" ]; then
		echo "  [ERROR] VS Code extensions directory not found."
		exit 1
	fi
	if [ -d "$(INSTALL_PATH)" ]; then
		rm -rf "$(INSTALL_PATH)"
		echo "  [OK] Removed $(INSTALL_PATH)"
	else
		echo "  [INFO] Nothing to remove at $(INSTALL_PATH)"
	fi

	echo "[2/2] Unregistering from extensions.json..."
	python3 register_theme.py "$(EXTENSIONS_JSON)" "$(INSTALL_PATH)" "$(PUBLISHER_ID)" "$(THEME_NAME)" "uninstall"
	echo ""
	echo "  All done! Restart VS Code."