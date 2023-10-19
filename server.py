from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("training_02.html")

@app.route("/run_script", methods = ["POST"])
def run_script():
    subprocess.run("./two.py", shell=True, check=True)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
