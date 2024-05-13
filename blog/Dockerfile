# Используем более легковесный базовый образ
FROM python:3.9.14-alpine

RUN sudo apt-get update
# Устанавливаем необходимые зависимости
RUN apk add --no-cache libpq

# Устанавливаем часовой пояс Украины (Europe/Kiev)
RUN apk add --no-cache tzdata
ENV TZ=Europe/Kiev

# Копируем файлы зависимостей Python и устанавливаем их
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysqlclient

# Копируем исходный код Django в контейнер
COPY . /app/

# Выполняем миграции
# RUN python manage.py makemigrations
RUN python manage.py migrate

# Экспозим порт Django
EXPOSE 8000

# Запускаем Django сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]