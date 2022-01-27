
# I used this on the words.txt file
class TextFile:
    '''Reads and removes words smaller than 4 letters.'''

    def read_text_file(text_file) -> list:
        with open(text_file) as file:
            words = file.readlines()
            return words
    
    def remove_small_words(words:list, new_file):
        with open(new_file, 'a+') as file:
            for item in list:
                if len(item) > 4:
                    print(f'{item.strip()}', file=file)

    def print_words(words:list):
        for item in words:
            print(item.strip())