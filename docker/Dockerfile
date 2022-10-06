# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./docker/requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user -r requirements.txt

CMD ["app.py"]