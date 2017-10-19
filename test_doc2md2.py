from doc2md2 import *

# import path, sys
# import folder = path.path(__file__).abspath()
# sys.path.append(folder.parent.parent) 
def test_en_zh():
    assert is_en_zh("你好") <= 0
    assert is_en_zh("你好asdfsdf") > 0
    assert is_en_zh("helloworld 你好") > 0

def test_zh():
    assert is_zh("你好") is True
    assert is_zh("helloworld") is False
    assert is_zh("你helloworld好") is False

    



