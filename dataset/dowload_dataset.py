import os
import argparse
import requests
import zipfile
import shutil
from tqdm import tqdm  # Thanh tiến độ

def download_and_prepare_dataset(destination_path):
    url = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/4gzzc9k49n-4.zip"
    zip_path = "dataset.zip"
    dataset_dir = "dataset_FOSD"

    print(f"🔽 Đang tải dataset từ {url} ...")

    # Tải về với thanh tiến độ
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('Content-Length', 0))
        block_size = 8192

        with open(zip_path, 'wb') as f, tqdm(
            total=total_size, unit='B', unit_scale=True, desc="📥 Tải về", ncols=80
        ) as progress_bar:
            for chunk in r.iter_content(chunk_size=block_size):
                f.write(chunk)
                progress_bar.update(len(chunk))

    print("✅ Tải xong.")

    if os.path.exists(dataset_dir):
        shutil.rmtree(dataset_dir)
        print("🧹 Đã xóa thư mục dataset cũ.")

    print("📦 Đang giải nén...")

    # Giải nén với tiến độ
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_list = zip_ref.infolist()  # Danh sách các file trong zip
        with tqdm(total=len(zip_list), desc="🗂️  Đang giải nén", unit="file", ncols=80) as progress_bar:
            for file in zip_list:
                zip_ref.extract(file, dataset_dir)
                progress_bar.update(1)

    print("✅ Giải nén xong.")

    # Di chuyển thư mục con
    src = os.path.join(dataset_dir, "FOSD Female Speech Dataset", "Female 16k")

    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    shutil.move(src, destination_path)
    print(f"✅ Đã chuyển thư mục tới: {destination_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and prepare FOSD Female Speech Dataset.")
    parser.add_argument("--destination_path", required=True, help="Đường dẫn đích để lưu thư mục 'Female 16k'")
    args = parser.parse_args()
    download_and_prepare_dataset(args.destination_path)
