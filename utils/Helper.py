
class Helper():
    def extract_url_parts(url):
        # return an array, containing parts of url: [protocol,domain1,domain2,...,domainn,path]
        # example: ["https","www","google","com"]
        arr = []
        regex_extract_protocol = "(.*)://"
        regex_extract_