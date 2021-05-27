import json

# word is a list


def insertData(word, filename):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
    dataSet = set(word) - set(data["user"][0]['word'])
    dataList = list(dataSet)
    with open(filename, 'w') as jsonfile:
        for singleWord in dataList:
            data["user"][0]['word'].append(singleWord)
        data["user"][0]['word'].sort()
        dataStr = json.dump(data, jsonfile)


def select(filename):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
    return data["user"][0]["word"]


if __name__ == '__main__':
    insertData(['dissent', 'autonomy', 'add'], "test.json")
    print(select('test.json'))
