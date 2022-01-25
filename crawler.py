import requests
from bs4 import BeautifulSoup


def Translate(words):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    data = []
    worddata = []
    for i in words:
        url1 = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/' + \
            i
        #url1 = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'+'test'
        url = requests.get(url1, headers=headers)
        url.encoding = "utf-8"
        soup = BeautifulSoup(url.text, "html.parser")

        _word = soup.find(class_='hw dhw')

        # 找到詞性
        part_of_speech = soup.find_all(
            "div", class_="posgram dpos-g hdib lmr-5")
        if part_of_speech == []:
            continue
        worddata = [_word.getText()]
        # 尋找每個詞性對應的中文解釋
        for j in part_of_speech:
            # data_part_of_speech dictionary
            dpos = {'name': '',  # 詞性
                    'audio': [],  # 音檔
                    'translate': [],  # 解釋
                    }
            # 輸出該詞性
            tmp = j.getText()
            dpos['name'] = tmp  # print("詞性:" + tmp)
            # 尋找該詞性的parent
            result = j.select_one("span").find_parent(
                "div").find_parent("div").find_parent("div")
            # 尋找單字音檔
            audio = result.find_all("source", type="audio/mpeg")
            url_audio_US = audio[0].get("src").replace('/', '=', 8)
            url_audio_UK = audio[1].get("src").replace('/', '=', 8)
            dpos['audio'].append(url_audio_US)  # print('US : ' + url_audio_US)
            dpos['audio'].append(url_audio_UK)  # print('UK : ' + url_audio_UK)
            # 用class尋找中文解釋
            translate = result.find_all("div", class_="def-body ddef_b")
            # 更新次數
            times = 1
            for k in translate:
                # 排除片語的中文解釋
                if k.find_parent("div", class_="pr phrase-block dphrase-block") == None:
                    mean = k.select_one(
                        "span", class_="trans dtrans dtrans-se  break-cj").getText()
                    # print("解釋" + str(times) + ":" + mean, end='')
                    dpos['translate'].append(mean)
                    times += 1
            worddata.append(dpos)
        data.append(worddata)
    return data


if __name__ == "__main__":
    word = ['test', 'exclaimed', 'ragged', 'revive']
    returned = Translate(word)
    print(returned)
