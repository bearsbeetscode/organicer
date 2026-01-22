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
}


def organize():
    if not DOWNLOADS_PATH.exists():
        print(f"Directory {DOWNLOADS_PATH} not found.")
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
                except Exception as e:
                    print(f"Failed to move {file_path.name}: {e}")
            else:
                print(f"No rule for extension: {ext} ({file_path.name})")


if __name__ == "__main__":
    organize()
