from flask import Flask,render_template,request
from utils.Checker import Checker

app = Flask(__name__)

@app.route("/",methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/api/check",methods=["GET"])
# Params chỉ bao gồm url của trang web cần check
def check():
    submit_url = request.args["url"]
    print("Getting info for",submit_url)
    result = Checker.check_url_status(submit_url)
    return str(result)

# remove cache for development purpose
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(threaded=True)