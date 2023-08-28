from flask import Flask, request, jsonify
from main import Model, char_list_from_file, decoder_type

app = Flask(__name__)

# load the model
model = Model(char_list_from_file(), decoder_type, must_restore=True)

@app.route('/predict', methods=['POST'])
def predict():
    # get the image file from the request
    img_file = request.files['image']
    
    # perform inference on the image
    text = infer(model, img_file)
    
    # return the predicted text as JSON
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
