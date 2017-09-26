import re
import os

global py_is
py_is = False

# 全局 代码区域定义


def py_is_fun(vv):
    global py_is
    if vv == '``` py':
        py_is = True

    elif vv == '```':
        py_is = False


def input_w(file, value):
    file.write('\n' + value + '\n')


input_value = {
    'h2': "## ",
    'start_tcode': "``` py\n",
    'end_code': '```\n'
}

Path = "../让你的Python优雅.md"
mkfileopen = open(Path)
lines = mkfileopen.readlines()
mkfileopen.close()
# 获得 文本文字

# 不需要改变，直接写入,开头匹配
res = [r"``` py", r"更好的方法", r"#", r"```", r'---', '<!-- more -->']
# 匹配中文


def is_zh(line):
    xx = u"([\u4e00-\u9fff]+)"
    pattern = re.compile(xx)
    results = pattern.findall(line)
    return bool(results)
# 匹配中英文


def is_en_zh(line):
    xx = u"([\w\W]+[\u4e00-\u9fff]+)"
    pattern = re.compile(xx)
    results = pattern.findall(line)
    return len(results)


match_value_s = []

for k, line in enumerate(lines):
    for re_value in res:

        if line.isspace():
            # \n 换行 直接 插入
            match_value_s.append(line)
            print('直接原文空格\n',)
            break

        match_value = re.match(re_value, line.strip(), re.M | re.I)

        if match_value:

            # 代码开始—结束的区域固定
            # ``` py
            # ```
            if py_is and re_value == r'``` py':
                match_value_s.append(input_value['end_code'] + line)
                print('两个```py 代码', line)
                py_is_fun('```')
                break
            elif re_value == r'``` py':
                py_is_fun(re_value)
                match_value_s.append(line)
                print('本来开始代码', line)
                break
            elif re_value == r'```':
                match_value_s.append(line)
                print('本来结束代码', line)
                py_is_fun('```')
                break
            elif py_is:
                match_value_s.append(input_value['end_code'] + line)
                print('其他白名单前代码闭合', line)
                py_is_fun('```')
                break
            else:
                match_value_s.append(line)
                print('原文白名单', line)
                break

    else:

        # 有中文有英文，不做处理
        # 多个中文片段
        if is_en_zh(line) is not 0 or is_zh(line) > 1:
            if py_is:
                match_value_s.append(input_value['end_code'] + line)
                py_is_fun('```')
                print('end', line)

            else:
                match_value_s.append(line)
                print('原本中文或英文不用加', line)

        # 单个中文片段，加 h2
        elif is_zh(line) and is_zh(line) <= 1:
            if py_is:
                match_value_s.append(
                    input_value['end_code'] + input_value['h2'] + line)
                py_is_fun('```')
                print('加h2+end', line)

            else:
                match_value_s.append(input_value['h2'] + line)
                print('加h2', line)
        # 默认
        elif py_is == False:

            match_value_s.append(input_value['start_tcode'] + line)
            py_is_fun('``` py')
            print('start', str(k), repr(line))

        else:
            match_value_s.append(line)
            print('默认原文', line)


write_file = '../test_w.md'

file = open(write_file, 'w+')

all = ''
for i in match_value_s:
    file.write(i)

file.close()
print('{} file is create markdown from {}'.format(write_file, Path))
