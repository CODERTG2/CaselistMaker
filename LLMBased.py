import subprocess
import json

class LLMBased:
    def __init__(self, text):
        self.disclosure = text
        self.prompt = """
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
        prompt = f"""All the arguments:
                        {self.disclosure}
                        {self.prompt}"""
        try:
            command = [
                "ollama", "run", "llama3.2", 
                prompt
            ]
            
            result = subprocess.run(
                command, 
                capture_output=True, 
                text=True, 
                timeout=120
            )
            
            if result.returncode == 0:
                self.arguments = result.stdout.strip()
                return self.arguments
            else:
                return f"Ollama command failed: {result.stderr}"
                
        except subprocess.TimeoutExpired:
            return "LLM processing timed out (2 minutes)"
        except FileNotFoundError:
            return "Ollama is not installed or not in PATH. Please install ollama first."
        except Exception as e:
            return f"LLM processing error: {str(e)}"