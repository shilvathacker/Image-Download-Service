import requests
from urllib.parse import urlparse
import os

def extract_image_name(image_url):
    parsed_url = urlparse(image_url)
    image_path = parsed_url.path
    image_name = os.path.basename(image_path)
    return image_name

# Server URL
BASE_URL = 'http://127.0.0.1:5000'

# Endpoint URLs
UPLOAD_IMAGES_URL =f'{BASE_URL}/upload_images'
LIST_IMAGES_URL = f'{BASE_URL}/list_images'
RETRIEVE_IMAGE_URL = f'{BASE_URL}/retrieve_image'

# Upload the list of image URLs
image_links = ["http://pngimg.com/uploads/butterfly/butterfly_PNG1037.png","http://pngimg.com/uploads/plum/plum_PNG8662.png"]

# 1. Operation 1: Upload images
payload = {'image_links': image_links}
response = requests.post(UPLOAD_IMAGES_URL, json=payload)

if response.status_code == 200:
    stored_images = response.json().get('stored_images')
    print("Uploaded images successfully.....")
    print("Downloaded Images are:\n", stored_images)
    
    
else:
    print("Failed to upload images")
    print(response.json()) 

# 2. Operation 2: List available images
response = requests.get(LIST_IMAGES_URL)

if response.status_code == 200:
    available_images = response.json().get('stored_images')
    print("\nAvailable images:")
    print(available_images)
    print("Link to view the list of available images:", LIST_IMAGES_URL)

else:
    print("Failed to list images")

# 3. Operation 3: Retrieve an image 
# (change 'image_url' to the desired image URL)
image_url = "http://pngimg.com/uploads/plum/plum_PNG8662.png"
image_name = extract_image_name(image_url)

if image_name in available_images:
    retrieve_params = {'image_url': image_url}
    response = requests.get(RETRIEVE_IMAGE_URL, params=retrieve_params) 

    # Check if retrieving the image was successful
    if response.status_code == 200:
        #with open('retrieved_image.jpg', 'wb') as f:
            #f.write(response.content)
        print("\nRetrieved image successfully......")
        print("Link to retrieve the image:", RETRIEVE_IMAGE_URL + f"?image_url={image_url}")
    else:
        print("Failed to retrieve image")
else:
    print("The specified image URL is not available or hasn't been uploaded previously.")
 