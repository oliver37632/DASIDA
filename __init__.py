from app import create_app
from config import secret

if __name__ == "__main__":
    app = create_app()
    app.config['SECRET_KEY'] = secret
    app.run(host="0.0.0.0", debug=True)