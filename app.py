from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App with Vulnerabilities!"

@app.route('/unsafe', methods=['GET'])
def unsafe_route():
    url = request.args.get('url')
    # Vulnerable to Open Redirect (if input is not sanitized)
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
