from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def homepage():
    params = {
        'api_key'='{API_KEY}',
        }
    r = requests.get('http://api.icndb.com/jokes/random/')
return render_template('chucknorrisjokes.html', jokes=json.loads(r.text)['jokes'])
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
