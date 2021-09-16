# Lab1

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

