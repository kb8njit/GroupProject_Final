FROM python:3.8

EXPOSE 5000

WORKDIR /calendar_app

COPY requirements.txt /calendar_app
RUN pip install  -r requirements.txt --upgrade pip

COPY . /calendar_app

CMD python app.py