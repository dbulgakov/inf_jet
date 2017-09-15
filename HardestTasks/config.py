import json
import os

with open(os.getcwd() + '/config_file.json') as __json_data_file:
    __app_config = json.load(__json_data_file)

YANDEX_USER_NAME = __app_config['yandex']['user_name']
YANDEX_KEY = __app_config['yandex']['api_key']
YANDEX_SEARCH_URL = "https://yandex.com/search/xml?l10n=en&user=" + YANDEX_USER_NAME + "&key=" + YANDEX_KEY + "&query="


API_THREADS_NUMBER = __app_config['other']['api_thread_number']
APP_HOST = __app_config['web-server']['host']
APP_PORT = __app_config['web-server']['port']



