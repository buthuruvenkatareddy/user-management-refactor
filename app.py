from flask import Flask
from routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes)

@app.route('/')
def home():
    return "User Management System is Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
