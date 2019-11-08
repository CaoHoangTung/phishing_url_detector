from flask import Flask,render_template,request
from utils.Checker import Checker

appppppppp = Flask(__name__)
feature_count = 30

@app.route("/",methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/api/check",methods=["GET"])
# Params chỉ bao gồm url của trang web cần check
def check():
    submit_url = request.args["url"]
    print("Getting info for",submit_url)
    input_array = embed_url(submit_url)
    print(input_array)
    result = Checker.check_url_status(submit_url)
    return str(result)

def embed_url(url):
    arr = [0] * feature_count
    arr[0]  = Checker.having_IP_Address(url)
    arr[1]  = Checker.URL_Length(url)
    arr[2]  = Checker.Shortining_Service(url)
    arr[3]  = Checker.having_At_Symbol(url)
    arr[4]  = Checker.double_slash_redirecting(url)
    arr[5]  = Checker.Prefix_Suffix(url)
    arr[6]  = Checker.having_Sub_Domain(url)
    arr[7]  = Checker.SSLfinal_State(url)
    arr[8]  = Checker.Domain_registeration_length(url)
    arr[9]  = Checker.Favicon(url)
    arr[10] = Checker.port(url)
    arr[11] = Checker.HTTPS_token(url)
    arr[12] = Checker.Request_URL(url)
    arr[13] = Checker.URL_of_Anchor(url)
    arr[14] = Checker.Links_in_tags(url)
    arr[15] = Checker.SFH(url)
    arr[16] = Checker.Submitting_to_email(url)
    arr[17] = Checker.Abnormal_URL(url)
    arr[18] = Checker.Redirect(url)
    arr[19] = Checker.on_mouseover (url)
    arr[20] = Checker.RightClick (url)
    arr[21] = Checker.popUpWidnow (url)
    arr[22] = Checker.Iframe(url)
    arr[23] = Checker.age_of_domain(url)
    arr[24] = Checker.DNSRecord(url)
    arr[25] = Checker.web_traffic(url)
    arr[26] = Checker.Page_Rank(url)
    arr[27] = Checker.Google_Index(url)
    arr[28] = Checker.Links_pointing_to_page(url)
    arr[29] = Checker.Statistical_report(url)
    return arr

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