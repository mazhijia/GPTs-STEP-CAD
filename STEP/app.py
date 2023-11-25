from flask import Flask, request, jsonify
from setp_read_set import *
import os 
from werkzeug.utils import secure_filename

app = Flask(__name__)

STEP_FILES_DIR = os.environ.get('STEP_FILES_PATH', '/app/step_files')

@app.route('/process_step_file', methods=['POST'])
def api_process_step_file():
    # 解析 JSON 请求获取文件 URL
    data = request.json
    file_url = data.get('file_url')

    if not file_url:
        return jsonify({"error": "No file URL provided"}), 400

    try:
        # 下载文件
        response = requests.get(file_url, stream=True)
        response.raise_for_status()

        # 为下载的文件创建一个安全的文件名
        filename = secure_filename(file_url.split('/')[-1])
        temp_file_path = os.path.join(STEP_FILES_DIR, filename)  # 这里使用变量而不是字符串

        with open(temp_file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        # 调用处理函数
        result = read_step_file(temp_file_path)

        # 可选：处理完后删除文件
        os.remove(temp_file_path)

        return jsonify({"success": True, "data": result}), 200
    except Exception as e:
        # 可选：发生异常时也删除文件
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
