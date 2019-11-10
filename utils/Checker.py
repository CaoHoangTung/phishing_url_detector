# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import ssl
import urllib
import urllib.request
from urllib.parse import urlparse
from urllib.request import urlopen
import whois
import datetime
from tldextract import extract
# import dnspython as dns
import dns.resolver
import bs4
import regex
import socket
import threading
import requests
from model.functions import Functions
import numpy as np
import time

class Checker():
    # def __init__(self):
    #     self.x = 1
    #     pass
    
    def check_connection(url):
        try:
            r = requests.get(url)
            return 1
        except:
            return 0
        # input_value is an array containing feature specified in /features.txt
        # return 1/-1 : Phishing/Normal
        return 1

    def having_IP_Address(url):
        symbol = regex.findall(r'(http((s)?)://)((((\d)+).)*)((\w)+)(/((\w)+))?',url)
        if(len(symbol)!=0):
            having_ip = 1 
        else:
            having_ip = -1 
        return(having_ip)        
            
    def URL_Length(url):
        length=len(url)
        if(length<54):
            return -1
        elif(54<=length<=75):
            return 0
        else:
            return 1

    def Shortining_Service(url):
        r = requests.get(url)
        if len(r.history) > 1:
            return 1
        else:
            return -1
        # proxyht
        return 1
    
    def having_At_Symbol(url):
        symbol=regex.findall(r'@',url)
        if(len(symbol)==0):
            return -1
        else:
            return 1 
    
    def double_slash_redirecting(url):
        if url.count('http') or url.count('https'):
            pass
        return 1
    
    def Prefix_Suffix(url):
        subDomain, domain, suffix = extract(url)
        if(domain.count('-')):
            return 1
        else:
            return -1
    
    def having_Sub_Domain(url):
        subDomain, domain, suffix = extract(url)
        if(subDomain.count('.')==0):
            return -1
        elif(subDomain.count('.')==1):
            return 0
        else:
            return 1
    
    def SSLfinal_State(url):
        try:
            if(regex.search('^https',url)):
                usehttps = 1
            else:
                usehttps = 0
            subDomain, domain, suffix = extract(url)
            host_name = domain + "." + suffix
            context = ssl.create_default_context()
            sct = context.wrap_socket(socket.socket(), server_hostname = host_name)
            sct.connect((host_name, 443))
            certificate = sct.getpeercert()
            # print("CERTIFICATE:",certificate)
            startingDate = str(certificate['notBefore'])
            endingDate = str(certificate['notAfter'])
            startingYear = int(startingDate.split()[3])
            endingYear = int(endingDate.split()[3])
            Age_of_certificate = endingYear-startingYear
            if((usehttps==1) and (Age_of_certificate>=1) ):
                return -1 
            else:
                return 1 
        except Exception as e:
            return 1  
    
    def Domain_registeration_length(url):
        try:
            w = whois.whois(url)
            updated = w.updated_date
            exp = w.expiration_date
            length = (exp[0]-updated[0]).days
            if(length<=365):
                return 1
            else:
                return -1
        except:
            return 0    
    
    def Favicon(url):
        # Tung + Na
        return 1
    
    def port(url):
        subDomain, domain, suffix = extract(url)
        host_name = domain + "." + suffix
        DEFAULT_TIMEOUT = 0.5
        open_port = []
        list_ports = [21,22,23,80,443,445,1433,1521,3306,3389]
        timeout=DEFAULT_TIMEOUT
        TCPsock = socket.socket()
        TCPsock.settimeout(timeout)
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            for i in list_ports:
                result = TCPsock.connect((host_name, i))
                if result == 0:
                    open_port.append(i)
        except:
            pass
        if (80,443 in open_port) and  len(list_ports) > 2:
            return 1
        elif (80,443 in open_port) and len(list_ports) == 2:
            return -1
                            
    def HTTPS_token(url):
        subDomain, domain, suffix = extract(url)
        host =subDomain +'.' + domain + '.' + suffix 
        if(host.count('https')): 
            return 1
        else:
            return -1
    
    def Request_URL(url):
        # proxyht
        r = requests.get(url)
        html = r.text
        domain = urlparse(url)[1]
        
        domain_elements = domain.split(".")
        domain = ".".join(domain_elements[len(domain_elements)-2:])
        # print("done domain",domain)
        regex_external = "(href=|src=)(\"|')((https|http)://)"
        # regex_external = "(\"|')http"

        links = regex.findall(regex_external,html)

        regex_all = "(href=|src=)(\"|')(.*?)(\"|')"
        total_links = len(regex.findall(regex_all,html))
        # print("done getting regex")
        count_diff = 0 # number of external domains
        for link in links:
            # print(link)
            domain_of_link = urlparse(link[2])[1]
            domain_elements = domain_of_link.split(".")
            domain_of_link = ".".join(domain_elements[len(domain_elements)-2:len(domain_elements)])
            # print("DOMAIN OF LINK:",domain_of_link)
            count_diff += domain_of_link != domain
        if (total_links == 0):
            return 1
        
        diff_rate = count_diff / total_links
        
        # print(diff_rate,count_diff,len(links),total_links)
            
        # print(len(links))
        # print(domain)
        if diff_rate < 0.22:
            return -1
        elif diff_rate <= 0.61:
            return 0
        else:
            return 1
    
    def URL_of_Anchor(url):
        # print("ANCHOR")
        # proxyht
        t1 = time.time()
        regex_str = "<a href=(\"|\')#"
        # print("TIME TAKEN:",time.time()-t1)
        html = requests.get(url).text
        # print("HTML GET")
        anchor_list = regex.findall(regex_str,html)
        # print("AN")
        # print("ANCHOR LIST",anchor_list)
        return -1
    
    def Links_in_tags(url):
        # MrNA
        return -1
    
    def SFH(url):
        # MrNA
        return -1
    
    def Submitting_to_email(url):
        # MrNA
        return -1

    def Abnormal_URL(url):
        # MrNA
        return -1
    
    def Redirect(url):
        # proxyht
        r = requests.get(url)
        redirections = len(r.history)
        # print(redirections)
        if redirections <= 1:
            return -1
        elif redirections < 4:
            return 0
        else:
            return 1
        # still need to validate client redirecting sites
    
    def on_mouseover(url):
        try:
            html = requests.get(url).text
            soup = BeautifulSoup(html, 'html.parser')
            p = soup.find_all('script')
            result = 1
            strr = ""
            for jss in p:
                strr = strr + jss.text
            if "window.status" in strr:
                result = -1
            return result
        except:
            return 1
    
    def RightClick(url):
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        p = soup.find_all('script')
        result = 1
        strr = ""
        for jss in p:
            strr = strr + jss.text
        if "contextmenu" in strr:
            result = -1
        return result
    
    def popUpWidnow(url):
        # MrNA
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        p = soup.find_all('script')
        result = 1
        strr = ""
        for jss in p:
            strr = strr + jss.text
        if "window.open" in strr:
            result = -1
        return result
    
    def Iframe(url):
        # proxyht
        import requests
        html = requests.get(url).text
        if "</iframe>" in html:
            return -1
        else:
            return 1
    
    def age_of_domain (url):
        try:
            w = whois.whois(url)
            start_date = w.creation_date
            current_date = datetime.datetime.now()
            age =(current_date-start_date[0]).days
            if(age>=180):
                return -1
            else:
                return 1
        except Exception as e:
            print(e)
            return 0

    def DNSRecord(url):
        try: 
            result = dns.resolver.query(url, 'A')
            for i in result:
                if i:
                  return -1  
        except:    
            return 1

    def web_traffic(url):
        soup = bs4.BeautifulSoup(urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url='+url).read(),features="html.parser")
        if not hasattr(soup.popularity,'text'):
            return 1

        rank = int(soup.popularity['text'])
        if rank < 100000:
            return -1
        else:
            return 1

    def Page_Rank(url):
        URL = "https://openpagerank.com/api/v1.0/getPageRank"
        PARAMS = {'domains[]':'google.com'} 
        r=requests.get(URL,params=PARAMS, headers={'API-OPR':'8044swwk8og00wwgc8ogo80cocs00o0o4008kkg0'})
        json_data = r.json()
        domainarray = json_data['response']
        target = domainarray[0]
        rank = target['rank']
        if rank=="None" or float(rank or 0.1)<0.2:
            return -1
        else:
            return 1

    def Google_Index(url):
        r = requests.head("https://webcache.googleusercontent.com/search?q=cache:" + url)
        if r.status_code == 404:
            return -1
        else:
            return 1

    def Links_pointing_to_page(url): # backlinks
        # proxyht
        return 0

    def Statistical_report(url):
        # proxyht
        # return 1
        f = open("model/data/urls.csv","r",encoding="UTF-8")
        data = f.read().split("\n")
        print(len(data))
        if url in data:
            return 1
        else: 
            return -1

    def vector(url):
        vec = [[url_having_ip(url),url_length(url),url_short(url),having_at_symbol(url),doubleSlash(url),prefix_suffix(url),sub_domain(url),SSLfinal_State(url),
                domain_registration(url),favicon(url),port(url),https_token(url),request_url(url),url_of_anchor(url),Links_in_tags(url),sfh(url),email_submit(url),abnormal_url(url),
                redirect(url),on_mouseover(url),rightClick(url),popup(url),iframe(url),age_of_domain(url),dns(url),web_traffic(url),page_rank(url),google_index(url),
                links_pointing(url),statistical(url)]]
        
        return vec

    
