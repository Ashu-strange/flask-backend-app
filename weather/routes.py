from flask import request, jsonify
from . import weather_bp
from .controller import WeatherController


@weather_bp.route('/weather', methods=['GET'])
def get_weather():
    query = request.args.to_dict(flat=False)

    if 'lat' in query.keys():
        lat = query['lat'][0]
    else:
        return jsonify({'error': 'Latitude not provided'}), 400
    if 'lon' in query.keys():
        lon = query['lon'][0]
    else:
        return jsonify({'error': 'Longitude not provided'}), 400

    weather = WeatherController.get_weather(lat, lon)

    if weather['cod'] != 200:
        return weather

    res = jsonify({'location': (
        lat, lon), 'temperature(K)': weather['main']['temp'], 'name': weather['name']})
    print(res)
    return res


@weather_bp.route('/weathers', methods=['GET'])
def show_weather():
    weathers = WeatherController.show_weather()
    print(weathers)
    res = ""
    for w in weathers:
        res += ("Location : {}{} temperature : {}C Time : {}".format(w.name,
                                                                     w.location, w.temperature-273, w.time) + "<br>")

    return res
