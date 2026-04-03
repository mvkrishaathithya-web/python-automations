import os
import shutil

folders = {
    "PDFs"      : [".pdf"],
    "Images"    : [".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif", ".heic", ".svg", ".ico"],
    "Videos"    : [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Music"     : [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Zips"      : [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code"      : [".py", ".js", ".html", ".css", ".json", ".xml", ".ts"],
    "Documents" : [".txt", ".docx", ".doc", ".pptx", ".xlsx", ".csv"],
    "Apps"      : [".exe", ".dmg", ".pkg", ".apk"],
    "Books"     : [".epub", ".mobi"],
}

downloads_path = input("Enter the folder path to sort: ").strip()

if not os.path.exists(downloads_path):
    print("❌ That folder doesn't exist! Check the path and try again.")
else:
    print(f"✅ Found it! Sorting {downloads_path}...")
    print("---")

    moved = 0
    skipped = 0

    for file in os.listdir(downloads_path):
        full_path = os.path.join(downloads_path, file)

        if os.path.isdir(full_path):
            continue

        name, extension = os.path.splitext(file)
        matched = False

        for folder_name, extensions in folders.items():
            if extension.lower() in extensions:
                folder_path = os.path.join(downloads_path, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(full_path, os.path.join(folder_path, file))
                print(f"✅ Moved {file} → {folder_name}")
                matched = True
                moved += 1
                break

        if not matched:
            other_path = os.path.join(downloads_path, "Others")
            os.makedirs(other_path, exist_ok=True)
            shutil.move(full_path, os.path.join(other_path, file))
            print(f"📦 Moved {file} → Others")
            skipped += 1

    print("---")
    print(f"🎉 Done! {moved} files sorted, {skipped} files moved to Others")