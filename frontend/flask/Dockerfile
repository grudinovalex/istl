# init a base image
FROM fedora:latest

# update pip to minimize dependency errors 
RUN yum -y update 
RUN yum -y upgrade
RUN yum -y install python pip
RUN pip install --upgrade pip

# define the present working directory
WORKDIR /flask

# copy the contents into the working dir
ADD . /flask
COPY app app

# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt

EXPOSE 5000

# define the command to start the container
CMD ["python","run.py"]
