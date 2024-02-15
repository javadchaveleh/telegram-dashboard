import json
from pathlib import Path


def read_json(file):
    with open(file, 'r') as f:
        data = json.load(f)
        return data
    
def write_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

data = read_json(Path('./data/telegram.json'))
data['messeges'] = data['messeges'][:1000]
write_json(data, Path('./data/telegram_short.json'))