import requests
import os
from datetime import datetime
from loguru import logger

folder_path = "blog/media/blog/img"

def download_image(image_url):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    response = requests.get(image_url)
    if response.status_code == 200:
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        image_name = f"image_{current_time}.jpg"
        image_path = os.path.join(folder_path, image_name)
        with open(image_path, 'wb') as f:
            f.write(response.content)
        logger.info("Image successfully saved!", image_path)
        return image_path
    else:
        logger.error("Failed to load image")