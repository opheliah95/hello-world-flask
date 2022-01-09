from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello world from flask"


@app.route("/capital/<name>")
def get_capital(name):
    url = f'https://restcountries.com/v3.1/capital/{name}'
    response = requests.get(url)

    if response.status_code == 200:
        print(f'data found for url: {url}')
        res_json = response.json()
        return f'{res_json}'
    elif response.status_code == 400:
        return f'{url} is not found'
    else:
        return f'unknown error'
    


if __name__ == "__main__":
    app.run(debug=True)
