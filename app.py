from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

def get_dad_joke():
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Dad Jokes Web App (https://github.com/yous92/dad-jokes)'
    }
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    if response.status_code == 200:
        return response.json()['joke']
    return 'Why did the dad app fail? Because it couldn\'t fetch a joke! 😅'

@app.route('/')
def home():
    joke = get_dad_joke()
    return render_template('index.html', joke=joke)

@app.route('/api/joke')
def get_joke():
    return {'joke': get_dad_joke()}

if __name__ == '__main__':
    app.run(debug=True)