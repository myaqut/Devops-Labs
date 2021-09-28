# Lab1
![example workflow](https://github.com/myaqut/devops/actions/workflows/main.yml/badge.svg)

**Table of Contents**

1. About Lab .
2. Getting Started :
	- Prequestes. 
	- Installation. 
3.  Add the time function to your app.
4. Unit testing. 

## About Lab:
This lab is mainly creating web application using python and deploy it on AWS instance. The application function is to show the current time and date in Moscow. You can view the live application throught the following link: [ec2-18-117-114-7.us-east-2.compute.amazonaws.com](http://ec2-18-117-114-7.us-east-2.compute.amazonaws.com "ec2-18-117-114-7.us-east-2.compute.amazonaws.com") .

## Getting Started: 
### Prequestes :
This setion is for preparing the required enviroment and libraries in order to get started.
1. Starting up an EC2 instance:
	- create an AWS account if you don't have it already.
	- Open AWS EC2 Console from https://console.aws.amazon.com/ec2/
	- Launch Intance
	- Choose AMI and find Ubuntu Server.
	- Configure the instance : 
		- On security group settings , add http on port 80 and allow all IP addresses . [![inbound security](https://miro.medium.com/max/1050/0*GfxWzIlIf9HzXzEO "inbound security")](https://miro.medium.com/max/1050/0*GfxWzIlIf9HzXzEOhttp:// "inbound security")
		- Make sure to download your pair key, and follow the following [steps](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html "steps") in order to establish ssh connection using linux.
		- You can also connect using EC2 [interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html "interface") .  
[Links](http://localhost/)
2. Installing dependencies :
	- Install python and flask.
`sudo apt-get install python3`
`sudo apt-get install python3-pip `
` sudo pip install flask`
	- Create Directory for your app.
`cd ~`
`mkdir ~/flaskapp`
`sudo ln -sT ~/flaskapp /var/www/html/flaskapp`
	- Verify your app is running .
	`cd ~/flaskapp `
	`echo "Hola" > index.html`
	- You should see hola displayed on your screen when you enter your instance public IP/index.
	- Add the following module in order to use it for the time function in your app.
`sudo pip install pytz`
`sudo pip install datetime`

## Installation :
1- Create flasskapp.py file inside your app folder created previously and add the following.

```python
from flask import Flask app = Flask(__name__)
@app.route('/') 
def hello_world():
   return 'Hello from Flask!' 
if __name__ == '__main__':
   app.run()
```
2- Create flaskpp.wsgi file in order to load your appplication and add the following code.

```python
#flaskapp.wsgi
import sys 
sys.path.insert(0, '/var/www/html/flaskapp')
  
from flaskapp import app as application

```
3- Enable mod_wsgi:

-  We need to replace the default html pages of appaches with your application, in order to do that we should do few changes to appache configuration file located in**  /etc/apache2/sites-enabled/000-default.conf**.

-  Add the following to the file after **DocumentRoot** line.
	
```html
WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi  
<Directory flaskapp>
     WSGIProcessGroup flaskapp
     WSGIApplicationGroup %{GLOBAL}
     Order deny,allow
     Allow from all 
</Directory>
```
4- Restart your server. 
`$ sudo service apache2 restart`

5- In case your server gave internal error please run the following in order to force wsgi to run the app using python 3, and then restart your server.
`sudo apt-get install libapache2-mod-wsgi-py3`

## Add the time function to your app
You can add the time function to your app by simply replacing your flaskapp.py file with the file already pre made in the rebo.

## Test that the time is refreshing using unittesting
We need to make sure that everytime we get the time it's different than the previous one. This why the time is actually updating and refreshing each time you refresh the application. Follow the next steps in order to establish  a test. 
1. Add the file named unitest.py in your app folder.
2. Install unitest module.
`sudo apt-get install -y python-unittest2`
2. Run unitest.py using python3.

# Deploying Flask App Using Docker


### Table of Content

1-  Overview

2- Getting Started
- Prerequisites
- Steps


## Overview

This Repo presents the steps needed in order to deploy Flask application using Docker. Using Docker you won't need to add the dependencies on your machine or do any configuration. Everything is automated and isolated from the rest of your machine. Docker runs as a separate process on your machine.

## Getting Started

### Prerequisites : 
The only two prerequisites is to install docker engine and composer on your machine. Please follw the next steps according to your OS.
##### Docker Enginge : 
- For windows users:  click [here](https://docs.docker.com/desktop/windows/install/ "here")
- For linux users : click [here](https://docs.docker.com/engine/install/ubuntu/ "here").

##### Docker Composer :
you can find the required steps for both linux and windows on the following [link](https://docs.docker.com/compose/install/ "link"). 

##### Docker Linter:
For this repo I used vscode and installed docker extenstion as [Linter](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker "Linter") for formatting.

### Getting Started : 

1- Create new folder and add your flaskapp.py file inside that folder. 
2- Create new file inside the same folder called requirements.txt in order to add the modules and dependencies required for the application.

    flask
    pytz
    datetime
3- Create docker file named Dockerfile and add the following conent. 

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
    
4- Add docker-compose.yml file in order to define the running services for the container.

    version: "3.9"
    services:
      web:
        build: .
        ports:
          - "5000:5000"
      redis:
        image: "redis:alpine"

5- Build your app using compose 
` docker-compose up`

6- Open your browser and type http://localhost:5000/. You should see the time of moscow displayed on your browser screen.
