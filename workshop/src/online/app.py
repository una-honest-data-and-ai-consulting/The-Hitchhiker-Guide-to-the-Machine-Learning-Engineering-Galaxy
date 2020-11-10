import logging

from flask import Flask, request

app = Flask(__name__)

model = None

@app.before_serving
def load_model():
    global model
    model = OnlineModel.load(path)


@app.route('/predict', methods=['POST'])
def predict():
    global model
    raw_data = request.get_json()
    prediction = model.predict(raw_data)
    output = {'input': raw_data, 'prediction': prediction}
    return output

if __name__ == '__main__':
    app.run(host, port, debug=False)