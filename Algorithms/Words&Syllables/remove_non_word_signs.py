# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import re
from faker import Faker

# ---

fake = Faker()
text = 'and IBM’s newly-announced partnership with UFC 2024.'


# ### Remove non word signs

def removeNonWordSigns(text: str) -> str:
    text = text.replace('-', ' ')
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w]+\w\b', '', text, flags=re.UNICODE) # 's
    text = re.sub(r'[^\w\s]', '', text)
    return text.replace('\n', ' ')

# + active=""
# print(removeNonWordSigns(text))
