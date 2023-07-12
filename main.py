
from utils.translate import Translate

import json

with open(f'config.json', "r", encoding="utf-8") as json_data:
    data = json.load(json_data)

def run() -> None:

    path = data['path']
    code = data['code']

    x = Translate(path, code)

    if not x is None:

      return print("Successfully completed the translation.")
    
    print("Can't find a language to translate")


if __name__ == '__main__': 
    run()
  