import json
import requests

snusbase_auth = "SNUSBASE API KEY"
snusbase_api = "https://api-experimental.snusbase.com/"

def main():
    try:
        def send_request(url, body=None):
            headers = {
                "Auth": snusbase_auth,
                "Content-Type": "application/json",
            }
            method = "POST" if body else "GET"
            data = json.dumps(body) if body else None
            response = requests.request(method, snusbase_api + url, headers=headers, data=data)
            return response.json()

        def print_search_results(results, search_type):
            if results:
                print(f"Positive {search_type.capitalize()} Search Results:")
                for index, result in enumerate(results, start=1):
                    print(f"{index}. {result}")
            else:
                print(f"No positive {search_type} search results found.")

        search_type = input("Search type (username, email, lastip, hash, password, name): ")
        search_term = input("Search term: ")

        search_response = send_request("data/search", {
            "terms": [search_term],
            "types": [search_type],
            "wildcard": False,
        })

        print("\nSearch Response:")
        print(json.dumps(search_response, indent=2))

        if search_response.get("status") == "success":
            search_results = search_response.get("data", {}).get(search_type, [])
            print_search_results(search_results, search_type)
    
    except KeyboardInterrupt:
        print("\
            ")
        return

        
