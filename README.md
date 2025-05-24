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

╔══════╗
║ Demo ║
╚══════╝
![Xbox 360 Partition 3 Image Extractor](demo/xbox360extract-ezgif.com-speed.gif)

╔═════╗
║ Use ║
╚═════╝
$ python3 xbox360imgextract.py
Enter folder path: .

╔═════════╗
║ Imports ║
╚═════════╝
os - basic python library for operating system interaction
tqdm - loading bar/progress bar visualization for file processing

╔═════════════════════════╗
║ Image Header Signatures ║
╚═════════════════════════╝
Formats: png, jpeg, gif (older & newer)
Does: Maps file signature bytes aka magic numbers to the corresponding file types.
Use: Detect embedded images in binary files.

╔════════════╗
║ Chunk Size ║
╚════════════╝
Does: Controls how much data is extracted after a signature is found.
Use: Prevents writing entire files unnecessarily.

╔═════════════════════════════════════════╗
║ Extract Image Function from Binary File ║
╚═════════════════════════════════════════╝
def extract_images_from_file(filepath, output_dir):
Does: Reads a binary file and searches for known image signatures.
Use: If match -> Extracts 100KB chunk or to EOF -> Saves as image in output dir.
     Returns # of images extracted from specific file.
Recap of Key Segments: Read full binary content -> Search for image signature -> write image chunk to file.

╔══════════════════════════╗
║ Directory Walk & Extract ║
╚══════════════════════════╝
def walk_and_extract_images(root_folder):
Does: Recursively traverses nested folders and calls extract image function on each file.
Use: Tracks total # images extracted & saves to /img_extracts sub-directory.
Recap of Key Segments: Walks every directory & file -> Shows a progress bar via tqdm

╔═══════════════════════════╗
║ Main & Script Entry Point ║
╚═══════════════════════════╝
if __name__ == "__main__":
Use: Prompts user for a folder path.

╔═════════╗
║ Summary ║
╚═════════╝
- Recursively scans all files in a folder.
- Checks for embedded image file sigs.
- Extracts a chunk starting from each sig.
- Saves extracted data as img files in /img_extracts.
- Progress bar for download.

╔═══════════════╗
║ ASCII Diagram ║
╚═══════════════╝
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
