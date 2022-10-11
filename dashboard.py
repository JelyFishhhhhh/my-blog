import logging
from urllib.parse import unquote

from flask import Flask, Request, render_template, request
import json

logger = logging.getLogger("main")

class Dashboard():
    app = Flask(__name__)
    def __init__(self) -> None:
        pass

    @app.route("/", methods=["GET", "POST"])
    def root():
        return open("index.html").read()
    
    @app.route("/templates/<filename>", methods=["GET", "POST"])
    def template(filename):
        return render_template(filename)
    
    def run(self):
        with open('.\\info\\config.json', 'r', encoding='utf-8') as file:
            config = json.load(file)
    
        self.app.run(
            
            host = config['app_info']['host'], 
            port = config['app_info']['port'],
            debug = config['app_info']['debug'],  
            use_reloader = config['app_info']['use_reloader'] 
        )