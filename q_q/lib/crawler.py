import os
import requests
import json
import tqdm

from search import get_all_message
from vectorizer import vocab

# チャンネルリストを取得する
def load_channles(access_token, verbose=False):
    if verbose:
        print('load all channels')
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    res = requests.get(
        "https://q.trap.jp/api/v3/channels",
        headers=headers,
    )

    if verbose:
        print('status:', res.status_code)

    return res.json()

# sodanチャンネルのidを取得する
def get_sodan_ids(all_channel, verbose=False):
    sodan_channles = set()
    if verbose:
        print('load sodan channels')
        iterator = tqdm.tqdm(all_channel['public'])
    else:
        iterator = all_channel['public']

    for ch in iterator:
        if 'sodan' in ch['name']:
            sodan_channles.add(ch['id'])

    return sodan_channles

# sodanチャンネルの子チャンネルのidを取得する
def get_child_sodan_channels(sodan_channels, all_channel, verbose=False):
    child_sodan_channels = set()
    if verbose:
        print('load child sodan channels')
        iterator = tqdm.tqdm(all_channel['public'])
    else:
        iterator = all_channel['public']
    for ch in iterator:
        if ch['parent_id'] in sodan_channels:
            child_sodan_channels.add(ch['id'])

    return child_sodan_channels


def build(verbose=False):
    ACCESS_TOKEN = os.getenv("ROBOP_ACCESS_TOKEN") 
    # "https://q.trap.jp/api/v3/channels"をdictで取ってくる
    all_channels = load_channles(ACCESS_TOKEN, verbose=verbose)
    # 全てのsodanチャンネルのid収集する
    sodan_channels = get_sodan_ids(all_channels, verbose=verbose)
    # sodanチャンネルの子チャンネルに対しても収集する
    sodan_channles_include_child = get_child_sodan_channels(sodan_channels, all_channels, verbose=verbose)

    # これらのメッセージを全部収集する
    messages = []
    if verbose:
        print('load all message in sodan channels')
        iterator = tqdm.tqdm(sodan_channles_include_child)
    else:
        iterator = sodan_channles_include_child
    for ch_id in iterator:
        messages.extend(get_all_message(ACCESS_TOKEN, ch_id))
    
    vocabulary = vocab(messages, verbose=verbose)
    with open('vocab.json', 'w') as f:
        # エスケープ消して読めるようにする
        json.dump(vocabulary, f, ensure_ascii=False)

    

if __name__ == '__main__':
    build(verbose=True)




    
