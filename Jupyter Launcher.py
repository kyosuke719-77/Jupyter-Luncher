import os
import json

#ファイルパスはjson形式で読み込み（チルダは使えない、\は/に変更する）
data=open('filepath.json','r', encoding='utf-8')
fp=json.load(data)
path=fp['path']
#ディレクトリを移動して、新規ターミナルを立ち上げてjupyterを起動
os.chdir(path)
os.system('start jupyter notebook')