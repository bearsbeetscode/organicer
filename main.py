import subprocess
from pathlib import Path
import shutil

DOWNLOADS_PATH = Path.home() / "Downloads"

DIRECTORY_MAP = {
    ".jpg": "Pictures",
    ".jpeg": "Pictures",
    ".png": "Pictures",
    ".mp4": "Music",
    ".mkv": "Music",
    ".mp3": "Music",
    ".flac": "Music",
    ".wav": "Music",
    ".pdf": "Books",
    ".fb2": "Books",
    ".epub": "Books",
    ".mobi": "Books",
}

moving_info = {}


def notify(title, message):
    """
    Sends passive KDE notification.
    """
    subprocess.run(["kdialog", "--title", title, "--passivepopup", message, "5"])


def organize():
    files_moved = 0
    if not DOWNLOADS_PATH.exists():
        print(f"Directory {DOWNLOADS_PATH} not found.")
        return
    ask = subprocess.run(
        ["kdialog", "--title", "Sure 'bout this?", "--yesno", "Start moving files?"]
    )
    if ask.returncode != 0:
        print("User cancelled")
        return

    for file_path in DOWNLOADS_PATH.iterdir():
        if file_path.is_file():
            ext = file_path.suffix.lower()

            if ext in DIRECTORY_MAP:
                dest_dir = Path.home() / DIRECTORY_MAP[ext]
                dest_dir.mkdir(exist_ok=True)
                dest_path = dest_dir / file_path.name

                try:
                    print(f"Moving {file_path.name} to {dest_dir}")
                    shutil.move(str(file_path), str(dest_path))
                    files_moved += 1
                    # Update moving info
                    if dest_dir in moving_info:
                        moving_info[dest_dir] += 1
                    else:
                        moving_info[dest_dir] = 1
                except Exception as e:
                    print(f"Failed to move {file_path.name}: {e}")
            else:
                print(f"No rule for extension: {ext} ({file_path.name})")
    print("\n ---Finished---")
    if not moving_info:
        print("No files moved, cuz emty foder, bruh")
    else:
        notify("Great", f"Moved {files_moved} files.")
        for folder, count in moving_info.items():
            print(f"Moved {count} files to {folder}.")


if __name__ == "__main__":
    organize()
