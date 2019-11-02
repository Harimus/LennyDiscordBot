import json
import random
with open("lenny.json", encoding="utf-8") as fh:
    lenny_parts = json.load(fh)


def random_lenny_face():
    eyes = random.choice(lenny_parts['Eyes'])
    mouth = random.choice(lenny_parts['Mouth'])
    ears = random.choice(lenny_parts['Ears'])
    return ears[0] + eyes[0] + mouth + eyes[1] + ears[1]

