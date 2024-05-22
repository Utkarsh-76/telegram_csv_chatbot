import requests
import json
from credentials import bot_token

FILE_API_URL = f'https://api.telegram.org/bot{bot_token}/getFile'
FILE_CONTENT_API_URL = f'https://api.telegram.org/file/bot{bot_token}/' + '{file_path}'


def get_file(message):
    """
    Send post request with specific params and get response.

    :param message: message that user sent (it already contains document).
    :return: response from request.
    """
    response = requests.post(url=FILE_API_URL, params={'file_id': message['document']['file_id']})
    json_response = json.loads(response.content)
    if response.status_code != 200 or not json_response.get('ok'):
        raise FileNotFoundError()
    data_file = requests.get(url=FILE_CONTENT_API_URL.format(file_path=json_response['result']['file_path']))
    if data_file.status_code != 200:
        raise FileNotFoundError()
    return data_file
