from flask import Flask, request, jsonify
import HardestTasks.config as app_config
from HardestTasks.yandex_manager import YandexManager

app = Flask(__name__)
yandex_manager = YandexManager(app_config.YANDEX_SEARCH_URL, app_config.API_THREADS_NUMBER)


@app.route('/search', methods=['GET'])
def get_tasks():
    query_list = request.args.getlist('query')
    if len(query_list) > 0:
        print('Queries: ', query_list)
        response = yandex_manager.perform_search(query_list)
        return jsonify(response)
    else:
        return 'Pass queries'


if __name__ == '__main__':
    app.run(host=app_config.APP_HOST, port=app_config.APP_PORT)
