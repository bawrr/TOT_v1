import subprocess

# Specify the library you want to install
#library_name = "flask"  # Replace with the name of the library you want to install

# Use pip to install the library
#try:
#    subprocess.check_call(["pip", "install", library_name])
#    print(f"Successfully installed {library_name}")
#except subprocess.CalledProcessError:
#    print(f"Failed to install {library_name}")


from flask import Flask, render_template, request, jsonify
from database import create_table, add_trick_or_treater, export_data_to_csv, reset_data, get_trick_or_treater_count
from datetime import datetime, timedelta, timezone


app = Flask(__name__)

# Create the trick_or_treaters table in the database
create_table()

# Define a function to convert UTC time to Eastern Time (ET)
def convert_to_eastern(utc_time):
    # Define the time difference between UTC and Eastern Time (ET)
    et_offset = timedelta(hours=-5)  # Eastern Time (ET) is UTC-5

    # Adjust the UTC time to Eastern Time (ET)
    et_time = utc_time + et_offset
    return et_time.strftime('%Y-%m-%d %H:%M:%S %Z')  # Format the time as desired

@app.route('/')
def index():
    trick_or_treater_count = get_trick_or_treater_count()  # Retrieve the trick-or-treater count
    return render_template('index.html', trick_or_treater_count=trick_or_treater_count)

@app.route('/add', methods=['POST'])
def add():
    add_trick_or_treater(None)  # Add trick-or-treater without a name
    return jsonify({'count': get_trick_or_treater_count()})  # Retrieve and return the updated trick-or-treater count

@app.route('/reset', methods=['GET'])
def reset():
    reset_data()
    return render_template('index.html', trick_or_treater_count=0)  # Initialize the count to 0

@app.route('/export', methods=['GET'])
def export():
    export_data_to_csv()
    return render_template('index.html', trick_or_treater_count=get_trick_or_treater_count())  # Retrieve and return the trick-or-treater count

@app.route('/count', methods=['GET'])
def count():
    trick_or_treater_count = get_trick_or_treater_count()
    return jsonify({'count': trick_or_treater_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

