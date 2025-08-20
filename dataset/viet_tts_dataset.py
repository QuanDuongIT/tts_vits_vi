import os
import tarfile
import argparse
import requests
from tqdm import tqdm

def download_with_progress(url, output_path):
    print("📥 Downloading dataset with progress bar...")
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1KB

    with open(output_path, 'wb') as file, tqdm(
        desc="⬇️ Download",
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            file.write(data)
            bar.update(len(data))
    print(f"✅ Downloaded to {output_path}")

def extract_with_progress(tar_path, extract_path):
    print("📦 Extracting dataset with progress bar...")
    with tarfile.open(tar_path, "r:gz") as tar:
        members = tar.getmembers()
        with tqdm(total=len(members), desc="📂 Extracting") as bar:
            for member in members:
                tar.extract(member, path=extract_path)
                bar.update(1)
    print(f"✅ Extracted to {extract_path}")

def convert_tsv_to_txt(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'meta_data.txt')
    print(f"🔄 Converting {input_file} to {output_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in tqdm(lines, desc="🔁 Processing lines"):
            parts = line.strip().split('\t')
            if len(parts) == 2:
                wav_path, text = parts
                outfile.write(f'{wav_path}|{text}\n')

    print("✅ Conversion complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download VietTTS dataset and convert TSV to TXT.")
    parser.add_argument('--output', type=str, default='dataset/',
                        help='Directory to save the extracted data and output meta_data.txt (default: dataset/)')
    args = parser.parse_args()

    dataset_url = "https://huggingface.co/datasets/ntt123/viet-tts-dataset/resolve/main/viet-tts.tar.gz"
    download_path = "viet-tts.tar.gz"
    extract_path = args.output  # <-- thay đổi ở đây
    input_file = os.path.join(extract_path, "meta_data.tsv")

    download_with_progress(dataset_url, download_path)
    extract_with_progress(download_path, extract_path)
    convert_tsv_to_txt(input_file, args.output)
