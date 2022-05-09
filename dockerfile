FROM python:3.10
# 1я строка отвечает за image
RUN mkdir -p /usr/src/app/
# run определяет какую команду выполнить
WORKDIR /usr/src/app/
#workir - рабочая директория
COPY . /usr/src/app/

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]