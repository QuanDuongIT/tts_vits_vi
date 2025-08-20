import os
import tarfile
import urllib.request

def download_and_extract_dataset(url, download_path, extract_path):
    print("Downloading dataset...")
    urllib.request.urlretrieve(url, download_path)
    print("Extracting dataset...")
    with tarfile.open(download_path, "r:gz") as tar:
        tar.extractall(path=extract_path)
    print("Dataset extracted to:", extract_path)

def convert_tsv_to_txt(input_file, output_file):
    print(f"Converting {input_file} to {output_file}...")
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                wav_path, text = parts
                outfile.write(f'{wav_path}|{text}\n')
    print("Conversion complete.")

if __name__ == "__main__":
    dataset_url = "https://huggingface.co/datasets/ntt123/viet-tts-dataset/resolve/main/viet-tts.tar.gz"
    download_path = "viet-tts.tar.gz"
    extract_path = "dataset"
    input_file = os.path.join(extract_path, "meta_data.tsv")
    output_file = os.path.join(extract_path, "meta_data.txt")

    download_and_extract_dataset(dataset_url, download_path, extract_path)
    convert_tsv_to_txt(input_file, output_file)
