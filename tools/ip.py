import ipinfo
import sys

access_token = "IPINFO ACCESS TOKEN"

def ip_search():       
    try: 
        try:
            ip_address = sys.argv[1]
        except IndexError:
            ip_address = str(input("Target IP: "))

        handler = ipinfo.getHandler(access_token)

        details = handler.getDetails(ip_address)

        for key, value in details.all.items():
            print(f"{key}: {value}")
    
    except KeyboardInterrupt:
        print("\
            ")
        return