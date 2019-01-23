from flask import Flask
from req import get_weather
from datetime import datetime

app = Flask(__name__)

city_id = '706369'
apikey = '300dd55367b503694f6bfa3ca8bfe0ec'


@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric'.format(city_id, apikey)
    weather = get_weather(url)
    current_date = datetime.now().strftime('%d.%m.%Y %H:%M')
    result = '<p><b>Today:</b> {}</p>'.format(current_date)
    result += '<p><b>City:</b> {}</p>'.format(weather['name'])
    result += '<p><b>Temperature:</b> {}</p>'.format(weather['main']['temp'])
    return result


@app.route('/test')
def test():
    return 'This is a TEST!'

if __name__ == '__main__':
    app.run()