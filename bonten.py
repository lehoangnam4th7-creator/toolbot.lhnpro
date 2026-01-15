from flask import Flask, render_template, request, jsonify
import subprocess
import threading

app = Flask(__name__)

# Biến để kiểm tra trạng thái Bot
bot_process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_bot', methods=['POST'])
def run_bot():
    global bot_process
    if bot_process is None:
        # Chạy file bonten.py của bạn
        bot_process = subprocess.Popen(['python', 'bonten.py'], stdin=subprocess.PIPE, text=True)
        return jsonify({"status": "Bot đang khởi động..."})
    return jsonify({"status": "Bot đã chạy rồi!"})

@app.route('/send_command', methods=['POST'])
def send_cmd():
    data = request.json
    cmd_type = data.get('type')
    # Ở đây bạn có thể log lệnh hoặc xử lý điều khiển trực tiếp
    return jsonify({"status": f"Đã thực thi lệnh {cmd_type} thành công!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
