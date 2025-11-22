import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import mysql.connector
from ddtrace import patch_all, tracer
import sys

patch_all()

# =====================================================
#   FLASK + CORS
# =====================================================
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# =====================================================
#   LOGGING SETUP
# =====================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("backend")
logger.setLevel(logging.INFO)

# Console logging
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(console_handler)

# File logging (rotating)
file_handler = RotatingFileHandler("app.log", maxBytes=2*1024*1024, backupCount=3)
file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(file_handler)

# =====================================================
#   DATABASE CONNECTION
# =====================================================
def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="mydatabase"
        )
        logger.info("DB connection established successfully")
        return conn
    except mysql.connector.Error as err:
        logger.error(f"DB connection failed: {err}")
        raise


# =====================================================
#   ROUTES
# =====================================================


@app.route("/")
def home():
    return render_template("index.html")

# ----- TEST ROUTE -----
@app.route("/test")
def test():
    return "TEST OK", 200

# ----- ADD USER -----
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    logger.info(f"POST /users called with: {data}")

    if "name" not in data or "email" not in data:
        return jsonify({"error": "name and email are required"}), 400

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (data["name"], data["email"])
        )
        conn.commit()
        logger.info("User added successfully")
        return jsonify({"message": "User added"}), 201

    except Exception as e:
        logger.error(f"Error adding user: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ----- UPDATE USER -----
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    logger.info(f"PUT /users/{user_id} called with: {data}")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET name=%s, email=%s WHERE id=%s",
            (data["name"], data["email"], user_id)
        )
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404

        logger.info("User updated successfully")
        return jsonify({"message": "User updated"}), 200

    except Exception as e:
        logger.error(f"Error updating user: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ----- DELETE USER -----
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    logger.info(f"DELETE /users/{user_id} called")

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404

        logger.info("User deleted successfully")
        return jsonify({"message": "User deleted"}), 200

    except Exception as e:
        logger.error(f"Error deleting user: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# ----- GET ALL USERS -----
@app.route("/users", methods=["GET"])
def get_users():
    logger.info("GET /users called")
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        logger.info(f"Fetched {len(users)} users")
        return jsonify(users), 200

    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        return jsonify({"error": str(e)}), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# =====================================================
#   START SERVER
# =====================================================
if __name__ == "__main__":
    logger.info("Starting Flask server on 0.0.0.0:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)