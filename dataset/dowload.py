import os
import requests
import zipfile
import shutil

# Tải file zip
url = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/4gzzc9k49n-4.zip"
zip_path = "dataset.zip"

print("Downloading dataset...")
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(zip_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
print("Download complete.")

# Xóa thư mục dataset nếu tồn tại
dataset_dir = "dataset"
if os.path.exists(dataset_dir):
    shutil.rmtree(dataset_dir)
    print("Old dataset directory removed.")

# Giải nén file zip
print("Unzipping dataset...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(dataset_dir)
print("Unzipping complete.")

# Di chuyển thư mục Female 16k tới /content/Female
src = os.path.join(dataset_dir, "FOSD Female Speech Dataset", "Female 16k")
dst = "Female"
if os.path.exists(dst):
    shutil.rmtree(dst)  # Xóa nếu thư mục Female đã tồn tại
shutil.move(src, dst)
print(f"Moved '{src}' to '{dst}'.")

# Nếu muốn, bạn có thể xóa thư mục dataset sau khi xử lý xong
# shutil.rmtree(dataset_dir)
