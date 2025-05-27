Приложения по выдаче прогноза погоды на три дня  
  
1.git clone https://github.com/virus37161/Whether.git  
  
2.создайте файл .env.dev в директории apps  
SECRET_KEY='секретный ключ джанго'  
ALLOWED_HOSTS=localhost 127.0.0.1  
CSRF_TRUSTED_ORIGINS=http://localhost:8001  
POSTGRES_USER=django  
POSTGRES_PASSWORD=password  
POSTGRES_DB=apps  
POSTGRES_PORT=5432  
  
3.Запускаем приложение docker compose up  
Переходим по адресу http://localhost:8001/whether 
  
Вы можете зарегистрироваться  
  
Чтобы создать админа, необходимо в контейнере apss-1 создать  
пользователя admin (python manage.py createsuperuser)
