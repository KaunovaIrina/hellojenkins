import os
from flask import Flask

app = Flask(__name__)

# Получаем имя студента и порт из переменных окружения
student_name = os.getenv('STUDENT_NAME', 'Студент')
port = int(os.getenv('PORT', 5000))

@app.route('/')
def hello():
    return f'<h1>Привет, меня зовут {student_name}!</h1><p>Порт: {port}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
