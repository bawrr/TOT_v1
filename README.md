# TOT_v1
# Trick or Treater Counter App

The **Trick or Treater Counter** is a simple web application built using Flask that allows you to keep track of the number of trick-or-treaters visiting your house on Halloween. It provides features to add trick-or-treaters, reset the count, and export the data to a CSV file.

## Prerequisites

Before running the **Trick or Treater Counter** app, you'll need to have the following prerequisites installed:

- Python 3.6 or higher
- Flask (Python web framework)
- SQLite (for the database)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/trick-or-treater-counter.git
cd trick-or-treater-counter
```
Trick or Treater Counter App
The Trick or Treater Counter is a simple web application built using Flask that allows you to keep track of the number of trick-or-treaters visiting your house on Halloween. It provides features to add trick-or-treaters, reset the count, and export the data to a CSV file.

### Create a Virtual Environment (Optional but Recommended):
It's a good practice to create a virtual environment to isolate the app's dependencies:
```bash
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
```

### Install Dependencies:
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### Run the App:
Start the Flask app by running the following command:
```bash
python main.py
```
The app will be accessible at http://localhost:5000 in your web browser.

## Usage
Adding Trick-or-Treaters: Click the "Add Trick or Treater" button to add a new trick-or-treater to the count. The app records the current timestamp.

Resetting Data: Click the "Reset Data" button to reset the trick-or-treater count and clear all recorded data. A confirmation prompt will appear.

Exporting Data to CSV: Click the "Export Data to CSV" button to export the recorded data to a CSV file named trick_or_treaters.csv.

Viewing Trick-or-Treater Count: The app displays the current trick-or-treater count at the top of the page. The count is updated when you add or reset data.
