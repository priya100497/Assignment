from flask import Flask, request, jsonify
from model import model_eval_and_store

app = Flask(__name__)

@app.route('/get_model', methods=['GET'])
def generate_model():
    if request.method == "GET":
        model_data= model_eval_and_store()

        return jsonify(model_data)


if __name__=="__main__":
    app.run(debug=True)