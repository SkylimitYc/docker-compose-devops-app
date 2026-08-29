from flask import Flask, jsonify
import os
import psycopg

app = Flask(__name__)


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Backend is running"
    })


@app.route("/api/db-health")
def db_health():
    try:
        conn = get_db_connection()
        conn.close()

        return jsonify({
            "status": "healthy",
            "database": "connected"
        })

    except Exception as error:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(error)
        }), 500


@app.route("/api/users")
def users():
    try:
        conn = get_db_connection()

        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, email FROM users ORDER BY id")
            rows = cursor.fetchall()

        conn.close()

        return jsonify([
            {
                "id": row[0],
                "name": row[1],
                "email": row[2]
            }
            for row in rows
        ])

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500


@app.route("/api")
def api():
    return jsonify({
        "message": "Hello from Docker Compose backend"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
