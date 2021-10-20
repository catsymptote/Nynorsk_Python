class NN_Dict:
    '''
    Converts to and from NN-Python.
    Has a dict:
    {Python-keyword: NN-keyword}
    '''

    # Load keywords
    with open('keywords.csv', 'r', encoding='utf-8') as f:
        keyword_text = f.read()
    keywords = keyword_text.split('\n')

    keyword_dict = {}
    for keyword_pair in keywords[1:]:
        if len(keyword_pair) == 0 or keyword_pair[0] == '#':
            continue

        py_key, nn_key = keyword_pair.split(',')
        keyword_dict[py_key.strip()] = nn_key.strip()

    @staticmethod
    def Py_keywords(_=None):
        return list(NN_Dict.keyword_dict.keys())

    @staticmethod
    def NN_keywords(_=None):
        return list(NN_Dict.keyword_dict.values())

    @staticmethod
    def to_NN(keyword: str) -> str:
        return NN_Dict.keyword_dict[keyword]

    @staticmethod
    def to_Py(keyword: str) -> str:
        for key in NN_Dict.keyword_dict.keys():
            if NN_Dict.keyword_dict[key] == keyword:
                return key
        return ''
