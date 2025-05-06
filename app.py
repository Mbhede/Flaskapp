from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# A list of quotes to serve
quotes = [
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "If you want to live a happy life, tie it to a goal, not to people or things. - Albert Einstein"
    "The hardest choices require the strongest wills. - Thanos"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote")
def quote():
    return jsonify({
        "quote": random.choice(quotes)
    })

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
