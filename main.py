from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    load_dotenv()
    app.run(port=os.getenv("PORT", default=5000), host=os.getenv("HOST"))
    #serve(app, host=os.getenv("HOST", default='127.0.0.1'), port=os.getenv("PORT", default=5000))

