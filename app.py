from flask import Flask, render_template, request
import requests
from requirements import API_KEY

app = Flask(__name__)

@app.route("/")
def index() -> None:
    return render_template('index.html')

@app.route("/weather")
def weather() -> None:
        
    city = request.args.get('city')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
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