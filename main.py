from loguru import logger

import requests
import json
import os


logger.info("Запрос: ")
name = input()

if not name: filename = "result/NONE_name.txt"
else: filename = f"result/{name}.txt"

if not os.path.isdir("result/"):
    os.mkdir("result/")

with open(filename, "w", encoding="utf-8") as file: pass

offset = 0
count_tag = 0
http = requests.Session()
while True:
    answer = http.get(f"https://combot.org/api/chart/all?limit=50&offset={offset}&q={name}",
                 headers={
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
                    'x-requested-with': 'XMLHttpRequest'})

    try:
        result = json.loads(answer.text)
    except:
        continue

    if not result:
        break
    else:
        for tg in result:
            # Можно поставить фильтр языков
            '''logger.info(tg['l']) 
            if tg["l"] == "RU":
                continue'''
            count_tag += 1
            tag = tg['u']
            with open(filename, "a", encoding="utf-8") as file:
                file.write("t.me/" + tag + "\n")
        logger.debug(f"+{len(result)}")
    offset += 50

logger.success(f"Count tags: {count_tag}\n")

os.system("pause")
