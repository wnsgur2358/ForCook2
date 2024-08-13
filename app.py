# app.py
from flask import Flask, render_template, request
from data import food_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    food_info = None
    if request.method == 'POST':
        food_name = request.form.get('food_name')
        if food_name in food_data:
            food_info = food_data[food_name]
        else:
            food_info = None
    return render_template('index.html', food_info=food_info)

if __name__ == '__main__':
    app.run(debug=True)
