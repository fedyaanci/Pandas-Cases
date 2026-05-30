def round_to_2(x):
    return round(float(x), 2)
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

def read_csv_and_calc_mean(lines, sep, column_name):
    headers = split_line(lines[0], sep)
    col_idx = headers.index(column_name)
    
    total = 0.0
    count = 0
    
    for line in lines[1:]:
        if line.strip() == '':
            continue
            
        row = split_line(line, sep)  
        total += float(row[col_idx]) 
        count += 1
        
    return round_to_2(total / count)
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

def read_csv_and_calc_mean(lines, sep, column_name):
    headers = split_line(lines[0], sep)
    col_idx = headers.index(column_name)
    
    total = 0.0
    count = 0
    
    for line in lines[1:]:
        if line.strip() == '':
            continue
            
        row = split_line(line, sep)  
        total += float(row[col_idx])
        count += 1
        
    return round_to_2(total / count)
if __name__ == '__main__':
    n = int(input())
    lines = []

    for _ in range(n):
        lines.append(input().strip())

    sep = input().replace(' ', '+').strip().replace('+', ' ')
    column_name = input().strip()
    
    print(read_csv_and_calc_mean(lines, sep, column_name))