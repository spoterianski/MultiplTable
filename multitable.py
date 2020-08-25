import os
import sys
import random
import re
import datetime
import json


def get_answer(a, b):
    answ = ''
    rdigs = re.compile('^[0-9]+$')
    answ = input("{} х {} = ".format(a, b))
    while not rdigs.match(answ):
        print("Введи ответ в виде числа и нажми Ввод")
        answ = input("{} х {} = ".format(a, b))
    return int(answ)
    

def save_result(tnums, results, score, percent):
    if not os.path.exists('./results'):
        os.mkdir('./results')
    dt = datetime.datetime.now()
    fname = 'multitab-' + dt.strftime('%Y%m%d-%H%M%S') + '.txt'
    f = open(os.path.join('./results', fname), 'w')
    f.write("проверяем знания на: {}\n".format(', '.join(tnums)))
    f.write("результат\n\n")

    f.write(json.dumps(results, indent=4, sort_keys=True))
    f.write("\n\n")

    f.write("score: {}\n".format(score))
    f.write("percent: {}\n".format(percent))

# def make_tasks(data, tnums, cnt):

def main():

    cnt = 10
    if len(sys.argv) >= 2:
        try:
            cnt = int(sys.argv[1])
        except:
            cnt = 10

    digs = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    results = []

    print('Привет!')
    print('Давай изучать таблицу умножения :)')
    val = input("Введи через запятую цифры на которые будет проверять знания таблицы умножения: ") 
    tnums = val.split(',')
    print("Отлично, проверяем знания на: {}".format(', '.join(tnums)))
    print("Начали, вводи ответ и нажимай Ввод")
    total_cnt = cnt * len(tnums)
    for _ in range(1, total_cnt):
        rnd_d = random.randint(0, len(digs) - 1)
        rnd_i = random.randint(0, len(tnums) - 1)
        a = int(digs[rnd_d])
        b = int(tnums[rnd_i])
        answ = get_answer(a, b)
        if a * b == answ:
            print("Верно!")
        else:
            print("Правильный ответ: {}".format(a * b))
        right_answer = (a * b == answ)
        # print(right_answer)
        results.append(
            {'a': a, 'b': b, 'r': answ, 'ok': right_answer}
        )
    
    # print score
    total = len(results)
    score = 0
    for item in results:
        if(item['ok']):
            print("{} x {} = {} - молодец!".format(item['a'], item['b'], item['a']))
            score += 1
        else:
            print("{} x {} != {}, правильный ответ: {}".format(item['a'], item['b'], item['r'], item['a'] * item['b']))
    percent = score / total * 100.0
    user_score2 = int((score / total * 5.0) + 0.5)
    print("Твоя оценка: {}".format(user_score2))
    save_result(tnums, results, score, percent)


if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
