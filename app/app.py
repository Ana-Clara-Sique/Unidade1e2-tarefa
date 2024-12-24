from flask import Flask
from controllers.problemacontroller import problema_controller
from controllers.autorcontroller import autor_controller

app = Flask(__name__)

@app.route('/')
def index():
    return problema_controller()   


@app.route('/resultado', methods=['POST'])
def resultado():
    return problema_controller()


@app.route('/autor')
def autor():
    return autor_controller()

if __name__ == '__main__':
    app.run(debug=True)