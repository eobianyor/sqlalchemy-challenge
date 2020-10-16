from flask import Flask, jsonify
# %matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
from sqlalchemy import and_
import numpy as np
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurements = Base.classes.measurement
Station = Base.classes.station

Measurements.__table__.columns.values()

Station.__table__.columns.values()


# Design a query to retrieve the last 12 months of precipitation data and plot the results
session = Session(engine)
connection = engine.connect()

# Calculate the date 1 year ago from the last data point in the database
climateAnalysis = pd.read_sql('Select * from Measurement', connection, parse_dates=['date'])
finalDate = climateAnalysis.date.max()
initialDate = finalDate - timedelta(days = 365)
initialDate
finalDate

# Perform a query to retrieve the data and precipitation scores
Rain_12months = pd.read_sql("SELECT date, prcp FROM Measurement WHERE date>= '2016-08-23' AND date<= '2017-08-23'", connection, parse_dates=['date'])
connection.close()
session.close()

app = Flask(__name__)

@app.route("/")
def index():
    return (
        f"<h1>Welcome! <br/><br/></h1>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    connection = engine.connect()
    Rain_12months = pd.read_sql("SELECT date, prcp FROM Measurement WHERE date>= '2016-08-23' AND date<= '2017-08-23'", connection, parse_dates=['date'])
    # Create a dictionary for Flask
    date_List = Rain_12months.date.tolist()
    prcp_List = Rain_12months.prcp.tolist()
    Precipitation_dict = {"date": date_List, "prcp": prcp_List}
    Precipitation_dict
    connection.close()
    session.close()
    return jsonify(Precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    connection = engine.connect()
    # Design a query to show how many stations are available in this dataset?
    StationNos = pd.read_sql('SELECT id, name, station FROM Station', connection)
    # Create a dictionary for Flask
    id_List = StationNos.id.tolist()
    Station_List = StationNos.station.tolist()
    Station_name_List = StationNos.name.tolist()
    Station_dict = {"id": id_List, "station": Station_List, "station name": Station_name_List}
    connection.close()
    session.close()
    return jsonify(Station_dict)

@app.route("/api/v1.0/tobs")
def temperatures():
    session = Session(engine)
    connection = engine.connect()
    # Perform a query to retrieve the temperature data from specific station
    Temp_12months = pd.read_sql("SELECT date, tobs FROM Measurement WHERE station='USC00519281' AND date>= '2016-08-23' AND date<= '2017-08-23'", connection, parse_dates=['date'])
    # Create a dictionary for Flask
    Temp_date_List = Temp_12months.date.tolist()
    Temp_List = Temp_12months.tobs.tolist()
    Temperature_dict = {"date": Temp_date_List, "prcp": Temp_List}
    connection.close()
    session.close()
    return jsonify(Temperature_dict)

@app.route("/api/v1.0/<startdate_mm-dd>")
def startdate_mm-dd():
    return "This is home. This is where the heart is"

@app.route("/api/v1.0/<start>/<end>")
def end():
    return "This is home. This is where the heart is"

if __name__=="__main__":
    app.run(debug=True)