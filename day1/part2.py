
# walk in from left and right

# if left is number, store and stop walking else buffer characters so far and check if valid digit
# if right is number, store and stop walking else buffer characters so far and check if valid digit

import re


def get_number(number: str) -> str:
    if number.isnumeric():
        return number
    
    match number:
        case "one": return "1"
        case "two": return "2"
        case "three": return "3"
        case "four": return "4"
        case "five": return "5"
        case "six": return "6"
        case "seven": return "7"
        case "eight": return "8"
        case "nine": return "9"
    

def check_line(line: str) -> int:
    matches = re.findall("(?=([0-9]{1}|one|two|three|four|five|six|seven|eight|nine))", line)
    return int(f"{get_number(matches[0])}{get_number(matches[len(matches)-1])}")


with open("input.txt") as file:
    sum = 0
    for dirty_line in file:
        line = dirty_line.rstrip()

        line_value = check_line(line)
        sum += line_value
        print(f"{line} = {line_value}")
        
    print(sum)