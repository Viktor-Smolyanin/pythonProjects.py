class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                info = file.read().lower()
                for i in info:
                    if i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        info.replace(i, "")
                        all_words[name] = info.split()
        file.close()
        return all_words

    def find(self, word):
        result = {}
        for value, key in self.get_all_words().items():
            if word.lower() in key:
                result[value] = key.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        for position, key in self.get_all_words().items():
            if word.lower() in key:
                result[position] = key.count(word.lower())
        return result


finder2 = WordsFinder(['test_file.txt'])
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
