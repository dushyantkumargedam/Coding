full_dot = '●'
empty_dot = '○'
total_dot = 10

def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return "The character name should be a string"
    if len(name)>10:
        return "The character name is too long"
    if ' 'in name:
        return "The character name should not contain spaces"
        
    stats = [strength,intelligence,charisma]
    
    for i in stats:
        if not isinstance(i,int):
            return "All stats should be integers"
    
    for i in stats:
        if i<1:
            return "All stats should be no less than 1"
        if i>4:
            return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"

    str_line = create_stat_line("STR",strength)
    int_line = create_stat_line("INT",intelligence)
    cha_line = create_stat_line("CHA",charisma)

    return f"{name}\n{str_line}\n{int_line}\n{cha_line}"

def create_stat_line(abbreviation, value):
    full_dots = full_dot * value
    empty_dots = empty_dot * (total_dot - value)
    return f"{abbreviation}{full_dots}{empty_dots}"

# Just call the function as the last line
print(create_character("ren",4,2,1))