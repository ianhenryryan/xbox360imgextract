╔═════════════════════════════════════════════════════╗  
║ Xbox 360 Hard Drive Partition 3 Contents Extractor ║  
╚═════════════════════════════════════════════════════╝  

╔═════════════════════════════════════════════════╗  
║ Partition 3 in the Xbox 360 Hard Drive contains ║  
╚═════════════════════════════════════════════════╝  
  └── 0000000000000000 Folder  
      └── System Wide Content: DLC, Gamerpic Packs, Themes, XBLA  
  └── E0000035D80184C8 Folders (varies per user profile)  
      └── User Profile Content: Gamertag, Gamerpic, Avatar Data, Save Settings  

---

## 🎬 Demo  
![Xbox 360 Partition 3 Image Extractor](demo/xbox360extract-ezgif.com-speed.gif)  

---

## 🖥️ Use  
```bash
$ python3 xbox360imgextract.py  
Enter folder path: .
```

---

## 📦 Imports  
- `os` – standard Python library for file and directory operations  
- `tqdm` – adds a visual loading/progress bar for file processing  

---

## 🧠 Image Header Signatures  
**Formats Supported:** PNG, JPEG, GIF (87a & 89a)  
- Maps file signature bytes (magic numbers) to image file types  
- Detects embedded images in binary files  

---

## 🧱 Chunk Size  
- Defines how much data to extract after an image signature is found  
- Prevents saving entire binary files unnecessarily  

---

## 🔍 Extract Image Function  
`def extract_images_from_file(filepath, output_dir):`  
- Reads binary file → Searches for known image signatures  
- If match:  
  → Extracts 100KB chunk or to EOF  
  → Saves as image in output directory  
- Returns number of images extracted from the file  

---

## 📁 Directory Walk & Extract  
`def walk_and_extract_images(root_folder):`  
- Recursively traverses nested folders  
- Calls `extract_images_from_file()` on every file  
- Tracks total images extracted and saves them to `/img_extracts`  
- Displays a progress bar using `tqdm`  

---

## 🚀 Script Entry Point  
```python
if __name__ == "__main__":
```
- Prompts the user to input a folder path  

---

## 📝 Summary  
- Recursively scans all files in the specified folder  
- Detects embedded image file signatures  
- Extracts chunks from matched signatures  
- Saves images to `/img_extracts`  
- Visual progress via loading bar  

---

## 📊 ASCII Diagram  

```
+-----------------------------+
|      User Input path        |
+-------------+---------------+
              |
              v
+-----------------------------+
| Create img_extracts folder  |
+-------------+---------------+
              |
              v
+-----------------------------+
| Recursively walk all files  |
+-------------+---------------+
              |
              v
+-----------------------------+
|       For each file:        |
|  ┌────────────────────────┐ |
|  │  Open file in binary   │ |
|  │     Read contents      │ |
|  └────────────────────────┘ |
|  For each image signature:  |
|   ┌──────────────────────┐  |
|   │ Search for signature │  |
|   │ If found:            │  |
|   │  • Extract chunk     │  |
|   │  • Save as png/jpg   │  |
|   │  • Increment counter │  |
|   └──────────────────────┘  |
+-------------+---------------+
              |
              v
+-----------------------------+
|    Show via progress bar    |
+-------------+---------------+
              |
              v
+-----------------------------+
|  Print total image count    |
|   & path to saved files     |
+-----------------------------+
              |
              v
           +-----+
           | End |
           +-----+
```
