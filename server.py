# This action requires the 'csv' module
# import csv
from flask import Flask, render_template
app = Flask(__name__,template_folder="./templates", static_folder="./static", instance_relative_config=True)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/alexa')
def alexa_template():
  print ('I got clicked!')

  return render_template('alexa.html')

if __name__ == '__main__':
  app.run(debug=True)

