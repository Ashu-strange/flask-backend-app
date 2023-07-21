from sqlalchemy import DateTime
from .. import db


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    time = db.Column(DateTime, nullable=False)

    def show_all():
        return Weather.query.all()

    def add_wather(lat, lon, temperature, name, time):
        weather = Weather(location="({},{})".format(lat, lon),
                          temperature=temperature, name=name, time=time)
        db.session.add(weather)
        db.session.commit()

        return weather
