# 自分用メモ macではvenvで仮想環境から実行する
import requests
import sys
from bs4 import BeautifulSoup

def extract_h3_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # h3要素を全て取得します
    h3_tags = soup.find_all('h3')

    # h3要素を子に持つ親要素を抽出します
    parents = [tag.parent for tag in h3_tags]

    # 親要素を表示します
    for parent in parents:
        print(f'## {parent.h3.text}')
        for p in parent.find_all('p'):
            text = p.text.replace("http","\nhttp")
            print(f'{text}\n')


def main():
    args = sys.argv
    extract_h3_text(args[1])

if __name__ == "__main__":
    main()

