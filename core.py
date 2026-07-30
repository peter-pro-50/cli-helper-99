from typing import List, Dict, Any


def process_data(data: List[Dict[str, Any]]) -> List[str]:
    """
    Process a list of dictionaries and extract the 'name' key.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries containing data.

    Returns:
        List[str]: A list of names extracted from the dictionaries.
    """
    names = []
    for item in data:
        name = item.get('name')
        if name:
            names.append(name)
    return names


def calculate_average(values: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        values (List[float]): A list of numeric values.

    Returns:
        float: The average of the provided values.
    """
    if not values:
        return 0.0
    return sum(values) / len(values)


if __name__ == '__main__':
    sample_data = [{'name': 'Alice'}, {'name': 'Bob'}, {'age': 30}, {'name': 'Eve'}]
    names = process_data(sample_data)
    print(names)

    average = calculate_average([10.0, 20.0, 30.0])
    print(f'Average: {average}')