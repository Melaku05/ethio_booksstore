FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /book_store
COPY requirements.txt /book_store/
RUN pip install -r requirements.txt
COPY . /book_store/