from flask import Flask
from datetime import datetime
import pytz
app = Flask(__name__)
@app.route('/')

def current_time():
  #get timezone 
  country_time_zone = pytz.timezone('Europe/Moscow')
  #get the time and date using the timezone
  country_time = datetime.now(country_time_zone)
  #preparing the text to send to as a result
  result = "mosocow " + country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S")
  return result


def hello_world():

  return  current_time()


if __name__ == '__main__':
  app.run()
