from typing import List, Dict, Any


def process_data(data: List[Dict[str, Any]]) -> List[str]:
    """
    Processes a list of dictionaries and extracts values.
    
    Args:
        data (List[Dict[str, Any]]): A list of dictionaries containing data to process.
    
    Returns:
        List[str]: A list of extracted values as strings.
    """
    extracted_values = []
    for item in data:
        if 'value' in item:
            extracted_values.append(str(item['value']))
    return extracted_values


def calculate_average(values: List[float]) -> float:
    """
    Calculates the average of a list of float values.
    
    Args:
        values (List[float]): A list of float values.
    
    Returns:
        float: The average of the provided values.
    """
    if not values:
        return 0.0
    total = sum(values)
    return total / len(values)


def main() -> None:
    """
    Main function to execute the processing.
    """
    sample_data = [{'value': 10}, {'value': 20}, {'value': 30}]
    extracted = process_data(sample_data)
    average = calculate_average([float(v) for v in extracted])
    print(f'Extracted: {extracted}, Average: {average}')


if __name__ == '__main__':
    main()