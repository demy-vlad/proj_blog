import os
from bs4 import BeautifulSoup
import requests
from loguru import logger
import json
from datetime import datetime
from dotenv import load_dotenv
from web_scraping.image_downloader import download_image

load_dotenv()


class BlogScraper:
    def __init__(self):
        self.base_url = os.getenv("API_URL")
        self.username = os.getenv("USER_USERNAME")
        self.password = os.getenv("USER_PASSWORD")
        self.page_title_art_nav = "body > div.common-table-div.d-flex.s-width > div.main-part-content > div.page-title-art"
        self.page_num_nav = "body > div.common-table-div.d-flex.s-width > div.main-part-content > div.list-pager > div > a.ib"
        self.articles_cell_navs = ".articles-cell"
        self.post_notice_nav = "body > div.common-table-div.d-flex.s-width > div.main-part-content > div.post-notice"
        self.post_content_nav = "body > div.common-table-div.d-flex.s-width > div.main-part-content > div.post-content"
        self.keywords_header_nav = "head > meta:nth-child(5)"
        self.description_header_nav = "head > meta:nth-child(6)"

    def get_all_catalogs(self):
        response = requests.get(f"{self.base_url}/catalogs/", auth=(self.username, self.password))
        if response.status_code == 200:
            json_data = json.loads(response.text)
            self.get_requests_html_text(json_data)
        else:
            logger.error(f"The request failed: {response.status_code}")

    def get_requests_html_text(self, data):
        try:
            for item in data:
                logger.info("[START SCRAPING]")
                logger.debug(item)
                response = requests.get(item['url_catalog'])
                if response.status_code == 200:
                    self.get_all_pagination(response.text, item)
                else:
                    logger.error(f"Error while getting data. Response code: {response.status_code}")
        except requests.exceptions.RequestException as error:
            logger.error(f"The request failed: {error}")

    def get_all_pagination(self, requests_html, url_data):
        soup = BeautifulSoup(requests_html, 'html.parser')
        page_nums = soup.select(self.page_num_nav)
        for page_num in page_nums:
            self.get_blog_preview(f"{url_data['url_catalog'][:11]}{page_num.get('href')[1:]}", url_data)

    def get_blog_preview(self, page_num_url, url_data):
        try:
            article_dict = {}
            logger.info(page_num_url)
            response = requests.get(page_num_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for index, articles_cell_nav in enumerate(soup.select(self.articles_cell_navs)):
                href = articles_cell_nav.find('a').get('href')
                title = articles_cell_nav.find('a').get('title')
                src = articles_cell_nav.select_one('img').get('src') if articles_cell_nav.select_one('img') else None
                article_desc = articles_cell_nav.find(class_='article-desc').text

                if href and title and src:
                    article_dict[index] = {
                        'article_desc': article_desc,
                        'href': f'https://ek.ua{href}',
                        'title': title,
                        'img': src[8:],
                        'catalog': url_data,
                    }
            self.get_all_post(article_dict)
        except AttributeError as error:
            logger.error(f"Something went wrong: {error}")

    def clean_text(self, text):
        text = text.replace("a0", " ")
        text = text.replace("xa", "")
        text = text.replace("\xa0", " ")
        text = text.replace("\n", " ")
        text = ' '.join(text.split())
        return text

    def get_all_post(self, page_posts):
        for index in page_posts:
            response = requests.get(page_posts[index]['href'])
            soup = BeautifulSoup(response.text, 'html.parser')
            post_notice = soup.select_one(self.post_notice_nav)
            post_content = soup.select_one(self.post_content_nav)
            keywords_header = soup.select_one(self.keywords_header_nav)
            description_header = soup.select_one(self.description_header_nav)

            updated_post = {
                'keywords_header': self.clean_text(keywords_header.get('content')),
                'description_header': self.clean_text(description_header.get('content')),
                'post_notice': self.clean_text(post_notice.text),
                'post_content': self.clean_text(post_content.text),
            }
            page_posts[index].update(updated_post)
            self.added_new_post(page_posts[index])

    def added_new_post(self, page_post):
        try:
            response = requests.get(f"{self.base_url}/blogs/")
            if response.status_code == 200:
                json_data = response.json()
                existing_titles = [entry['title'] for entry in json_data]
                if page_post['title'] not in existing_titles:
                    json_post = {
                        "title": page_post['title'],
                        "keywords_header": page_post['keywords_header'],
                        "description_header": page_post['description_header'],
                        "catalog_name": page_post['catalog']['title'],
                        "short_description": page_post['article_desc'],
                        "full_description": f"{page_post['post_notice']} + {page_post['post_content']}"[:4000],
                        "image": download_image(f"https://{page_post['img']}")[11:],
                        "date_added": datetime.now().strftime("%Y-%m-%d"),
                    }
                    requests.post(f"{self.base_url}/blogs/", auth=(self.username, self.password), json=json_post)
            else:
                logger.error("The request failed:", response.status_code)
        except KeyboardInterrupt as error:
            logger.error(f"Something went wrong: {error}")


if __name__ == "__main__":
    scraper = BlogScraper()
    scraper.get_all_catalogs()