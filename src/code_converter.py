from src.nn_dict import NN_Dict


class Converter:
    def __init__(self, to_nynorsk: bool = False):
        self.to_nynorsk = to_nynorsk

    def to_NN(self, code: str, to_nynorsk: bool = True) -> str:
        new_code: str = ''
        idx: int = 0
        word: str = ''
        while idx < len(code):
            char = code[idx]

            if len(word) == 0:
                if char.isalpha():
                    word += char
                else:
                    new_code += char
            else:
                if char.isalpha():
                    word += char
                else:
                    if to_nynorsk:
                        if word in NN_Dict.Py_keywords():
                            word = NN_Dict.to_NN(word)
                    else:
                        if word in NN_Dict.NN_keywords():
                            word = NN_Dict.to_Py(word)
                    new_code += word
                    new_code += char
                    word = ''

            idx += 1

        return new_code

    def to_Py(self, code: str) -> str:
        return self.to_NN(code, to_nynorsk=False)
