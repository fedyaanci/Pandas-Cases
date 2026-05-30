from function.string_to_words_solution import string_to_words_solution

def count_word_solution(s, word):
    """
    Подсчитывает, сколько раз в строке s встречается слово word.
    
    Аргументы:
        s: Строка из слов, разделённых пробелами.
        word: Слово, упоминания которого в строке s нужно подсчитать.
        
    Возвращаемое значение:
        Число раз, которое слово word встречается в строке s.
    """
    
    words = string_to_words_solution(s)
    
    
    return words.count(word)