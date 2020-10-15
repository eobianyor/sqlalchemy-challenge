from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return"This is home. This is where the heart is"

@app.route("/about")
def about():
    return"That's not what this is about"

@app.route("/contact")
def contact():
    return"3 2 1 contact"

if __name__=="__main__":
    app.run(debug=True)