import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Перехватываем IP через прокси-заголовок хостинга
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if user_ip:
        # Если за несколькими прокси, берем самый первый (клиентский) IP
        user_ip = user_ip.split(',')[0].strip()

    print(f"\n==========================================")
    print(f"[!] НОВЫЙ ПОСЕТИТЕЛЬ! IP-адрес: {user_ip}")
    print(f"==========================================\n", flush=True)

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)