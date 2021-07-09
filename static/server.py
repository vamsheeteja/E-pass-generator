from flask import Flask
from flask import render_template
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello dear'
# if __name__ == "__main__":
#     app.run()

@app.route('/')
def index():
    return render_template('index.html', title = 'Flask', username = 'Vamshee')
if __name__ == "__main__":
    app.run()



