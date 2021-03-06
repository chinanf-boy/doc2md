# doc2md

[![Build Status](https://travis-ci.org/chinanf-boy/doc2md.svg?branch=master)](https://travis-ci.org/chinanf-boy/doc2md)

本意是为了

像

---

``` py
倒序
for color in sorted(colors, reverse=True):
    print colors

自定义排序顺序

colors = ['red', 'green', 'blue', 'yellow']

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print sorted(colors, cmp=compare_length)

更好的方法

print sorted(colors, key=len)

第一种方法效率低而且写起来很不爽。另外，Python 3已经不支持比较函数了。

调用一个函数直到遇到标记值

blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)
```
# 变成 下面 markdown 格式
``` py
# 倒序
for color in sorted(colors, reverse=True):
    print colors

```
自定义排序顺序

``` py
colors = ['red', 'green', 'blue', 'yellow']

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print sorted(colors, cmp=compare_length)

```
更好的方法

``` py
print sorted(colors, key=len)

```
第一种方法效率低而且写起来很不爽。另外，Python 3已经不支持比较函数了。

调用一个函数直到遇到标记值

``` py
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

```

---

## 运行文件是 ``main/doc2md.py``

一步一步过程 可以使用``jupyter notebook`` 查看 ``doc2md.ipynb``

首先说明缺陷就是，命令行还没有做
请自己进入文件修改先。
``` py
Path = "../让你的Python优雅.md"
write_file = '../test_w.md'
```


## demo 就是

``` py
python doc2md.py file1
```
> 获取 ``让你的Python优雅.md``

> md格式``写``入 ``test_w.md``

