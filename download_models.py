# download_models.py
import gdown
import os

# Model files configuration
files = {
    '16rCpiE5gX4TzgrQ2gnNG5wkHnJfToRBC': 'gbm_drug_recommendation_model.pkl',
    '14SLBek0cIV-wGh0E2vObMKPEardIEQjx': 'label_encoder.pkl'
}

def download_files():
    for file_id, filename in files.items():
        if not os.path.exists(filename):
            url = f'https://drive.google.com/uc?id={file_id}'
            gdown.download(url, filename, quiet=False)
            print(f"Downloaded {filename}")
        else:
            print(f"{filename} already exists")

if __name__ == '__main__':
    download_files()
