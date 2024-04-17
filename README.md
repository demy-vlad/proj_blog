# Blog Web Application
## Peculiarities
- 


## Installation and launch
1. Clone the repository
2. Change to the project directory: ```cd comments```
3. Create and activate virtual environment: ```python3 -m venv venv``` и ```source venv/bin/activate``` (or ```venv\Scripts\activate``` on Windows)
4. Install dependencies: ```pip install -r requirements.txt```
5. Apply migrations: ```python manage.py migrate```
6. Start local server: ```python manage.py runserver```

## Installing with docker
1. ```docker-compose build --no-cache```
2. ```docker-compose up --detach```


## Running Tests
- You must have dependencies installed!
1. Running tests: ```pytest -s -v```
