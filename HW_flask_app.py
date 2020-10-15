# 1. Import Flask
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

# Create our session (link) from Python to the DB
session = Session(engine)

# Perform a query to retrieve the data and precipitation scores
Rain_12months = session.query(Measurements.date, Measurements.prcp).filter(and_(Measurements.date>='2016-08-23', Measurements.date <= '2017-08-23'))
print(Rain_12months)



# # Save the query results as a Pandas DataFrame and set the index to the date column
# Rain_12months_df = pd.DataFrame(Rain_12months)
# Rain_12months_df.head()

# # Sort the dataframe by date
# Rain_12months_df = Rain_12months_df.sort_values(by='date', ascending=False)
# Rain_12months_df.groupby('date').sum()
# # Rain_12months_df.set_index('date', inplace=True)
# Rain_12months_df.head()



# # 2. Create an app
# app = Flask(__name__)


# # 3. Define static routes
# @app.route("/api/v1.0/precipitation")
# @app.route("/api/v1.0/stations")
# @app.route("/api/v1.0/tobs")



# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     return "Hello, world!"


# @app.route("/about")
# def about():
#     name = "Chris"
#     city = "The Woodlands"

#     return f"My name is {name}, and I currently live in {city}."


# @app.route("/contact")
# def contact():
#     email = "Chris@domain.com"

#     return f"Questions? Comments? Complaints? Shoot an email to {email}."


# # 4. Define main behavior
# if __name__ == "__main__":
#     app.run(debug=True)
