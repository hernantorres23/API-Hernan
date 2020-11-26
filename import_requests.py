from flask import Flask, jsonify
from requests import request
import json


app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Estoy en el Home"


# @app.route("/movies/<string:titulo>", methods=["GET"])
# def show_results(titulo):
#     url = "https://itunes.apple.com/search"
#     querystring = {
#         "term": titulo,
#         "entity": ["movie,tvSeason", "tvEpisode"],
#         "limit": "200",
#     }
#     response = request("GET", url, params=querystring)
#     return response
#     print(type(response))

url = "https://itunes.apple.com/search"

querystring = {"term":"thrones","entity":["movie,tvSeason","tvEpisode"],"limit":"200"}

payload = ""
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = request("GET", url, data=payload, headers=headers, params=querystring)

print(json.dumps(response.text))

if __name__ == "__main__":
    app.run(debug=True, port="5300")
