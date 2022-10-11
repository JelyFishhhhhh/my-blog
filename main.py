from flask import Flask, render_template
import json
from datetime import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def origin():
    return open('index.html').read()

@app.route('/templates/<filename>', methods=['GET', 'POST'])
def template(filename):
    return render_template(filename)

if __name__ == '__main__':
    
    with open('.\\info\\config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    
    app.run(
        
        host = config['app_info']['host'], 
        port = config['app_info']['port'],
        debug = config['app_info']['debug'],  
        use_reloader = config['app_info']['use_reloader'] 
    )