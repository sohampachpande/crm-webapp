from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = "\x1fw=\x8b\xa2\r\n\x1e\xea\xb0\x82$c\x04\xe8buOY\xe2\x98\xea\xe7\xda"
app.config['mongoIP'] = '127.0.0.1'
app.config['mongoPort'] = 27017

from app import routes, customerRoutes