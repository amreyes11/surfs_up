from flask import Flask
app = Flask(__name__)
# Our Flask app has been created—let's create our first route!

# Now, we need to define the starting point
@app.route('/')
def hello_world():
    return 'Hello world'





