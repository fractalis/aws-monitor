from flask import Flask, render_template
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_assets import Environment, Bundle

import boto3
import json

app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='aws-monitor', template_mode='bootstrap3')
assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle('scss/main.scss', filters='pyscss', output='main.css')
assets.register('scss_all', scss)

Bootstrap(app)


@app.route('/')
def hello():
    ec2 = boto3.client('ec2')

    instances = ec2.describe_instances()

    return render_template('index.html', instances=instances)
