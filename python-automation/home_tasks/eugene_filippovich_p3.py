# -*- coding: utf-8 -*-
import collections


text = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

text_low_case = text.lower()
letters = collections.Counter(text_low_case)

print (letters)

print '\n'

def sortByKey():
    sorted_by_key_letters = sorted(letters.items(), key = lambda t: t[0])
    print sorted_by_key_letters
sortByKey()

for char in letters:
    var = ('%s = %d' % (char, letters[char]))
    print var

print '\n'

for key, value in sorted(
        letters.iteritems(), key=lambda (k, v): (v, k), reverse=True)[:10]:
    print (str(key) + ' = ' + str(value))