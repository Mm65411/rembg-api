from flask import Flask, request, send_file, jsonify
from rembg import remove
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    try:
        # Ensure the file is part of the request
        if 'image_file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['image_file']
        
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        # Read the image file and remove the background
        img_data = file.read()
        output = remove(img_data)

        # Convert the result to an image
        img = BytesIO(output)
        return send_file(img, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
