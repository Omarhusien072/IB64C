# IB64C (Image Base64 Converter)

A modern, multithreaded desktop utility built with Python and PySide6 (Qt6) that converts images into base64 encoded strings and compiles them into importable Python resource modules. 

This tool is designed to simplify resource management in desktop applications (like PySide6/PyQt apps) by allowing developers to embed images directly into Python files, eliminating the need to distribute separate image files alongside the executable.

---

## 🚀 Key Features

- **Recursive Directory Scan:** Automatically traverses the selected input directory and all of its subfolders to find images.
- **Flexible Format Filters:** Supports conversion for specific file formats (`PNG`, `JPG`, `JPEG`, `GIF`, `BMP`, `WebP`, `SVG`) or `ALL` image types at once.
- **Multithreaded Processing:** Runs scans and conversion processes in a background worker thread (`QThread`) to ensure the GUI remains fully responsive.
- **Smart Name Sanitization:** Automatically sanitizes image filenames to create valid Python variable names (handles spaces, special characters, and leading digits).
- **Chunked Base64 Output:** Chunks base64 string outputs into clean 80-character lines to prevent text editors and IDEs from lagging when opening resource files.
- **Modern UI Styling:** A clean, custom-styled dark-mode interface matching slate/blue aesthetics with real-time directory validation (green/red borders).
- **Automatic Collision Handling:** Intelligently checks for existing output files and names new files sequentially (e.g., `Images.py`, `Images_1.py`) to avoid overwriting your work.

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **GUI Framework:** PySide6 (Qt6)
- **Concurrency:** Qt Concurrency (`QThread`, `QObject` signals)
- **Formatting & Conversion:** Native `base64` and filesystem libraries

---

## 📦 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Omarhusien072/IB64C.git
   cd IB64C
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   Make sure you have PySide6 installed:
   ```bash
   pip install PySide6
   ```

4. **Run the Application:**
   ```bash
   python main.py
   ```

---

## 📖 How to Use

1. **Set Input Directory:** Click the browse folder icon in the **Input Directory** field to choose the folder containing the images you wish to convert.
2. **Choose File Type:** Select the image format from the dropdown menu (e.g., `PNG`, `SVG`, `WebP`, or `ALL`).
3. **Set Output Directory:** Choose the folder where the generated Python resource module should be saved.
4. **Convert:** Click **Convert to Base64**. A spinner will show while processing, and a success panel will appear once the `.py` file is generated.

---

## 💻 How to Use the Generated File in Python

Once the file is generated (usually named `Images.py`), you can import and decode the images directly in your Python code:

```python
import base64
from PySide6.QtGui import QPixmap, QIcon
# Import the auto-generated variable (e.g., logo_png or icon_svg)
from Images import logo_png

# 1. Loading into a QPixmap for QLabel, QButton, etc.
pixmap = QPixmap()
pixmap.loadFromData(base64.b64decode(logo_png))

# 2. Assigning it to a QLabel
label = QLabel()
label.setPixmap(pixmap)
```

---

## 📂 Project Structure

```
IB64C/
├── Assets/                  # Icon assets and loading animations
├── IB64C_Core/              # Core conversion engines
│   └── IB64C_Core_Logic.py  # Traversal, base64 encoding, & file generation
├── IB64C_UI/                # GUI Components
│   ├── Logic/
│   │   └── IB64C_Logic.py   # Event logic, worker thread management, signals
│   ├── Theme/
│   │   └── Theme.py         # QSS (Qt Stylesheet) Dark Theme setup
│   └── UI/
│       └── IB64C_UI.py      # QMainWindow layout setup and widget styling
├── main.py                  # App entry point
├── LICENSE                  # License file
└── README.md                # Project documentation
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.