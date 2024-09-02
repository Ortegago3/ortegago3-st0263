from flask import Flask, request, jsonify, send_from_directory
import os
import requests

app = Flask(__name__)

peers = []  # Lista de peers conocidos

@app.route('/register_peer', methods=['POST'])
def register_peer():
    peer_info = request.json
    if peer_info not in peers:
        peers.append(peer_info)
    return jsonify(peers)

@app.route('/list_files', methods=['GET'])
def list_files():
    directory = request.args.get('directory')
    try:
        if not os.path.exists(directory):
            return jsonify({"error": f"Directory '{directory}' not found"}), 404
        files = os.listdir(directory)
        return jsonify(files)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/find_file', methods=['GET'])
def find_file():
    filename = request.args.get('filename')
    for peer in peers:
        try:
            response = requests.get(f"{peer['url']}/list_files", params={"directory": peer['directory']})
            if response.status_code == 200 and filename in response.json():
                return jsonify({"peer": peer, "filename": filename})
        except Exception as e:
            print(f"Error contacting peer {peer['url']}: {e}")
            continue
    return jsonify({"error": "File not found"}), 404

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file.save(os.path.join(upload_dir, file.filename))
    return jsonify({"status": "File uploaded successfully"}), 200

@app.route('/download', methods=['GET'])
def download_file():
    filename = request.args.get('filename')
    directory = request.args.get('directory')
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        return send_from_directory(directory, filename, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404

@app.route('/notify', methods=['POST'])
def receive_notification():
    data = request.json
    print(f"Notification received: {data['message']}")
    return jsonify({"status": "Notification received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
