from flask import Flask, jsonify, Response
import pymysql
from flask_cors import CORS
import os
import logging

# Configure logging
LOG_FILE_PATH = '/var/log/backend/flask_error.log'  # Specify the log file path
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=LOG_FILE_PATH,  # Log errors to the specified file
    filemode='a'  # Append to the log file
)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

@app.route('/data', methods=['GET'])
def get_data():
    # Check if environment variables are set
    required_env_vars = ['DB_HOST', 'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'PORT']
    for var in required_env_vars:
        if var not in os.environ:
            error_message = f"Missing environment variable: {var}"
            logging.error(error_message)  # Log the error
            return jsonify({"error": error_message}), 500

    try:
        # Connect to the database
        connection = pymysql.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            database=os.environ['DB_NAME']
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM test_table")
            rows = cursor.fetchall()

        # Close the connection after use
        connection.close()

        # Return data as JSON response
        return jsonify(rows)

    except pymysql.MySQLError as e:
        # Log MySQL-specific errors
        error_message = f"MySQL error: {str(e)}"
        logging.error(error_message)  # Log the error
        return jsonify({"error": error_message}), 500
    except Exception as e:
        # Log any other errors
        error_message = f"An error occurred: {str(e)}"
        logging.error(error_message)  # Log the error
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    # Ensure the PORT environment variable is set
    port = os.environ.get('PORT', 5000)  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=int(port))
