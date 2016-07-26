# encoding:utf-8
'''
MindWiki
A webset of wiki use mindmap.

Author: zYeoman(zhuangyw.thu#gmail.com)
Last Edit: 2016-07-27
'''
import os
from flask import (Flask, render_template, request)
from flask_script import Manager


APP = Flask(__name__)
APP.config['CONTENT_DIR'] = 'notes'
APP.config['TITLE'] = 'wiki'
APP.secret_key = 'sdklafj'
try:
    APP.config.from_pyfile('config.py')
except IOError:
    print ("Startup Failure: You need to place a "
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
    path = os.path.join(APP.config['CONTENT_DIR'],
                        url + '.md')
    if os.path.exists(path):
        with open(path, 'rU') as file_read:
            content = file_read.read().decode('utf-8')
    else:
        content = u'# ' + url.decode('utf-8')
    if request.method == 'POST':
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(path, 'w') as file_write:
            file_write.write(request.form.get('body').replace('\r\n', '\n').encode('utf-8'))


    if request.args.get('nofmt'):
        return content
    return render_template('page.html')

if __name__ == '__main__':
    MANAGER = Manager(APP)
    MANAGER.run()
