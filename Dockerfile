FROM python:3

ENV PYTHONBUFFER=1

WORKDIR /root/chat_info_bot/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]
