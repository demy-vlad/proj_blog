# validators.py

from fastapi import HTTPException
from datetime import date

def validate_blog_data(title: str, keywords_header: str, description_header: str, catalog_name: str, short_description: str, full_description: str, date_added: str):
    # Проверка наличия всех обязательных полей
    if not all([title, keywords_header, description_header, catalog_name, short_description, full_description, date_added]):
        raise HTTPException(status_code=400, detail="All fields are required")
    
    # Проверка типов данных и ограничений на количество символов для каждого поля
    if not isinstance(title, str) or len(title) > 200:
        raise HTTPException(status_code=400, detail="Title must be a string with max length 200")
    
    if not isinstance(keywords_header, str) or len(keywords_header) > 300:
        raise HTTPException(status_code=400, detail="Keywords header must be a string with max length 300")
    
    if not isinstance(description_header, str) or len(description_header) > 300:
        raise HTTPException(status_code=400, detail="Description header must be a string with max length 300")
    
    if not isinstance(catalog_name, str) or len(catalog_name) > 100:
        raise HTTPException(status_code=400, detail="Catalog name must be a string with max length 100")
    
    if not isinstance(short_description, str) or len(short_description) > 400:
        raise HTTPException(status_code=400, detail="Short description must be a string with max length 400")
    
    if not isinstance(full_description, str) or len(full_description) > 400:
        raise HTTPException(status_code=400, detail="Full description must be a string with max length 400")
