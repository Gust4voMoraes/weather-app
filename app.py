from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def weather():
    city = request.args.get('city')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c32cd803940fee998e5be7a343aa5a4b&units=metric'
    r = requests.get(url.format(city)).json
    response = requests.get(url)
    data = response.json()
    weather_info = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon'],
        'humidity': data['main']['humidity'],
    }
    return render_template('index.html', weather_info=weather_info)

if __name__ == '__main__':
    app.run(debug=True)