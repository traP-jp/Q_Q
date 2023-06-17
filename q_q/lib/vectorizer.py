from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import MeCab
import re
import tqdm

SPECIAL_WORD = ['break',
    'default',
    'func',
    'interface',
    'select',
    'case',
    'defer',
    'go',
    'map',
    'struct',
    'chan',
    'else',
    'goto',
    'package',
    'switch',
    'const',
    'fallthrough',
    'if',
    'range',
    'type',
    'continue',
    'for',
    'import',
    'return',
    'var',
    'False', 
    'None', 
    'True', 
    'and',
    'as',
    'assert', 
    'async', 
    'await',
    'break',
    'class',
    'continue',
    'def',
    'del',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'if',
    'import',
    'in',
    'is',
    'lambda',
    'nonlocal',
    'not',
    'or',
    'pass',
    'raise',
    'return',
    'try',
    'while',
    'with',
    'yield',
    'int',
    'float'
    ]


# コードブロックからスペシャルワードを削除する
def clean_code(text, special_word_list):
    code_block_pattern = re.compile(r'```(.*?)```', re.DOTALL)
    
    def remove_words(match):
        code_block = match.group(0)
        for word in special_word_list:
            code_block = code_block.replace(word, '')
        return code_block
    
    processed_text = re.sub(code_block_pattern, remove_words, text)
    
    return processed_text

# 温かみのある正規表現により、不要な記号などを削除
def cleanup(text):
    text = clean_code(text, SPECIAL_WORD)
    text = re.sub(r'@\w+',',',text)
    text = re.sub(r'#\w+', ',', text)
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', ',', text)
    text = re.sub(r'[\n\r]', ',', text)
    text = re.sub(r'[\[\]{}()【】「」『』【】〔〕〈〉《》〚〛〘〙〖〗〝〞“”‘’‹›«»]+', ',', text)
    text = re.sub(r'[、。,.`_"]', ',', text)
    return text

# アルファベット小文字一文字か判定。ソースコード中の添字とかを消す用
def is_single_alpha(s):
    return len(s) == 1 and s.isalpha()

# トークナイザ
def tokenize(text):
    text = cleanup(text)
    text = text.replace(' ', '')
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    node = tagger.parseToNode(text)
    result = []
    while node:
        if ',' in node.surface:
            node = node.next
            continue
        if is_single_alpha(node.surface):
            node = node.next
            continue
        if node.feature.split(',')[0] in ['名詞']:
            result.append(node.surface)
        node = node.next
    return result

# メッセージのリストを受け取ると、適切な単語を抽出したリストを作る
def vocab(messages, verbose):
    if verbose:
        print('create vocabulary')
        iterator = tqdm.tqdm(messages)
    else:
        iterator = messages
    vocabulary = []
    for text in iterator:
        text = cleanup(text)
        text = text.replace(' ', '')
        tagger = MeCab.Tagger('-Ochasen')
        tagger.parse('')
        node = tagger.parseToNode(text)
        result = []
        while node:
            if ',' in node.surface:
                node = node.next
                continue
            if is_single_alpha(node.surface):
                node = node.next
                continue
            if node.feature.split(',')[0] in ['名詞']:
                vocabulary.append(node.surface)
            node = node.next

    return list(set(vocabulary))

# 作成したボキャブラをロードする
def load_vocab():
    with open('vocab.json') as f:
        return json.load(f)

# `texts`: 文章の列
# `tokenizer`: トークナイザ
# `vocab_path`: 作成したボキャブラリの保存先(json)
def vectorize(texts, tokenizer, vocab_path):
    vocab = load_vocab(vocab_path)
    vectorizer = TfidfVectorizer(tokenizer=tokenizer, vocabulary=vocab, max_df=0.9)
    vectors = vectorizer.fit_transform(texts)
    return vectors

# `target_vector`: 類似度を計算したい文章のベクトル
# `vectors`: 類似度を計算したい文章のベクトルの集合
# `k`: 類似度の高い文章の数
def top_k_similar(target_vector, vectors, k=5):
    sims = cosine_similarity(target_vector, vectors)
    return sims[0].argsort()[-k:][::-1]

