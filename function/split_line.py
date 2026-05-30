def split_line(line, sep) -> list:
    if line  == '':
        return ['']  
    new_word = ''
    res_list = []
    flag_marks = False
    for i in line:
        if i == '"' or i == "'":
            if flag_marks == False:
                flag_marks = True
                continue
            else:
                flag_marks = False
                continue
        if flag_marks == False:
            if i == sep:
                res_list.append(new_word)
                new_word = ''
            else:
                new_word += i
        else:
            if i == '"' or i == "'":
                continue
            else:
                new_word += i
    res_list.append(new_word)
    return res_list