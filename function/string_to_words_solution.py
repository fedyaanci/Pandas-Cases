def string_to_words_solution(s):
    """
    Разделяет строку на слова.
    
    Аргументы:
        s: Строка из слов, разделённых пробелами.
        
    Возвращаемое значение:
        Список слов, входящих в строку, которые идут в том же порядке,
        в котором они встречались в исходной строке.
    """
    nl = []
    new_word = ''
    for idx ,value in enumerate(s):
        if value != ' ':
            new_word = new_word + value 
            if idx == len(s)-1:
                nl.append(new_word)
                new_word = ''
        elif new_word != '':
            nl.append(new_word)
            new_word = ''
    return nl