# build and image starting with pythom 3.8 which is the version needed for our app
FROM python:3.8-slim-buster
# set the working directory
WORKDIR /code
#set the variable used by flask command
ENV FLASK_APP=flaskapp.py
ENV FLASK_RUN_HOST=0.0.0.0
#copy and install the depndeincies in the file requirments.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#set the port for the container to be 5000
EXPOSE 5000
#copy the current files to the file 
COPY . .
#set the default command for the container to flask run 
CMD ["flask", "run"]
