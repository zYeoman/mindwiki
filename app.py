# encoding:utf-8
'''
MindWiki
A webset of wiki use mindmap.

Author: zYeoman(zhuangyw.thu#gmail.com)
Create: 2016-07-16
Modify: 2017-02-07
Version: 0.1.3
'''
import os
from flask import (Flask, render_template, request)
from flask_script import Manager

import convert

APP = Flask(__name__)
APP.config['CONTENT_DIR'] = 'notes'
APP.config['TITLE'] = 'wiki'
APP.secret_key = 'sdklafj'
try:
    APP.config.from_pyfile('config.py')
except IOError:
    print("Startup Failure: You need to place a "
          "config.py in your root directory.")


@APP.route('/', methods=['GET', 'POST'])
def home():
    '''
    Root of mindwiki.
    '''
    return display('home')


@APP.route('/<path:url>', methods=['GET', 'POST'])
def display(url):
    '''
    Page of mindwiki, auto generate.
    '''
    filename = url.strip('/').split('/')[-1]
    path = os.path.join(APP.config['CONTENT_DIR'],
                        url.strip('/') + '.md')
    if os.path.exists(path):
        with open(path, 'rb') as file_read:
            content = file_read.read().decode('utf-8')
    else:
        content = u'# ' + filename
    if request.method == 'POST':
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(path, 'wb') as file_write:
            markdown = convert.km2md(request.form.get('body')).encode('utf-8')
            file_write.write(markdown)

    if request.args.get('nofmt'):
        return convert.md2km(content)
    return render_template('page.html')


if __name__ == '__main__':
    MANAGER = Manager(APP)
    MANAGER.run()
