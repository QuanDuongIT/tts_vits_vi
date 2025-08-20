import os
import tarfile
import urllib.request
import argparse
from tqdm import tqdm

def download_and_extract_dataset(url, download_path, extract_path):
    print("📥 Downloading dataset...")
    urllib.request.urlretrieve(url, download_path)
    print("📦 Extracting dataset...")
    with tarfile.open(download_path, "r:gz") as tar:
        tar.extractall(path=extract_path)
    print(f"✅ Dataset extracted to: {extract_path}")

def convert_tsv_to_txt(input_file, output_file):
    print(f"🔄 Converting {input_file} to {output_file}...")
    
    # Đếm số dòng để tạo thanh tiến độ
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in tqdm(lines, desc="🔁 Processing lines"):
            parts = line.strip().split('\t')
            if len(parts) == 2:
                wav_path, text = parts
                outfile.write(f'{wav_path}|{text}\n')

    print("✅ Conversion complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download VietTTS dataset and convert TSV to TXT.")
    parser.add_argument('--output', type=str, default='dataset/meta_data.txt',
                        help='Path to save the output .txt file (default: dataset/meta_data.txt)')
    args = parser.parse_args()

    dataset_url = "https://huggingface.co/datasets/ntt123/viet-tts-dataset/resolve/main/viet-tts.tar.gz"
    download_path = "viet-tts.tar.gz"
    extract_path = "dataset"
    input_file = os.path.join(extract_path, "meta_data.tsv")
    output_file = args.output

    # Đảm bảo thư mục output tồn tại
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    download_and_extract_dataset(dataset_url, download_path, extract_path)
    convert_tsv_to_txt(input_file, output_file)
