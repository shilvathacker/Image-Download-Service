#Server side code
from flask import Flask, jsonify, send_file, request
import os
import requests
from urllib.parse import urlparse

app = Flask(__name__)
IMAGE_STORAGE_PATH = "image_storage"

#Endpoint Logic for downloading the images
@app.route('/upload_images', methods=['POST'])
def upload_images():
    data = request.json
    image_links = data.get('image_links', [])

    stored_images = []

    if not os.path.exists(IMAGE_STORAGE_PATH):
        os.makedirs(IMAGE_STORAGE_PATH)

    for link in image_links:
        try:
            parsed_link = urlparse(link)
            if parsed_link.scheme in ('http', 'https'):
                response = requests.get(link)
                if response.status_code == 200:
                    image_name = os.path.basename(parsed_link.path)
                    image_path = os.path.join(IMAGE_STORAGE_PATH, image_name)
                    with open(image_path, 'wb') as f:
                        f.write(response.content)
                    stored_images.append(link)
        except Exception as e:
            print(f"Error downloading {link}: {e}")
    
    return jsonify({'stored_images': stored_images})

#Endpoint logic for showing the available images
@app.route('/list_images', methods=['GET'])
def list_images():

    stored_images = []
    if os.path.exists(IMAGE_STORAGE_PATH):
        stored_images = [filename for filename in os.listdir(IMAGE_STORAGE_PATH)]
    return jsonify({'stored_images': stored_images})

#Endpoint logic for showing the retrieving the image provided in image url
@app.route('/retrieve_image', methods=['GET'])
def retrieve_image():
    image_url = request.args.get('image_url')
    image_name = os.path.basename(urlparse(image_url).path)
    image_path = os.path.join(IMAGE_STORAGE_PATH, image_name)
    
    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return jsonify({'message': 'Image not found'})

if __name__ == '__main__':
    app.run(debug=True)
