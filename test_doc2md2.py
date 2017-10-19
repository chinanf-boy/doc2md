# -*- coding: utf-8 -*-
from doc2md2 import is_en_zh
from doc2md2 import is_zh


# import path, sys
# import folder = path.path(__file__).abspath()
# sys.path.append(folder.parent.parent) 
def test_en_zh():
    assert is_en_zh(u"你好") <= 0
    assert is_en_zh(u"你好asdfsdf") > 0
    assert is_en_zh(u"helloworld 你好") > 0

def test_zh():
    assert is_zh(u"你好") is True
    assert is_zh(u"helloworld") is False
    assert is_zh(u"你helloworld好") is False

    



