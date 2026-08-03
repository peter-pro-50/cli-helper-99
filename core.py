import json
import sys

class ErrorHandling:
    def __init__(self):
        self.error_log = []

    def log_error(self, message):
        self.error_log.append(message)
        print(f"Error logged: {message}")

    def handle_edge_cases(self, value):
        if not isinstance(value, (int, float)):
            self.log_error("Invalid input type, must be int or float")
            return None
        elif value < 0:
            self.log_error("Negative value encountered")
            return 0
        return value

def process_data(data):
    handler = ErrorHandling()
    processed_data = []
    
    for item in data:
        processed_item = handler.handle_edge_cases(item)
        if processed_item is not None:
            processed_data.append(processed_item)
    
    return processed_data

if __name__ == '__main__':
    input_data = json.loads(sys.argv[1])
    result = process_data(input_data)
    print(json.dumps(result))