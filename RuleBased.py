import re

class RuleBased:
    """
    All you need to do is copy the neg positions from the wiki ->
    past it on a Google sheet (get rid of any rows) ->
    copy the specific column or round report from sheets ->
    paste it on the terminal ->
    double enter ->
    it will print individual positions.
    """
    
    def __init__(self, disclosure):
        self.disclosure = disclosure
        self.arguments = None
        self.regex_pattern = r'1NC(.*?)2NR'

    def process(self):
        self.arguments = self.convert_input()
        return self.arguments

    def convert_input(self):
        self.disclosure = self.disclosure.replace('\n', ' ')
        pattern = re.compile(self.regex_pattern, re.IGNORECASE | re.DOTALL)
        matches = pattern.findall(self.disclosure)
        all_positions = {}
        for match in matches:
            match_list = match.split(', ')
            for position in match_list:
                position = position.replace("---", " ").replace("--", " ").replace("-", " ").replace(":", " ").replace("   ", " ").strip()
                all_positions[position.lower()] = position
        unique_positions = list(all_positions.values())

        print(unique_positions)
        return '\n'.join(unique_positions)
