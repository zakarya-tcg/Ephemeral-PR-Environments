import os
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Get the branch name from an environment variable. 
# Default to 'local' if the variable is not set.
branch_name = os.environ.get("BRANCH_NAME", "local")

# Define a route for the root URL "/"
@app.route('/')
def hello_world():
    # The HTML we'll display. It's an H1 tag with a message.
    return f"<h1>Hello zakarya! This app is running from the '{branch_name}' environment.</h1>"

# This makes the app runnable directly with 'python app.py'
if __name__ == '__main__':
    # Run the app on host 0.0.0.0 (accessible externally) and port 5000
    app.run(host='0.0.0.0', port=5000)
