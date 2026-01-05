import requests
import json

def test_petstore_swagger():
    url = "http://127.0.0.1:8000/api/full-workflow"
    payload = {
        "spec_url": "https://petstore.swagger.io/v2/swagger.json",
        "api_base_url": "https://petstore.swagger.io/v2"
    }
    
    print(f"Sending request to {url} with payload: {payload}")
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("Success!")
            print(f"Message: {data.get('message')}")
            test_plan = data.get('test_plan', {})
            print(f"Total Tests Generated: {test_plan.get('total_tests')}")
            # Print first test case as sample
            if test_plan.get('test_cases'):
                print("Sample Test Case:")
                print(json.dumps(test_plan['test_cases'][0], indent=2))
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_petstore_swagger()
