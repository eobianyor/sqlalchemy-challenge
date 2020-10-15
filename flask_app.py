from flask import Flask, jsonify

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
    return jsonify(Precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(Station_dict)

@app.route("/api/v1.0/tobs")
def temperatures():
    return jsonify(Temperature_dict)

@app.route("/api/v1.0/<start>")
def start():
    return "This is home. This is where the heart is"

@app.route("/api/v1.0/<start>/<end>")
def end():
    return "This is home. This is where the heart is"

if __name__=="__main__":
    app.run(debug=True)