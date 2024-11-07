from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.users import Users

# Models
from models.users_model import UserModel

main = Blueprint("users_blueprint", __name__)


@main.route("/")
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/<id>")
def get_user_by_id(id):
    try:
        user = UserModel.get_user_id(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/add", methods=["POST"])
def add_user():
    try:
        nombre = request.json["nombre"]
        email = request.json["email"]
        id = uuid.uuid4()
        user = Users(str(id), nombre, email)

        affected_rows = UserModel.add_user(user)
        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/delete/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = Users(id)

        affected_rows = UserModel.delete_user(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({"message": "No user delete"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@main.route("/update/<id>", methods=["PUT"])
def update_user(id):
    try:
        nombre = request.json["nombre"]
        email = request.json["email"]
        user = Users(id, nombre, email)

        affected_rows = UserModel.update_user(user)
        
        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({"message": "Error on update"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
