# -*- coding: utf-8 -*-

import ssl
import urllib.request
import whois
import datetime
from tldextract import extract
from urllib.request import urlopen
import dnspython as dns
import dns.resolver
import bs4
import regex
import socket
import threading

#phishing 1
#legit -1 

class Checker():
    def __init__(self):
        self.x = 1
        pass
    
    def check_url_status(input_value):
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
        except:
            return 0    
    
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
        return 1
    
    def port(url):
        port_open = ['80','443']
        subDomain, domain, suffix = extract(url)
        host = domain +'.'+suffix
        ip = socket.gethostbyname(host)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        valid+port = [80,443]
        def scanner(port):
            try:
                for i in port:
                    sock.connect((ip, port))
                return True
            except:
                return False
        
        for i in port:
            if scanner(portNumber):
                

        
        

    def HTTPS_token(url):
        subDomain, domain, suffix = extract(url)
        host =subDomain +'.' + domain + '.' + suffix 
        if(host.count('https')): 
            return 1
        else:
            return -1
    
    def Request_URL(url):
        return 1
    
    def URL_of_Anchor(url):
        return 1
    
    def Links_in_tags(url):
        return 1
    
    def SFH(url):
        return 1
    
    def Submitting_to_email(url):
        return 1

    def Abnormal_URL(url):
        return 1
    
    def Redirect(url):
        return 1
    
    def on_mouseover(url):
        return 1
    
    def RightClick(url):
        return 1
    
    def popUpWidnow(url):
        return 1
    
    def Iframe(url):
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
        soup = bs4.BeautifulSoup(urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url='+url).read())
        rank=soup.popularity['text']
        if rank < '100000':
            return -1
        elif rank > '100000':
            return 1
    def Page_Rank(url):
        return 1

    def Google_Index(url):
        return 1

    def Links_pointing_to_page(url):
        return 1

    def Statistical_report(url):
        return 1

    def vector(url):
        vec = [[url_having_ip(url),url_length(url),url_short(url),having_at_symbol(url),doubleSlash(url),prefix_suffix(url),sub_domain(url),SSLfinal_State(url),
                domain_registration(url),favicon(url),port(url),https_token(url),request_url(url),url_of_anchor(url),Links_in_tags(url),sfh(url),email_submit(url),abnormal_url(url),
                redirect(url),on_mouseover(url),rightClick(url),popup(url),iframe(url),age_of_domain(url),dns(url),web_traffic(url),page_rank(url),google_index(url),
                links_pointing(url),statistical(url)]]
        
        return vec

    
