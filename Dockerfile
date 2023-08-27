# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /mysite

# Set the working directory to /mysite
WORKDIR /mysite

# Copy the current directory contents into the container at /mysite
ADD . /mysite/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt