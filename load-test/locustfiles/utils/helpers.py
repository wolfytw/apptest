def get_response_time(response):
    return response.elapsed.total_seconds()

def parse_csv(file_path):
    import csv
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def log_request_info(response):
    print(f"Request URL: {response.url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Time: {get_response_time(response)} seconds")