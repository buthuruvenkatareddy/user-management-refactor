from flask import jsonify
from models.db import cursor, conn
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_users_controller():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users), 200

def get_user_by_id_controller(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

def create_user_controller(data):
    name = data['name']
    email = data['email']
    password = generate_password_hash(data['password'])

    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()
    return jsonify({'message': 'User created successfully'}), 201

def update_user_controller(user_id, data):
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({'error': 'Name and Email are required'}), 400

    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()
    return jsonify({'message': 'User updated'}), 200

def delete_user_controller(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    return jsonify({'message': f'User {user_id} deleted'}), 200

def search_users_controller(name):
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    users = cursor.fetchall()
    return jsonify(users), 200

def login_controller(data):
    email = data['email']
    password = data['password']
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if user and check_password_hash(user[3], password):
        return jsonify({'status': 'success', 'user_id': user[0]}), 200
    return jsonify({'status': 'failed'}), 401
