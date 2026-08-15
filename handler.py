from typing import Any, Dict, List


def handle_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """
    Processes an incoming request and returns a response.

    Parameters:
    request (Dict[str, Any]): The incoming request data.

    Returns:
    Dict[str, Any]: A dictionary containing the response data.
    """
    response = {'status': 'success', 'data': None}
    # Simulate processing the request
    if 'action' in request:
        if request['action'] == 'get_data':
            response['data'] = get_data()
        elif request['action'] == 'set_data':
            set_data(request.get('data', None))
            response['data'] = 'Data set successfully'
        else:
            response['status'] = 'error'
            response['message'] = 'Unknown action'
    else:
        response['status'] = 'error'
        response['message'] = 'No action provided'
    return response


def get_data() -> List[str]:
    """
    Simulates data retrieval.

    Returns:
    List[str]: A list of sample data.
    """
    return ['item1', 'item2', 'item3']


def set_data(data: Any) -> None:
    """
    Simulates data setting.

    Parameters:
    data (Any): The data to be set.
    """
    print(f'Setting data: {data}')