
from typing import Dict, List, Literal

from .cache import makedirs

translate_code = [
    'en',
    'zh-CN',
    'zh-TW',
    'fr',
    'de',
    'it',
    'ja',
    'ko',
    'pl',
    'pt',
    'ru',
    'es',
    'vi',
]

def Translate(original_path: str, locle_code: Literal['de', 'en', 'es', 'fr', 'it', 'ja', 'ko', 'pl', 'pt', 'ru', 'vi', 'zh-CN', 'zh-TW']
) -> Dict:
    """JSON DATA"""

    if not locle_code in translate_code:
        return None
    
    import json

    with open(f'{original_path}', "r", encoding="utf-8") as json_data:
        data = json.load(json_data)

    data = _math_data(data, locle_code)

    path = f'languages/{locle_code}.json'

    makedirs(path)

    with open(path, "w", encoding="utf-8") as json_data:
        json.dump(data, json_data, indent=2, ensure_ascii=False)

    return data


def _googletrans(text: str, locale_code: str) -> str:

    from googletrans import Translator

    translator = Translator()

    print('->', text)

    translated = translator.translate(text, dest=locale_code)

    x = translated.text

    if "{" in x and "}" in x:
        
        import re

        ww_x = re.findall(r'{(.*?)}', text)

        ww_o = re.findall(r'{(.*?)}', x)

        if len(ww_o) == len(ww_x):

          for i in range(len(ww_x)):

            x = x.replace(ww_o[i], ww_x[i])

    return x

def _spend_list(formats: Dict, locle_code: str) -> List:

    data = []

    for x in formats:

        if isinstance(x, dict):
            data.append(_math_data(x, locle_code))

        elif isinstance(x, list):
            data.append(_spend_list(x, locle_code))

        elif isinstance(x, str):
            data.append(_googletrans(x, locle_code))
        else:
            data.append(x)

    return data



def _math_data(formats: Dict, locle_code: str) -> Dict:

    data = {}

    for x in formats:

        key = formats[x]

        if key == '':
            data[x] = ''
        elif isinstance(key, dict):
            data[x] = _math_data(key, locle_code)
        elif isinstance(key, list):
            data[x] = _spend_list(key, locle_code)
        elif isinstance(key, str):
            data[x] = _googletrans(key, locle_code)
        else:
            data[x] = key

    return data
