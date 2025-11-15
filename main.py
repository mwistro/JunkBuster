import os
import shutil

# Safe folders
TEMP_USER = os.environ["TEMP"]
TEMP_WINDOWS = os.path.join(os.environ["WINDIR"], "Temp")
CBS_LOGS = os.path.join(os.environ["WINDIR"], "Logs", "CBS")
MINIDUMP = os.path.join(os.environ["WINDIR"], "Minidump")

FOLDERS = [
    ("TEMP_USER", TEMP_USER),
    ("TEMP_WINDOWS", TEMP_WINDOWS),
    ("CBS_LOGS", CBS_LOGS),
    ("MINIDUMP", MINIDUMP),
]

def folder_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except:
                pass
    return total

def format_size(b):
    for u in ["B", "KB", "MB", "GB"]:
        if b < 1024:
            return f"{b:.2f} {u}"
        b /= 1024
    return f"{b:.2f} TB"

def clean_folder(path):
    for item in os.listdir(path):
        p = os.path.join(path, item)
        try:
            if os.path.isfile(p):
                os.remove(p)
            else:
                shutil.rmtree(p)
        except:
            pass  # ignore errors (file in use, perms, etc.)

print("=== FOLDER SIZE OVERVIEW ===\n")

# Store sizes before for later comparison
sizes_before = {}

for name, path in FOLDERS:
    size_b = folder_size(path)
    sizes_before[name] = size_b
    print(f"{name}")
    print(f"  Size before: {format_size(size_b)}\n")

input("Press ENTER to begin cleaning...\n")

total_removed_global = 0

for name, path in FOLDERS:
    choice = input(f"Clean {name}? (y/N): ").lower()

    if choice == "y":
        clean_folder(path)
        size_after = folder_size(path)

        removed = sizes_before[name] - size_after
        total_removed_global += removed

        print(f"  Size after: {format_size(size_after)}")
        print(f"  Removed: {format_size(removed)}\n")
    else:
        print("  Skipped.\n")

print("=== FINAL RESULT ===")
print(f"Total removed: {format_size(total_removed_global)}")

input("\nPress ENTER to exit...")