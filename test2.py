from model.functions import Functions
import sys
import bs4
import time
from utils.Checker import Checker
import random
from threading import Thread
import threading


def embed_url(url):
    url = "https://"+url
    threads = [None]*30
    arr_threads_result = []
    arr = []
    try:
        threads[0] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.having_IP_Address(arg1),0)), args=(arr_threads_result,url))
        threads[1] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.URL_Length(arg1),1)), args=(arr_threads_result,url,))
        threads[2] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Shortining_Service(arg1),2)), args=(arr_threads_result,url,))
        threads[3] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.having_At_Symbol(arg1),3)), args=(arr_threads_result,url,))
        threads[4] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.double_slash_redirecting(arg1),4)), args=(arr_threads_result,url,))
        threads[5] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Prefix_Suffix(arg1),5)), args=(arr_threads_result,url,))
        threads[6] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.having_Sub_Domain(arg1),6)), args=(arr_threads_result,url,))
        threads[7] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.SSLfinal_State(arg1),7)), args=(arr_threads_result,url,))
        threads[8] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Domain_registeration_length(arg1),8)), args=(arr_threads_result,url,))
        threads[9] = threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Favicon(arg1),9)), args=(arr_threads_result,url,))
        threads[10]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.port(arg1),10)), args=(arr_threads_result,url,))
        threads[11]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.HTTPS_token(arg1),11)), args=(arr_threads_result,url,))
        threads[12]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Request_URL(arg1),12)), args=(arr_threads_result,url,))
        threads[13]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.URL_of_Anchor(arg1),13)), args=(arr_threads_result,url,))
        threads[14]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Links_in_tags(arg1),14)), args=(arr_threads_result,url,))
        threads[15]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.SFH(arg1),15)), args=(arr_threads_result,url,))
        threads[16]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Submitting_to_email(arg1),16)), args=(arr_threads_result,url,))
        threads[17]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Abnormal_URL(arg1),17)), args=(arr_threads_result,url,))
        threads[18]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Redirect(arg1),18)), args=(arr_threads_result,url,))
        threads[19]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.on_mouseover (arg1),19)), args=(arr_threads_result,url,))
        threads[20]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.RightClick (arg1),20)), args=(arr_threads_result,url,))
        threads[21]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.popUpWidnow (arg1),21)), args=(arr_threads_result,url,))
        threads[22]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Iframe(arg1),22)), args=(arr_threads_result,url,))
        threads[23]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.age_of_domain(arg1),23)), args=(arr_threads_result,url,))
        threads[24]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.DNSRecord(arg1),24)), args=(arr_threads_result,url,))
        threads[25]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.web_traffic(arg1),25)), args=(arr_threads_result,url,))
        threads[26]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Page_Rank(arg1),26)), args=(arr_threads_result,url,))
        threads[27]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Google_Index(arg1),27)), args=(arr_threads_result,url,))
        threads[28]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Links_pointing_to_page(arg1),28)), args=(arr_threads_result,url,))
        threads[29]= threading.Thread(target=lambda arr, arg1: arr_threads_result.append((Checker.Statistical_report(arg1),29)), args=(arr_threads_result,url,))
        # threads[29] = -1
        for i in range(30):
            threads[i].start()
        for i in range(30):
            threads[i].join()
            print("THREAD ",i,"DONE",threads[i])
            print(len(arr))
        print("DONE THREAD")
        print(threads)
        arr_threads_result.sort(key=lambda tup: tup[1])
        for elem in arr_threads_result:
            arr.append(elem[0])
        print(arr)
        return arr
    except Exception as e:
        print(e)
        return -2

f = open("new_data_legit.csv","a",encoding="UTF-8")
urls_file = open("na_dataset.csv","r",encoding="UTF-8")
urls = urls_file.read().split("\n")
urls = urls[165:]
for elems in urls:
    url = elems.split(",")[1].replace('"','')
    # print(url)
    # f.write("HI")
    arr = embed_url(url)
    print(arr)
    if (arr == -2):
        continue 
    print(arr)
    row = ','.join(str(e) for e in arr)
    print(row)
    f.write(row+"\n")
