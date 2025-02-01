from flask import Flask, request, jsonify
from rembg import remove
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'image_file' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image_file']
    
    # Read the image as bytes
    image_bytes = image_file.read()

    # Remove the background
    result = remove(image_bytes)

    # Return the processed image as a response
    return (result, 200, {
        'Content-Type': 'image/png',
        'Content-Disposition': 'attachment; filename=output.png'
    })

if __name__ == '__main__':
    app.run(debug=True)
