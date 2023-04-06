#!/usr/bin/env python3
""" Main file """
import time

get_page = __import__('web').get_page


print(get_page)
print(get_page('google'))
print('sleep .1')
time.sleep(.1)
print(get_page('google'))
print(get_page('micro'))
print('sleep .1')
time.sleep(.1)
print(get_page('micro'))
print(get_page('google'))

print('sleep 10')
time.sleep(10)
print(get_page('google'))
print(get_page('micro'))

print(get_page('google'))
print(get_page('google'))
