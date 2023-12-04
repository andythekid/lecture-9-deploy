# Курс **Технологии разработки интернет-приложений**. 2 семестр
## Лекция 9: Развертывание на production

### Запуск

Клонируем репозиторий
```
git clone https://github.com/andythekid/lecture-9-deploy.git
cd lecture-9-deploy
```

Создаем виртуальное окружение:
```
python -m venv venv
```
Запускаем его н linux и Mac OS:
```
source venv/bin/activate
```
или на Windows
```
.\venv\bin\activate.bat
```
Устанавливаем пакеты:
```
pip install -r requirements.txt
```
Запускаем сервер:
```
cd templatesTest
python manage.py runserver

```
