def port(url):
        subDomain, domain, suffix = extract(url)
        host_name = domain + "." + suffix
        DEFAULT_TIMEOUT = 0.5

        list_ports = []
        def TCP_connect(ip, port_number, output,timeout=DEFAULT_TIMEOUT):
            TCPsock = socket.socket()
            TCPsock.settimeout(timeout)
            TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                TCPsock.connect((ip, port_number))
                output[port_number] = 'open'
            except:
                output[port_number] = ''

        def scan_ports(host_ip):

            threads = []        
            output = {}        

            for i in range(10000):
                t = threading.Thread(target=TCP_connect, args=(host_ip, i, output))
                threads.append(t)

            for i in range(10000):
                threads[i].start()

            for i in range(10000):
                threads[i].join()

            for i in range(10000):
                if output[i] == 'open':
                    list_ports.append(i)
            
        def main():
            host_ip = host_name
            # host_ip = 'www.google.com'
            scan_ports(host_ip)
            if (80,443 in list_ports) and  len(list_ports) > 2:
                return 1
            elif (80,443 in list_ports) and len(list_ports) = 2:
                return -1


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
            print("CERTIFICATE:",certificate)
            startingDate = str(certificate['notBefore'])
            endingDate = str(certificate['notAfter'])
            startingYear = int(startingDate.split()[3])
            endingYear = int(endingDate.split()[3])
            Age_of_certificate = endingYear-startingYear
            if((usehttps==1) and and (Age_of_certificate>=1) ):
                return -1 
            else:
                return 1 
        except Exception as e:
            return 1  