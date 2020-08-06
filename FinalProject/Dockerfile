FROM python:3.8

EXPOSE 5000

WORKDIR /FinalProject

COPY requirements.txt /FinalProject
RUN pip install  -r requirements.txt --upgrade pip

COPY . /FinalProject

CMD python app.py