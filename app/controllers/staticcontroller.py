from flask import send_from_directory

import os

def static_controller():
   return send_from_directory(os.path.join(os.getcwd(), 'static'), 'style.css')
