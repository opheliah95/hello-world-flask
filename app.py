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
        result = {}
        res_json = response.json()

        # a list of country information needed
        result["country_name"] = res_json[0]["name"]["common"]
        result["capital"] = res_json[0]["capital"]
        result["flag"] = res_json[0]["flags"]["png"]
        result["lang"] = res_json[0]["languages"]

        return f'{result}'
    elif response.status_code == 400:
        return f'{url} is not found'
    else:
        return f'unknown error'
    


if __name__ == "__main__":
    app.run(debug=True)
