import time
a = input('想说的话：')
with open(f'./diary/{str(time.strftime("%Y%m%d%H%M%S"))}', 'w') as f:
    content = bytes(a, encoding='utf-8')
    f.write(str(content))
