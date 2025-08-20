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

def convert_tsv_to_txt(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'meta_data.txt')
    print(f"🔄 Converting {input_file} to {output_file}...")
    
    # Đọc toàn bộ dòng để đếm và tạo thanh tiến độ
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
                        help='Directory to save the output meta_data.txt (default: dataset/)')
    args = parser.parse_args()

    dataset_url = "https://huggingface.co/datasets/ntt123/viet-tts-dataset/resolve/main/viet-tts.tar.gz"
    download_path = "viet-tts.tar.gz"
    extract_path = "dataset"
    input_file = os.path.join(extract_path, "meta_data.tsv")

    download_and_extract_dataset(dataset_url, download_path, extract_path)
    convert_tsv_to_txt(input_file, args.output)

