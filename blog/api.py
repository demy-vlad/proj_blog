from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from validators import validate_blog_data
from main.models import Blog, CatalogOfArticles

app = FastAPI()

# Pydantic модель для Catalog
class CatalogOfArticlesResponse(BaseModel):
    id: int
    title: str
    url_catalog: str
    
# Pydantic модель для Blog
class BlogResponse(BaseModel):
    id: int
    title: str
    keywords_header: str
    description_header: str
    catalog_name: str
    short_description: str
    full_description: str
    image: str
    date_added: date
    
# Pydantic модель для создания нового блога
class BlogCreate(BaseModel):
    title: str
    keywords_header: str
    description_header: str
    catalog_name: str
    short_description: str
    full_description: str
    image: Optional[str] = "default.jpg"
    date_added: date

# Класс для хранения пользователей (заглушка)
class Users:
    users = {"admin": "admin"}
    
# Инициализируем экземпляр HTTPBasic для аутентификации
security = HTTPBasic()

# Функция для проверки учетных данных пользователя
def check_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    # Получаем переданные учетные данные
    username = credentials.username
    password = credentials.password
    
    # Проверяем, есть ли такой пользователь и совпадает ли пароль
    if username not in Users.users or Users.users[username] != password:
        # Если нет, вызываем исключение HTTP 401 Unauthorized
        raise HTTPException(
            status_code=401,
            detail="Incorrect user or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    # Возвращаем имя пользователя, чтобы можно было его использовать в обработчике
    return username

# Роут для получения всех блогов
@app.get("/blogs/", response_model=List[BlogResponse])
def get_all_blogs():
    try:
        # Получение всех объектов Blog из базы данных
        blogs = Blog.objects.all()
        # Преобразование объектов Django в объекты Pydantic
        blogs_response = []
        for blog in blogs:
            # Получение URL изображения, если доступен
            image_url = blog.image.url if hasattr(blog.image, 'url') else str(blog.image)
            blogs_response.append(BlogResponse(
                id=blog.id,
                title=blog.title,
                keywords_header=blog.keywords_header,
                description_header=blog.description_header,
                catalog_name=blog.catalog_name,
                short_description=blog.short_description,
                full_description=blog.full_description,
                image=image_url,  # Передача URL изображения
                date_added=blog.date_added
            ))
        return blogs_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Роут для создания нового блога
@app.post("/blogs/", response_model=BlogResponse)
def create_blog(blog_data: BlogCreate, username: str = Depends(check_credentials)):
    try:
        validate_blog_data(blog_data.title, blog_data.keywords_header, blog_data.description_header, blog_data.catalog_name, blog_data.short_description, blog_data.full_description, blog_data.date_added)
        
        # Создание нового объекта Blog
        new_blog = Blog.objects.create(
            title=blog_data.title,
            keywords_header=blog_data.keywords_header,
            description_header=blog_data.description_header,
            catalog_name=blog_data.catalog_name,
            short_description=blog_data.short_description,
            full_description=blog_data.full_description,
            image=blog_data.image,
            date_added=blog_data.date_added
        )
        # Преобразование созданного блога в Pydantic модель и возвращение
        created_blog = BlogResponse(
            id=new_blog.id,
            title=new_blog.title,
            keywords_header=new_blog.keywords_header,
            description_header=new_blog.description_header,
            catalog_name=new_blog.catalog_name,
            short_description=new_blog.short_description,
            full_description=new_blog.full_description,
            image=new_blog.image.url if hasattr(new_blog.image, 'url') else str(new_blog.image),
            date_added=new_blog.date_added
        )
        return created_blog
    except (Exception, KeyboardInterrupt) as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/catalogs/", response_model=List[CatalogOfArticlesResponse])
def get_all_catalog(username: str = Depends(check_credentials)):
    try:
        return CatalogOfArticles.objects.all()
    except (Exception, KeyboardInterrupt) as e:
        raise HTTPException(status_code=500, detail=str(e))