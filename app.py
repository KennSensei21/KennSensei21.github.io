from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

def generate_image(api_key, query):
    endpoint = 'https://api.unsplash.com/photos/random'
    params = {
        'client_id': api_key,
        'query': query,
        'orientation': 'landscape'
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        image_url = response.json()['urls']['raw']
        return image_url

    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    unsplash_api_key = 'GUjY0Tv_z0L4DZ_fdgDEorKsS1vteOQ3G71XvnJ4B5s'
    query = request.form['query']
    image_url = generate_image(unsplash_api_key, query)
    return render_template('result.html', image_url=image_url)

if __name__ == '__main__':
    app.run()
