# Build an RPG Character
# Building a small app that creates a character for an RPG adventure

# User Stories:
# 1. Have a function named create_character.
# 2. The function should accept, in order, a character name followed by three stats:
# strength, intelligence, and charisma.
# 3. The char name should be validated:
# - If the char name is not a string, return "The character name should be a string".
# - If the char name is an empty string, return "The character should have a name".
# - If the char name is longer than 10 characters, return "The character name is too long".
# - If the char name contains spaces, return "The character name should not contain spaces".
# 4. The stats should also be validated:
# - If one or more stats are not integers, return "All stats should be integers".
# - If one or more stats are less than 1, return "All stats should be no less than 1".
# - If one or more stats are more than 4, return "All stats should be no more than 4".
# - If the sum of all stats does not equal 7. return "The character should start with 7 points".
# 5. If all values pass the verification, the function should return a string with four lines:
# - The first line contain the character name
# - Lines 2 - 4 should start with the stat abbreviation, STR, INT, or CHA (in this order),
# then a space, and then a number of full dots(●) equal to the value of the stat, and 
# a number of empty dots(○) to reach 10. Example: if the value of strength is 3, there must
# be 3 full dots followed by 7 empty dots.

# Note: While str and int are common abbreviations for the stats, Python also uses those 
# names for its string and integer types, so it's best if you avoid using them as variable names.
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intel, cha):
    stats = (strength, intel, cha)
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == '':
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not isinstance(strength, int) or not isinstance (intel, int) or not isinstance(cha, int):
        return "All stats should be integers"
    if strength < 1 or intel < 1 or cha < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intel > 4 or cha > 4:
        return "All stats should be no more than 4"
    if strength + intel + cha != 7:
        return "The character should start with 7 points"

    return f"{name}\nSTR {full_dot*strength}{empty_dot*(10-strength)}\nINT {full_dot*intel}{empty_dot*(10-intel)}\nCHA {full_dot*cha}{empty_dot*(10-cha)}"
    return f"""{name}\nSTR {full_dot * strength}{empty_dot * (10 - strength)} 
INT {full_dot * intel}{empty_dot * (10 - intel)}
CHA {full_dot * cha}{empty_dot * (10 - cha)}"""
    
print(create_character('ren', 3, 2, 1))
