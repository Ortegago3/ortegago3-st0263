import requests
import json
import os

def register_with_peer(peer_url, config):
    try:
        response = requests.post(f"{peer_url}/register_peer", json=config)
        if response.status_code == 200:
            print(f"Successfully registered with peer: {peer_url}")
        else:
            print(f"Failed to register with peer: {peer_url} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error during peer registration: {e}")

def find_file(peer_url, filename):
    try:
        response = requests.get(f"{peer_url}/find_file", params={"filename": filename})
        if response.status_code == 200:
            print(f"File found: {response.json()}")
        else:
            print("File not found.")
    except Exception as e:
        print(f"Error during file search: {e}")

def upload_file(peer_url, file_path):
    try:
        print(f"Attempting to open file: {file_path}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at path: {file_path}")
        with open(file_path, 'rb') as file:
            response = requests.post(f"{peer_url}/upload", files={"file": file})
        if response.status_code == 200:
            print("File uploaded successfully.")
            notify_peer(peer_url, f"New file uploaded: {file_path}")
        else:
            print(f"Failed to upload file - Status Code: {response.status_code}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except Exception as e:
        print(f"Error during file upload: {e}")

def download_file(peer_url, filename, directory):
    try:
        response = requests.get(f"{peer_url}/download", params={"filename": filename, "directory": directory})
        if response.status_code == 200:
            print("File download ready.")
        else:
            print(f"Failed to download file - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error during file download: {e}")

def notify_peer(peer_url, message):
    try:
        response = requests.post(f"{peer_url}/notify", json={"message": message})
        if response.status_code == 200:
            print(f"Notification sent to peer: {peer_url}")
        else:
            print(f"Failed to notify peer: {peer_url} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error during notification: {e}")

if __name__ == "__main__":
    try:
        with open('../config/peer1_config.json', 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError as e:
        print(f"Configuration file not found: {e}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON configuration file: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error loading configuration: {e}")
        exit(1)

    peer_seed_url = config.get('peer_seed_url')
    if not peer_seed_url:
        print("peer_seed_url is not defined in the configuration file.")
        exit(1)

    register_with_peer(peer_seed_url, config)

    # Find a file in the network
    find_file(peer_seed_url, "test.txt")

    # Upload file with absolute path
    upload_file(peer_seed_url, "C:/Users/holme/OneDrive/Escritorio/Universidad/Noveno Semestre/Topicos Telematica/reto1/ortegago3-st0263/src/shared/files/test.txt")
    
    # Download file to specified directory
    download_file(peer_seed_url, "test.txt", "C:/Users/holme/OneDrive/Escritorio/Universidad/Noveno Semestre/Topicos Telematica/reto1/ortegago3-st0263/src/shared/files")
