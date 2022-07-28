# set base image (host OS)
FROM python:latest

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY monit2postgres.py /code/

# configs volume to hold yaml files
VOLUME [ "/configs" ]

# set the working directory in the container
WORKDIR /code

# command to run on container start
CMD [ "python3", "monit2postgres.py" ]