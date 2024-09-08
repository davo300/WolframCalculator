import requests

# Replace with your Wolfram Alpha App ID
APP_ID = '8AAJJT-957R4K6XWA'

def query_wolfram_alpha(query):
    url = "http://api.wolframalpha.com/v2/query"
    params = {
        'input': query,
        'format': 'plaintext',
        'output': 'JSON',
        'appid': APP_ID
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

def display_results(data):
    if 'queryresult' in data and 'pods' in data['queryresult']:
        for pod in data['queryresult']['pods']:
            if 'subpods' in pod and pod['subpods']:
                for subpod in pod['subpods']:
                    # Display plaintext results
                    if 'plaintext' in subpod:
                        print(f"Result from '{pod['title']}': {subpod['plaintext']}")
    else:
        print("No results found.")

if __name__ == '__main__':
    query = input("Enter a command: ex. integral of x^3 or derivative of x^2: ")
    result = query_wolfram_alpha(query)
    if result:
        display_results(result)
