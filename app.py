from dotenv import load_dotenv
import os
from flask import Flask
from controllers.usuario_controller import usuario_bp

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(usuario_bp)

if __name__ == "__main__":
    app.run(debug=True)