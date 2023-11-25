from flask import Flask, request, jsonify
from setp_read_set import *

app = Flask(__name__)


@app.route('/process_step_file', methods=['POST'])
def api_process_step_file():
    data = request.json
    file_path = data.get('file_path')

    if not file_path:
        return jsonify({"error": "No file path provided"}), 400

    try:
        result = read_step_file(file_path)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
