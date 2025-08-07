import ollama

class LLMBased:
    def __init__(self, text):
        self.disclosure = text
        self.prompt = f"""
                        All the arguments:
                        {self.disclosure}

                        - read through all the different arguments.
                        - make sure you are checking all the 1NC arguments first
                        - if the 1NC list doesn't exist check 2NC or 1NR or 2NR.
                        - compile and only return a list of unique arguments.
                        - dont give me a python code or anything but just a list of all the unique 1NC and 2NR.
                        - don't have repeating arguments.
                        - don't number the arguments.
                        - put all arguments in a new line.
                        """
        self.arguments = None

    def process(self):
        message = [{"role": "user", "content": self.prompt}]
        response = ollama.chat(model="llama3.2", messages=message)
        self.arguments = response['message']['content']
        return self.arguments