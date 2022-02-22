FROM python:3

WORKDIR /code

#prevent python from creating pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install pip --upgrade pip

COPY ./TODOList/requirements.txt /code/
RUN pip install pip --upgrade
RUN pip install --upgrade --no-cache-dir --src /usr/src -r requirements.txt
COPY ./TODOList /code/
