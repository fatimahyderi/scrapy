
from __future__ import unicode_literals
import json
import requests
from waitress import serve


from flask import Flask, request, Response, render_template, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def scrape():

    params = {
        'spider_name': 'coins',
        'start_requests': True,
     
    }

    response = requests.get('http://localhost:9080/crawl.json', params)
    data = json.loads(response.text)
    # result='\n'.join('<p><b>{}</b> - {}</p>'.format(item['author'], item['text'])
    #                    for item in data['items'])
    return data
    
    
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5555)