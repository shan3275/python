#!/usr/bin/python
#coding:utf-8

def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] < lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    list = [1,3,28, 29,48,21]
    print list
    list = bubble_sort(list)
    print list
