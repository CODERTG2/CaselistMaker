"""
All you need to do is copy the neg positions from the wiki ->
past it on a Google sheet (get rid of any rows) ->
copy the specific column or round report from sheets ->
paste it on the terminal ->
double enter ->
it will print individual positions.
"""
import re


def take_multiline_input():
    lines = []
    print("Enter neg position disclosure:")
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return '\n'.join(lines)


def convert_input(disclosure):
    disclosure = disclosure.replace('\n', ' ')
    pattern = re.compile(r'1NC(.*?)2NR', re.IGNORECASE | re.DOTALL)
    matches = pattern.findall(disclosure)
    print(matches)
    all_positions = {}
    for match in matches:
        match_list = match.split(', ')
        for position in match_list:
            position = position.replace("---", " ").replace("--", " ").replace("-", " ").replace(":", " ").replace("   ", " ").strip()
            all_positions[position.lower()] = position
    unique_positions = list(all_positions.values())
    for unique_position in unique_positions:
        print(unique_position)


if __name__ == '__main__':
    teamDisclosure = take_multiline_input()
    # print(teamDisclosure)
    convert_input(teamDisclosure)
