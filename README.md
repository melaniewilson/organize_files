# 🗂️ File Organizer (Python)

A simple and smart Python script that organizes your messy folders into neatly categorized subfolders based on file type — with undo support, logging, and clear feedback.

---

## ✨ Features

- Organize any folder (default: `Downloads`)
- Categorizes files into folders like Images, Documents, Code, etc.
- Automatically skips hidden files (like `.DS_Store`)
- Saves a move log to a `logs/` folder with timestamps
- Undo file moves after running
- Friendly messages and clear UX
- Command-line support
- GUI version coming soon 👀

---

## 🧰 How to Use

### 1. Clone the repo

```bash
git clone https://github.com/melaniewilson/file-organizer.git
cd file-organizer
```

### 2. Run the script

#### 🖥️ Option A: Organize your Downloads folder (default)

```bash
python organize_files.py
```

#### 🗂️ Option B: Organize a specific folder

```bash
python organize_files.py /path/to/your/folder
```

At the end of the run, the script will:
- Show how many files were moved
- Ask if you want to undo the changes
- Offer to open the move log

---

## 📁 Example Folder Output

If organizing a folder with mixed content, the result might look like this:

```
Downloads/
├── Audio/
│   └── track.wav
├── Code/
│   └── script.py
├── Documents/
│   └── resume.pdf
├── Images/
│   └── photo.jpg
├── Spreadsheets/
│   └── data.csv
├── Video/
│   └── movie.mp4
├── Others/
│   └── unknown.xyz
├── logs/
│   └── file_moves_2025-03-23_141530.txt
```

---

## ✅ Requirements

- Python 3.7 or later
- OS: macOS  
  (Note: log file opening uses the `open` command. GUI + Windows support coming soon.)
- No external libraries required (only Python standard library)

---

## 🧪 Development Roadmap

- [x] Command-line support (`argparse`)
- [ ] GUI interface using `tkinter`
- [ ] Scheduling (e.g., auto-run weekly)
- [ ] Optional exclusion filters (by name or extension)

---

## 📬 Questions or Ideas?

Feel free to open an issue or fork the repo.

---

## 💻 License

MIT License – use it, share it, improve it!
