import google.generativeai as genai
from loguru import logger
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ModerationBlog:
    def __init__(self):
        self.base_url = os.getenv("API_URL")
        self.username = os.getenv("USER_USERNAME")
        self.password = os.getenv("USER_PASSWORD")
        self.info_description = "Використовуй Українську мову та Онови статтю до 3500 символів з оптимізацією під СЕО та граматично правильним текстом, використовуй HTML теги"
        
    def moderation_blog(self):
        response = requests.get(f"{self.base_url}/blogs/")
        for json_data in response.json():
            if json_data["flag"] != True:
                self.generate_content(blog_id=json_data['id'], full_description=json_data['full_description'])
        
    def generate_content(self, blog_id, full_description):
        genai.configure(api_key=os.getenv("API_KEY"))
        model = genai.GenerativeModel('gemini-1.0-pro')
        response = model.generate_content(f"{self.info_description}: {full_description}")
        self.put_blog(blog_id=blog_id, full_description=response.text)
    
    def put_blog(self, blog_id, full_description):
        if full_description != None:
            update_data = {
                'full_description': full_description,
                "flag": True,
            }
            requests.put(f'{self.base_url}/blogs/{blog_id}/', json=update_data, auth=(self.username, self.password))
            
            logger.info(f"Update full_description, blog_id: {blog_id}")
            self.blog_deleted(blog_id)
            
    def blog_deleted(self, blog_id=1006):
        response = requests.get(f"{self.base_url}/blogs/{blog_id}").json()
        if 0 == len(response['full_description']):
            requests.delete(f"{self.base_url}/blogs/{blog_id}", auth=(self.username, self.password))
            logger.info(f"[{blog_id}] Blog deleted successfully")

if __name__ == "__main__":
    moderation = ModerationBlog()
    moderation.moderation_blog()