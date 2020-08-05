FROM python:3.8

EXPOSE 5000

WORKDIR /LoginApp

COPY requirements.txt /LoginApp
RUN pip install  -r requirements.txt --upgrade pip

COPY . /LoginApp

CMD python app.py