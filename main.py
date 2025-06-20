from flask import Flask, request, jsonify
from services.functions import edit_user
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)

@app.route('/update-user', methods=['PATCH'])
def update_user():
    
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Token missing or invalid"}), 401

    token = auth_header.replace("Bearer ", "")
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        Id_User = decoded.get("user_id")
        if not Id_User:
            return jsonify({"error": "Invalid token data"}), 401
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    data = request.get_json()
    Name = data.get("Name")
    Lastname = data.get("Lastname")
    Password = data.get("Password")

    response, code = edit_user(Id_User, Name, Lastname, Password)
    return jsonify(response), code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
