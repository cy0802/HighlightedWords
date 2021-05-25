import json

# word is a list


def insertData(word, filename):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
    with open(filename, 'w') as jsonfile:
        for singleWord in word:
            data["user"][0]['word'].append(singleWord)
        dataStr = json.dump(data, jsonfile)


def select(filename):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
    return data["user"][0]["word"]


if __name__ == '__main__':
    insertData(['affair', 'table', 'fine'], "test.json")
    print(select('test.json'))
