import os

def rename_images(folder_path, extension=".jpg", sort_by="name"):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(extension)]
    
    # Sorting options
    if sort_by == "name":
        files.sort()
    elif sort_by == "time":
        files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    
    # Step 1: temporary rename (avoid conflicts)
    for i, file in enumerate(files, start=1):
        src = os.path.join(folder_path, file)
        temp_name = os.path.join(folder_path, f"temp_{i}{extension}")
        os.rename(src, temp_name)
    
    # Step 2: final rename
    temp_files = [f for f in os.listdir(folder_path) if f.startswith("temp_")]
    temp_files.sort()
    
    for i, file in enumerate(temp_files, start=1):
        src = os.path.join(folder_path, file)
        final_name = os.path.join(folder_path, f"{i}{extension}")
        os.rename(src, final_name)

    print("Renaming completed successfully!")

# 🔹 Usage
folder = r"C:\Users\misha\abhishek.github.io\Photos"
rename_images(folder, extension=".jpg", sort_by="name")