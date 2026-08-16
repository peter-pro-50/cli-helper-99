import time
from multiprocessing import Pool

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_item(self, item):
        # Simulate a time-consuming process
        time.sleep(1)
        return item * 2

    def process_all(self):
        with Pool() as pool:
            results = pool.map(self.process_item, self.data)
        return results

if __name__ == '__main__':
    dp = DataProcessor(range(10))
    start_time = time.time()
    processed_data = dp.process_all()
    end_time = time.time()
    print(f'Processed Data: {processed_data}')
    print(f'Time taken: {end_time - start_time:.2f} seconds')