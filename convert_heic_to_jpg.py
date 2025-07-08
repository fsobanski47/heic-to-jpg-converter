import os
import sys
from pathlib import Path
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()

def convert_all_heic_in_folder(folder_path, output_folder_name):
    input_folder = Path(folder_path)
    if not input_folder.is_dir():
        print(f"This path is not a folder: {input_folder}")
        return

    output_folder = input_folder / output_folder_name
    output_folder.mkdir(exist_ok=True)

    heic_files = list(input_folder.glob("*.heic")) + list(input_folder.glob("*.HEIC"))

    if not heic_files:
        print("No HEIC files in this folder.")
        return

    for heic_file in heic_files:
        jpg_file = output_folder / (heic_file.stem + ".jpg")
        try:
            with Image.open(heic_file) as img:
                img.save(jpg_file, "JPEG")
            print(f"{heic_file.name} -> {output_folder_name}/{jpg_file.name}")
        except Exception as e:
            print(f"Error converting {heic_file.name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        folder = input("HEIC images folder path: ")
        output_folder_name = input("JPG folder name: ")
    else:
        folder = sys.argv[1]
        output_folder_name = sys.argv[2]

    convert_all_heic_in_folder(folder, output_folder_name)