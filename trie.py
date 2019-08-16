from json import dumps

_end = '_end'
class Trie():
    def __init__(self, words):
        self.root = dict()
        for word in words:
            current_dict = self.root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = _end

    def __repr__(self):
        return dumps(self.root)
