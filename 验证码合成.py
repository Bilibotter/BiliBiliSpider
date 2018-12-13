from PIL import Image
import re


def get_px():
    res = []
    with open('html.txt', 'r')as f0:
        html = f0.read()
    pattern = 'background-position:.*?;'
    pxs = re.findall(pattern, html)
    reps = ['background-position:', ';', ' ']
    for px in pxs:
        for rep in reps:
            px = px.replace(rep, '')
        px = abs(int(px.split('px')[0]))
        res.append(px)
    return res


jpg = Image.open('bilibili6.jpg')
captcha = Image.open('bilibili6.jpg')
res = get_px()
begin = 1
start0 = 58
start1 = 0
for num, px in enumerate(res):
    if num == 26:
        begin = 1
        start0, start1 = start1, start0
    span = 11 if px != 301 else 10
    box0 = (px, start0, px+span, start0+58)
    box1 = (begin, start1, begin+span, start1+58)
    block = jpg.crop(box0)
    captcha.paste(block, box1)
    begin += span-1
captcha = captcha.crop((1, 0, begin+1, 116))
captcha.show()
captcha.save('success5.jpg')
