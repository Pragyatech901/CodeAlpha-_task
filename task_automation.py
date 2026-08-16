import os
import shutil

source_folder = "photos"
destination_folder = "new_photos"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(file, "moved successfully!")

print("All JPG files moved successfully.")
