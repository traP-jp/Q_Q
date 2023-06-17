import traq
from traq.api import message_api

# `_in`チャンネルの中で`word`を含むメッセージを検索する
def search_in(configuration, word, _in, offset=0):
    with traq.ApiClient(configuration) as api_client:
        api_instance = message_api.MessageApi(api_client)
        try:
            api_response = api_instance.search_messages(word=word, offset=offset, _in=_in)
        except traq.ApiException as e:
            print("Exception when calling MessageApi->search_messages: %s\n" % e)
    return api_response

# `channel_id`のチャンネルの全メッセージを取得する
def get_all_message(configuration, channel_id):
    print('load all message in ', channel_id)
    messages = []
    offset = 0
    while True:
        response = search_in(configuration, '', _in=channel_id, offset=offset)
        texts = list(map(lambda m: m['content'], response['hits']))
        if len(texts) == 0:
            break
        else:
            messages.extend(texts)
            offset += 100
    return messages