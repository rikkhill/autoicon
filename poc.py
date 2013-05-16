# Proof of concept for autoicon

import json
from PIL import Image, ImageDraw, ImageFont

def nplace(i1, array):
    try:
        base = Image.open("./icons/%s.png" % (i1));
    except IOError:
        return False

    try:
        imj = json.load(open("./icons/%s.val" % (i1)))
    except IOError:
        return base
    places = []
    for i in imj:
        if i.isnumeric():
            places.append(int(i))

    places.sort()

    if len(array) in places:
        count = 1
        for i in array:
            dat = imj[str(len(array))]
            tick = str(count)
            box = (int(dat[tick]['x']), int(dat[tick]['y']), int(dat[tick]['x']) + int(dat[tick]['size']), int(dat[tick]['y']) + int(dat[tick]['size']))
            if type(i) == str:
                stamp = Image.open("./icons/%s.png" % (i))
            else:
                stamp = i
            base.paste(stamp.resize((int(dat[tick]['size']),int(dat[tick]['size']))), (int(dat[tick]['x']), int(dat[tick]['y'])))
            count +=1 # This is not pythonic
    else:
        return base

    return base
        

def oneplace(i1, i2):
    base = Image.open("./icons/%s.png" % (i1))
    imj = json.load(open("./icons/%s.val" % (i1)))

    if type(i2) == str:
        i2 = Image.open("./icons/%s.png" % (i2))

    dat = imj['1']
    box = (int(dat['1']['x']), int(dat['1']['y']), int(dat['1']['x']) + int(dat['1']['size']), int(dat['1']['y']) + int(dat['1']['size']))
    base.paste(i2.resize((int(dat['1']['size']),int(dat['1']['size']))), (int(dat['1']['x']), int(dat['1']['y'])))

    return base


def twoplace(i1, i2, i3):
    base = Image.open("./icons/%s.png" % (i1))
    imj = json.load(open("./icons/%s.val" % (i1)))

    if type(i2) == str:
        i2 = Image.open("./icons/%s.png" % (i2))
    if type(i3) == str:
        i3 = Image.open("./icons/%s.png" % (i3))

    dat = imj['2']
    box1 = (int(dat["1"]['x']), int(dat["1"]['y']), int(dat["1"]['x']) + int(dat["1"]['size']), int(dat["1"]['y']) + int(dat["1"]['size']))
    box2 = (int(dat["2"]['x']), int(dat["2"]['y']), int(dat["2"]['x']) + int(dat["2"]['size']), int(dat["2"]['y']) + int(dat["2"]['size']))
    base.paste(i2.resize((int(dat["1"]['size']),int(dat["1"]['size']))), (int(dat["1"]['x']), int(dat["1"]['y'])))
    base.paste(i3.resize((int(dat["2"]['size']),int(dat["2"]['size']))), (int(dat["2"]['x']), int(dat["2"]['y'])))
    
    return base

def charim(char):
    im = Image.new("RGBA", (300,300))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("resources/cambriai.ttf", 250)
    draw.text((80, 0), char, (0,0,0), font=font)
    return im
    
    

f1 = 'eye'
f2 = 'dot'
f3 = 'gear'
f4 = 'scale'
f0 = 'square'

#im = nplace('matrix', ['gear', oneplace('eye', 'gear'), oneplace('eye', charim('Q')), 'brain'])
im = nplace('eye', [oneplace('gear', 'dot')])



im.save("monster.png")
#eye = oneplace(f1,f2)
#gear = oneplace(f3, eye)

#getter = twoplace(f4, eye, gear)
#supes = oneplace('eye', 'brain')
#supes.save("monster.png");

#getter = oneplace(f1,f3)
#getter = oneplace(f3, getter)
#getter.save('temp.png');
