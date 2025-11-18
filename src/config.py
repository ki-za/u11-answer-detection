from pathlib import Path

# get directory path containing this file
PACKAGE_DIR = Path(__file__).resolve()
SRC_DIR = PACKAGE_DIR.parent
PROJECT_ROOT = SRC_DIR.parent
# `__path__` = current file path
# `.parent` = go up one dir
# `.resolve()` = convert relative path to absolute


INPUT_PDF_DIR = PROJECT_ROOT / "data" / "input"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"
TEMP_DIR = PROJECT_ROOT / "data" / "temp"
CONFIG_DIR = PROJECT_ROOT / "config"

# ensure dirs exist when config imported
#
INPUT_PDF_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)
