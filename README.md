# PrintPrintBaby 🖨️

![PrintPrintBaby Logo](assets/logo.png)

A very simple Python package created for teaching purposes. This project allows printing text in the terminal.

## Installation

This project is **not installed with pip**.

To use it, you must configure two environment variables:

### 1. PYTHONPATH (for the library)

In order to use the `printprintbaby` library in your **own Python scripts**, you need to add the `src/` directory of this project to your `PYTHONPATH`.

Replace `your_project_location` with the actual path to the project on your machine.

**Linux / macOS**
```bash
export PYTHONPATH=your_project_location/src
```

**Windows (PowerShell)**
```powershell
$env:PYTHONPATH="your_project_location\src"
```

This allows Python to find the `printprintbaby` package when using `import`.

---

### 2. PATH (for the scripts)

To execute the command-line script easily, you need to add the `scripts/` directory of this project to your `PATH`.

Replace `your_project_location` with the actual path to the project on your machine.

**Linux / macOS**
```bash
export PATH=your_project_location/scripts:$PATH
```

**Windows (PowerShell)**
```powershell
$env:PATH="your_project_location\scripts;$env:PATH"
```

This allows you to run the script directly from the command line.

---

## Usage

### Library usage

```python
from printprintbaby import print_baby

print_baby("PrintPrintBaby!")
```

### Script usage

```bash
printprintbaby_cli.py "PrintPrintBaby!"
```
