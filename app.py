from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world from flask"

@app.route("/capital/<name>")
def get_capital(name):
    return f'finding country related to {name}'

if __name__=="__main__":
    app.run(debug=True)