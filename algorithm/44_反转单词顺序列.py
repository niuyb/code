#!/usr/bin/env python
# encoding: utf-8
# 作者：Ksar4
# 日期：2021/3/1 10:07
# 工具：PyCharm
# Python版本：3.7.0

# python 2
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# python 3
# import sys
# import importlib
# importlib.reload(sys)
""""""


"""
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
正确的句子应该是“I am a student.”

"""


"""
input:   "nowcoder. a am I"

:return  "I am a nowcoder."

"""


class Solution:
    def ReverseSentence(self, s):
        if not s:
            return s
        l = s.split()
        if len(l) == 0:
            return s

        l.reverse()
        new_s = ' '.join(l)
        return new_s

    def self_ReverseSentence(self,s):
        if not s:
            return s
        l = s.split()
        if len(l) == 0:
            return s
        # l = l[::-1]
        return " ".join(l[::-1])






if __name__ == "__main__":

    s = Solution()
    s_str = s.self_ReverseSentence("nowcoder. a am I")
    print(s_str)






