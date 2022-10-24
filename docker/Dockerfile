# start by pulling the python image
FROM python:3.8-alpine
# copy the requirements file into the image
COPY ./docker/requirements.txt /app/requirements.txt
# switch working directory
WORKDIR /app
# update pip
RUN /usr/local/bin/python -m pip install --upgrade pip
# install dependancies
RUN apk add --no-cache libressl-dev musl-dev libffi-dev build-base
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
CMD ["api/app.py"]