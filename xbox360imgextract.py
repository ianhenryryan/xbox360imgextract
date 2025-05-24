import os
from tqdm import tqdm

# img headers & types
IMAGE_SIGNATURES = {
    b"\x89PNG\r\n\x1a\n": "png",
    b"\xFF\xD8\xFF": "jpg",
    b"GIF87a": "gif",
    b"GIF89a": "gif",
}

# num bytes to scan after sig
DEFAULT_CHUNK_SIZE = 102400  # 100KB

def extract_images_from_file(filepath, output_dir):
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
    except:
        return 0

    extracted_count = 0
    for sig, ext in IMAGE_SIGNATURES.items():
        index = 0
        while True:
            index = data.find(sig, index)
            if index == -1:
                break

            end = index + DEFAULT_CHUNK_SIZE
            if end > len(data):
                end = len(data)

            chunk = data[index:end]
            output_path = os.path.join(output_dir, f"{os.path.basename(filepath)}_{extracted_count}.{ext}")
            with open(output_path, 'wb') as out_file:
                out_file.write(chunk)

            extracted_count += 1
            index += len(sig)
    return extracted_count

def walk_and_extract_images(root_folder):
    output_dir = os.path.join(root_folder, "img_extracts")
    os.makedirs(output_dir, exist_ok=True)

    all_files = []
    for root, dirs, files in os.walk(root_folder):
        for name in files:
            full_path = os.path.join(root, name)
            all_files.append(full_path)

    print(f"Scanning {len(all_files)} files for embedded images.\n")

    total_images = 0
    for file_path in tqdm(all_files, desc="Extracting images"):
        total_images += extract_images_from_file(file_path, output_dir)

    print(f"\nExtract Finished. {total_images} images saved: {output_dir}")

if __name__ == "__main__":
    folder = input("Enter folder path: ").strip('"')
    walk_and_extract_images(folder)

