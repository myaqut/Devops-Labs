from flask import Flask
from datetime import datetime
import pytz
app = Flask(__name__)
@app.route('/')

def current_time():
  country_time_zone = pytz.timezone('Europe/Moscow')
  country_time = datetime.now(country_time_zone)
  result = "mosocow " + country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S")
  return result


def hello_world():

  return  current_time()


if __name__ == '__main__':
  app.run()
