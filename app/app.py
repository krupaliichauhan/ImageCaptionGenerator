from flask import Flask, render_template, request
from PIL import Image
import numpy as np

app = Flask(__name__)

def generate_caption(image):
    # Dummy function (replace with your model)
    return "A sample generated caption for the uploaded image."

@app.route('/', methods=['GET', 'POST'])
def index():
    caption = None
    if request.method == 'POST':
        file = request.files['image']
        image = Image.open(file.stream)
        caption = generate_caption(image)
    return render_template('index.html', caption=caption)

if __name__ == '__main__':
    app.run(debug=True)