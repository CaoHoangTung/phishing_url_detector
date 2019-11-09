from flask import Flask,render_template,request
from utils.Checker import Checker
from model.functions import Functions
import threading
import requests
app = Flask(__name__)
feature_count = 30

@app.route("/",methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/api/check",methods=["GET"])
# Params chỉ bao gồm url của trang web cần check
def check():
    submit_url = request.args["url"]
    if not Checker.check_connection(submit_url):
        return "-1"
    if(Checker.Statistical_report(submit_url) == 1):
        return "1"

    print("Getting info for",submit_url)
    input_array = embed_url(submit_url)
    print(input_array)
    print(len(input_array))
    result = Functions.check_vector(input_array)
    if (result == 1):
        f = open("model/data/urls.csv","a",encoding="UTF-8")
        f.write(submit_url+"\n")
    return str(result)

def embed_url(url):
    threads = [None]*30
    arr = []
    try:
        threads[0] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.having_IP_Address(arg1)), args=(arr,url))
        threads[1] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.URL_Length(arg1)), args=(arr,url,))
        threads[2] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.Shortining_Service(arg1)), args=(arr,url,))
        threads[3] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.having_At_Symbol(arg1)), args=(arr,url,))
        threads[4] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.double_slash_redirecting(arg1)), args=(arr,url,))
        threads[5] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.Prefix_Suffix(arg1)), args=(arr,url,))
        threads[6] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.having_Sub_Domain(arg1)), args=(arr,url,))
        threads[7] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.SSLfinal_State(arg1)), args=(arr,url,))
        threads[8] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.Domain_registeration_length(arg1)), args=(arr,url,))
        threads[9] = threading.Thread(target=lambda arr, arg1: arr.append(Checker.Favicon(arg1)), args=(arr,url,))
        threads[10]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.port(arg1)), args=(arr,url,))
        threads[11]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.HTTPS_token(arg1)), args=(arr,url,))
        threads[12]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Request_URL(arg1)), args=(arr,url,))
        threads[13]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.URL_of_Anchor(arg1)), args=(arr,url,))
        threads[14]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Links_in_tags(arg1)), args=(arr,url,))
        threads[15]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.SFH(arg1)), args=(arr,url,))
        threads[16]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Submitting_to_email(arg1)), args=(arr,url,))
        threads[17]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Abnormal_URL(arg1)), args=(arr,url,))
        threads[18]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Redirect(arg1)), args=(arr,url,))
        threads[19]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.on_mouseover (arg1)), args=(arr,url,))
        threads[20]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.RightClick (arg1)), args=(arr,url,))
        threads[21]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.popUpWidnow (arg1)), args=(arr,url,))
        threads[22]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Iframe(arg1)), args=(arr,url,))
        threads[23]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.age_of_domain(arg1)), args=(arr,url,))
        threads[24]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.DNSRecord(arg1)), args=(arr,url,))
        threads[25]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.web_traffic(arg1)), args=(arr,url,))
        threads[26]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Page_Rank(arg1)), args=(arr,url,))
        threads[27]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Google_Index(arg1)), args=(arr,url,))
        threads[28]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Links_pointing_to_page(arg1)), args=(arr,url,))
        threads[29]= threading.Thread(target=lambda arr, arg1: arr.append(Checker.Statistical_report(arg1)), args=(arr,url,))
        # threads[29] = -1
        for i in range(30):
            threads[i].start()
        for i in range(30):
            threads[i].join()
            print("THREAD ",i,"DONE",threads[i])
            print(len(arr))
        print("DONE THREAD")
        print(threads)
        print(arr)
        return arr
    except Exception as e:
        return e

# def embed_url(url):
#     arr = [0] * feature_count
#     arr[0]  = Checker.having_IP_Address(url)
#     arr[1]  = Checker.URL_Length(url)
#     arr[2]  = Checker.Shortining_Service(url)
#     arr[3]  = Checker.having_At_Symbol(url)
#     arr[4]  = Checker.double_slash_redirecting(url)
#     arr[5]  = Checker.Prefix_Suffix(url)
#     arr[6]  = Checker.having_Sub_Domain(url)
#     arr[7]  = Checker.SSLfinal_State(url)
#     print("DONE SSL")
#     arr[8]  = Checker.Domain_registeration_length(url)
#     print("DONE DOMAIN LEN")
#     arr[9]  = Checker.Favicon(url)
#     print("DONE FAV")
#     arr[10] = Checker.port(url)
#     print("DONE PORT")
#     arr[11] = Checker.HTTPS_token(url)
#     print("DONE HTTPSTOKEN")
#     arr[12] = Checker.Request_URL(url)
#     print("DONE Request_URL")
#     arr[13] = Checker.URL_of_Anchor(url)
#     print("DONE URL_of_Anchor")
#     arr[14] = Checker.Links_in_tags(url)
#     print("DONE Links_in_tags")
#     arr[15] = Checker.SFH(url)
#     print("DONE SFH")
#     arr[16] = Checker.Submitting_to_email(url)
#     print("DONE Submitting_to_email")
#     arr[17] = Checker.Abnormal_URL(url)
#     print("DONE abnormal")
#     arr[18] = Checker.Redirect(url)
#     print("DONE redirect")
#     arr[19] = Checker.on_mouseover (url)
#     print("DONE onmouseover")
#     arr[20] = Checker.RightClick (url)
#     print("DONE rightclick")
#     arr[21] = Checker.popUpWidnow (url)
#     print("DONE popupwindow")
#     arr[22] = Checker.Iframe(url)
#     print("DONE iframe")
#     arr[23] = Checker.age_of_domain(url)
#     print("DONE age of domain")
#     arr[24] = Checker.DNSRecord(url)
#     print("DONE dnsrecord")
#     arr[25] = Checker.web_traffic(url)
#     print("DONE webtraffic")
#     arr[26] = Checker.Page_Rank(url)
#     print("DONE page rank")
#     arr[27] = Checker.Google_Index(url)
#     print("DONE google index")
#     arr[28] = Checker.Links_pointing_to_page(url)
#     print("DONE backlinks")
#     arr[29] = Checker.Statistical_report(url)
#     print("DONE stat")
#     return arr

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