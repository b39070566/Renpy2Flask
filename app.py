from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/get_title', methods=['GET'])
def get_title():
    url = request.args.get('url')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find_all("h3", itemprop="headline")[0].text
    return jsonify({'title': title})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
