import os
import shutil
from pathlib import Path
from datetime import datetime
import random
import subprocess  # Used to open files (macOS only)
import argparse  # For command-line arguments

# 🔹 File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".js", ".html"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".mov", ".avi"],
}


def organize_folder(folder_path):
    """
    Organizes files in the given folder into subfolders based on file type.
    Also logs all moves, supports undo, and offers to open the move log.
    """
    hidden_files_skipped = 0
    hidden_file_names = []
    move_history = []

    logs_dir = folder_path / "logs"
    logs_dir.mkdir(exist_ok=True)

    for item in folder_path.iterdir():
        if item.name.startswith('.'):
            hidden_files_skipped += 1
            hidden_file_names.append(item.name)
            continue

        if item.is_file():
            matched = False

            for folder_name, extensions in FILE_TYPES.items():
                if item.suffix.lower() in extensions:
                    new_dir = folder_path / folder_name
                    new_dir.mkdir(exist_ok=True)
                    dest = new_dir / item.name
                    shutil.move(str(item), dest)
                    print(f"Moved {item.name} → {folder_name}")
                    move_history.append((dest, item))
                    matched = True
                    break

            if not matched:
                other_dir = folder_path / "Others"
                other_dir.mkdir(exist_ok=True)
                dest = other_dir / item.name
                shutil.move(str(item), dest)
                print(f"Moved {item.name} → Others")
                move_history.append((dest, item))

    print(f"\nSkipped {hidden_files_skipped} hidden file(s).")
    if hidden_file_names:
        print("Hidden files skipped:")
        for name in hidden_file_names:
            print(f" - {name}")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_filename = f"file_moves_{timestamp}.txt"
    log_path = logs_dir / log_filename

    with open(log_path, "w") as log_file:
        for new_path, old_path in move_history:
            log_file.write(f"{new_path} → {old_path}\n")

    print(f"\n📝 Move history saved to: {log_path}")

    undo = input("↩️  Undo all moves? (y/n): ")
    if undo.lower() in ['y', 'yes']:
        for new_path, old_path in move_history:
            shutil.move(str(new_path), str(old_path))
            print(f"Restored {new_path.name} to original folder.")
    else:
        messages = [
            "🙏 Thanks for using the File Organizer. Stay tidy out there!",
            "🧹 Another day, another clean folder. You're crushing it!",
            "🎯 Mission accomplished. File chaos defeated!",
            "💾 Order restored. Your Downloads folder thanks you.",
            "📦 All sorted — feels good, right?"
        ]
        print("\n✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
        print("🎉 All done! Your files have been neatly organized.")
        print(f"✅ {len(move_history)} files moved into categorized folders.")
        print(f"🧼 {hidden_files_skipped} hidden file(s) were skipped.")
        print(f"🗂️ Move history saved to: {log_path}")
        print(random.choice(messages))
        print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n")

        open_log = input("📂 Would you like to open the log file now? (y/n): ")
        if open_log.lower() in ['y', 'yes']:
            try:
                subprocess.run(["open", str(log_path)])  # macOS
            except Exception as e:
                print(f"⚠️ Couldn't open the file: {e}")
        else:
            print(f"📁 Log file not opened — you can find it later here:\n{log_path}")


def main():
    """Handles command-line arguments and starts the organizer."""
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument(
        "folder", nargs="?", default=str(Path.home() / "Downloads"),
        help="Path to the folder you want to organize (default: Downloads)"
    )
    args = parser.parse_args()
    folder_path = Path(args.folder)

    if not folder_path.exists() or not folder_path.is_dir():
        print(f"❌ The provided path does not exist or is not a folder:\n{folder_path}")
        return

    print(f"📂 Organizing folder: {folder_path}")
    organize_folder(folder_path)


# 🏁 Run the script
if __name__ == "__main__":
    main()
