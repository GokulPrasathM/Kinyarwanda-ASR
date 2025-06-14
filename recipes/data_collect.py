import os
import tarfile
import zipfile
from kagglehub import dataset_download

# 1. Specify download path
download_path = "track_a_dataset.tar.xz"

# 2. Download the dataset (adjust slug as needed)
digitalumuganda_track_a_kinyarwanda_asr_dataset_path = dataset_download(
    "digitalumuganda/track-a-kinyarwanda-asr-dataset",
    file=download_path  # specify download filename
)

print("Downloaded to:", digitalumuganda_track_a_kinyarwanda_asr_dataset_path)

# 3. Ensure the data folder exists
os.makedirs("data", exist_ok=True)

# 4. Extract the archive into `data/`
if download_path.endswith(".tar.xz") or download_path.endswith(".tar.gz"):
    with tarfile.open(download_path, "r:*") as tar:
        tar.extractall(path="data/")
        print("Extracted tar archive to data/")
elif download_path.endswith(".zip"):
    with zipfile.ZipFile(download_path, "r") as zf:
        zf.extractall(path="data/")
        print("Extracted zip archive to data/")
else:
    raise ValueError(f"Unknown archive type: {download_path}")

# 5. Confirm extraction success by printing structure
for root, dirs, files in os.walk("data"):
    level = root.replace("data", "").count(os.sep)
    indent = " " * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    if level >= 2:
        # stop printing deeper for brevity
        continue
    for f in files[:5]:
        print(f"{indent}  - {f}")
