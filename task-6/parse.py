import re

def parse_response_codes(log_data):
    # Regular expression pattern to match the response code
    pattern = r'\s(\d{3})\s'
    
    # Find all matches in the log data
    response_codes = re.findall(pattern, log_data)
    
    return response_codes

# Example usage
log_data = '''
192.168.1.100 - - [27/Sep/2023:14:30:45 +0000] "GET /api/v1/resource?id=12345 HTTP/1.1" 200 1500 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
192.168.1.101 - - [27/Sep/2023:15:45:20 +0000] "GET /api/v1/resource?id=54321 HTTP/1.1" 500 1200 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
'''

response_codes = parse_response_codes(log_data)
print("Response Codes:", response_codes)