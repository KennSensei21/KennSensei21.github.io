from flask import Flask, render_template, request, Response
import requests
import random
import base64

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

        image_data = requests.get(image_url).content
        return image_data

    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        unsplash_api_key = 'GUjY0Tv_z0L4DZ_fdgDEorKsS1vteOQ3G71XvnJ4B5s'
        query = request.form['query']

        image_data = generate_image(unsplash_api_key, query)

        if image_data:
            image_data = base64.b64encode(image_data).decode('utf-8')
            return render_template('index.html', image_data=image_data)
        else:
            return 'Failed to generate the image.'
    else:
        return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image_route():
    unsplash_api_key = 'GUjY0Tv_z0L4DZ_fdgDEorKsS1vteOQ3G71XvnJ4B5s'
    query = request.form['query']

    image_data = generate_image(unsplash_api_key, query)

    if image_data:
        return Response(image_data, mimetype='image/jpeg')
    else:
        return 'Failed to generate the image.'

if __name__ == '__main__':
    app.run()
