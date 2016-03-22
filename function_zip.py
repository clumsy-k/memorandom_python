#! /usr/bin/env python
# encoding:utf-8

# 要素10のlistを2つ作成
List1 = []
List2 = []

for i in xrange(10):
    List1.append(i)
    List2.append(i)

List2.reverse()
Last_list = []

for (a, b) in zip(List1, List2):
    print a, b
    elm = a + b
    Last_list.append(elm)

print Last_list
