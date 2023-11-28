# Image-Download-Service
This Flask application allows users to upload images from provided list of URLs, list stored images, and retrieve specific images based on their URLs.

## Installation
- Clone the project:
```bash
https://github.com/shilvathacker/Image-Download-Service.git
```
- Install the required dependencies:
```bash
pip install -r requirements.txt
```
- Now in the **client.py**, enter the list of image urls and also entire the image url you want to retrieve. 

- Run the Flask application in one terminal shell:
```bash
python app.py
```
- and then run the client side file in other terminal shell:
```bash
python client.py
```


## Usage

1. **Upload Images**

 -      - Endpoint: /upload_images
        - Method: POST
        - Description: Upload images from the provided list  of URLs.
        - Request Payload: JSON object with a list of image URLs.
2. **List Stored Images**
 -      - Endpoint: /list_images
        - Method: GET
        - Description: List all stored image filenames.

3. **Retrieve Image**
-       - Endpoint: /retrieve_image
        - Method: GET
        - Description: Retrieve a specific image based on its URL.
        - Query Parameter: image_url (URL of the image to retrieve)

## Folder Structure
- **app.py:** Flask application file containing the endpoints and logic.
- **client.py:** Python file where there is a logic and input parameters handled by client.  
- **image_storage/:**  Local Directory where uploaded images are stored.







