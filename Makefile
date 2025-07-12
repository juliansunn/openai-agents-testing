PYTHON_VERSION=3.12.1
VENV_DIR=.venv

.PHONY: all setup env pyenv venv install run

all: setup

setup: env pyenv venv install
	@echo "Setup complete. Activate your venv with: source $(VENV_DIR)/bin/activate"

# Create .env from .env.example if not exists
env:
	@if [ ! -f .env ]; then \
		cp env.example .env || cp .env.example .env; \
		echo ".env created from example."; \
	else \
		echo ".env already exists."; \
	fi

# Ensure pyenv has the correct Python version
pyenv:
	@if command -v pyenv >/dev/null 2>&1; then \
		if ! pyenv versions --bare | grep -q '^$(PYTHON_VERSION)$$'; then \
			echo "Installing Python $(PYTHON_VERSION) with pyenv..."; \
			pyenv install $(PYTHON_VERSION); \
		fi; \
		pyenv local $(PYTHON_VERSION); \
		echo "Using Python version: $$(pyenv version)"; \
	else \
		echo "pyenv not found, skipping pyenv setup."; \
	fi

# Create venv if not exists
venv:
	@if [ ! -d $(VENV_DIR) ]; then \
		python$(PYTHON_VERSION) -m venv $(VENV_DIR) || python -m venv $(VENV_DIR); \
		echo "Virtual environment created at $(VENV_DIR)"; \
	else \
		echo "Virtual environment already exists at $(VENV_DIR)"; \
	fi

# Install requirements in venv
install:
	@. $(VENV_DIR)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Start the Chainlit app
run:
	@. $(VENV_DIR)/bin/activate && chainlit run chainlit_app.py 