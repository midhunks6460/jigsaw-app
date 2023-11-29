from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Example puzzle pieces
puzzle_pieces = [
    {"id": 1, "image": "piece1.jpg"},
    {"id": 2, "image": "piece2.jpg"},
    {"id": 3, "image": "piece3.jpg"},
    # Add more pieces as needed
]

# Shuffle the pieces randomly
random.shuffle(puzzle_pieces)

@app.route('/')
def index():
    return render_template('index.html', puzzle_pieces=puzzle_pieces)

@app.route('/shuffle')
def shuffle_pieces():
    global puzzle_pieces
    random.shuffle(puzzle_pieces)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
