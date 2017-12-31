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

my_email = "\neugene_filippovich93@gmail.com"
concatenate = text + my_email

print len(concatenate)

count = 0

string = concatenate.lower()

for char in string:
    if char in 'aeyuio':
        count += 1

print count

case = concatenate.swapcase()

for i in range(17,len(concatenate),18):
    print i+1, case[i]
