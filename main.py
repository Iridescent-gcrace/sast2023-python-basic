import argparse
import json
import random
import re


nouns = ["人", "狗", "花", "山", "水", "风"]
verbs = ["跑", "吃", "睡", "看", "听", "玩"]
adjectives = ["美丽", "快乐", "悲伤", "高兴", "聪明", "勇敢"]
adverbs = ["快速地", "慢慢地", "高兴地", "难过地", "认真地"]

pos_dict = {
    "名词": nouns,
    "动词": verbs,
    "形容词": adjectives,
    "副词": adverbs,
}

def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    # TODO: 添加更多参数
    parser.add_argument("-w", "--which", help="指定哪一篇文章", required=False)
    args = parser.parse_args()
    return args



def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    try:
        with open(filename, 'r', encoding="utf-8") as f:  
            # TODO: 用 json 解析文件 f 里面的内容，存储到 data 中
            file_content = f.read()  # 读取文件内容为字符串

        data = json.loads(file_content)
    except Exception as e :
        print(f"发生错误：{e}")
        return None
    return data

# def find_max_placeholder_index(article):
#     """
#     查找文章中所有 {{i}} 形式的字符串，并得到最大的 i 值

#     :param article: 文章内容

#     :return: 最大的 i 值，如果没有找到 {{i}} 形式的字符串，返回 0
#     """
#     pattern = r"\{\{(\d+)\}\}"
#     matches = re.findall(pattern, article)

#     if matches:
#         max_index = max(int(index) for index in matches)
#         return max_index
#     else:
#         return 0

def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        print(hint)
            
        user_input = input()
        keys.append(user_input)

    return keys


def replace(article, keys):
    """
    替换文章内容

    :param article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    for i in range(len(keys)):
        # TODO: 将 article 中的 {{i}} 替换为 keys[i]
        # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换
        article = article.replace("{{" + str(i + 1) + "}}", keys[i])

    return article


if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]
    articles_num = len(data["articles"])
    article = None
    hints = None
    # TODO: 根据参数或随机从 articles 中选择一篇文章
    if args.which is None:
        rng = random.randint(0,articles_num)
        article = data["articles"][rng]["article"]
        hints = data["articles"][rng]["hints"]
    else:
        for i in data["articles"]:
            if i["title"] == args.which:
                article = i["article"]
                hints = i["hints"]
                break

    # TODO: 给出合适的输出，提示用户输入

    keys = get_inputs(hints=hints)
    # TODO: 获取用户输入并进行替换
    article = replace(article=article,keys=keys)
    # TODO: 给出结果
    print(article,)


