from flask import Flask, request
from wa import wa
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = wa(request.json)
        return bot.processing()

if(__name__) == '__main__':
    app.run(debug=True)
