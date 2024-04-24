import json
import os
from ollama import generate
import re

class DatasetCreator:
    """
    A class for creating datasets in alpaca style.

    Attributes:
    - model: The model used for generating responses.
    - n_data: The number of data points to generate for each file.
    - initial: The initial line index to start processing data.
    - final: The final line index to stop processing data.
    - system_prompt: The system prompt for generating responses.

    Methods:
    - clean_text: Cleans the text by extracting the JSON portion.
    - generate_dataset: Generates the dataset by processing input files.
    """
    def __init__(self,model,n_data=10,initial=0, final=10):
        self.model = model
        self.n_data = n_data
        self.initial = initial
        self.final = final
        with open("setup_promp\system_prompt.txt", "r") as f:
            self.system_prompt = f.read()

    def clean_text(self, text):
        answer = re.findall(r'\[.*?\]', text, re.DOTALL)
        answer = ''.join(answer)
        return answer
    def generate_dataset(self):
        for file in os.listdir("input_data"):
            print(file)
            file_index = file
            file_index = file_index.replace(".txt", "").replace(".md", "").replace(" ", "_").replace("-", "_")
            if file.endswith(".txt") or file.endswith(".md"):
                while True:
                    with open(f"./input_data/{file}", "r") as f:
                        lines = f.readlines()
                        data = lines[self.initial:self.final]
                    if not data:
                        print("End of file")
                        break
                    print('Processing data on line : ', self.initial," - ", self.final)
                    model = generate(
                        model=self.model,
                        prompt=f"<context>{data}</context>\
                            expect_output = {self.n_data} of set ",
                        system=self.system_prompt
                    )
                    answer = self.clean_text(model['response'])
                    print(answer)
                    try:
                        answer = json.loads(answer)
                        with open(f"./output_data/{file_index}{self.initial}_{self.final}.json", "w") as f:
                            json.dump(answer, f)
                        self.initial += 10
                        self.final += 10
                    except:
                        print("output is not json format")
                        print("retrying...")
                        pass
            

            else:
                print("file is not txt or md")
                break

