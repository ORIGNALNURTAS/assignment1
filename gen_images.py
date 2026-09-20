from PIL import Image, ImageDraw, ImageFilter
import random, math

def wall_scene(path, w=900, h=560):
    # Dusk sky gradient behind the colossal wall silhouette
    img = Image.new("RGB", (w, h))
    top = (28, 26, 38)
    bottom = (140, 60, 52)
    for y in range(h):
        t = y / h
        r = int(top[0] + (bottom[0]-top[0]) * t)
        g = int(top[1] + (bottom[1]-top[1]) * t)
        b = int(top[2] + (bottom[2]-top[2]) * t)
        ImageDraw.Draw(img).line([(0,y),(w,y)], fill=(r,g,b))
    draw = ImageDraw.Draw(img)
    # sun
    draw.ellipse([w*0.72, h*0.18, w*0.72+90, h*0.18+90], fill=(232, 213, 168))
    # wall silhouette
    wall_top = int(h*0.58)
    draw.rectangle([0, wall_top, w, wall_top+70], fill=(24,22,26))
    # crenellations
    step = 40
    for x in range(0, w, step):
        draw.rectangle([x, wall_top-24, x+20, wall_top], fill=(24,22,26))
    # ground
    draw.rectangle([0, wall_top+70, w, h], fill=(16,15,18))
    # small figures on the wall (scouts)
    for x in [120, 260, 520, 700]:
        draw.line([(x, wall_top-24),(x, wall_top-50)], fill=(20,19,22), width=3)
        draw.ellipse([x-4, wall_top-58, x+4, wall_top-50], fill=(20,19,22))
    img = img.filter(ImageFilter.GaussianBlur(0.4))
    img.save(path, quality=90)

def survey_corps_emblem(path, size=700):
    img = Image.new("RGB", (size, size), (232, 223, 200))
    d = ImageDraw.Draw(img)
    cx, cy = size//2, size//2
    r = size*0.34
    # two wings (simplified)
    d.ellipse([cx-r*1.6, cy-r*0.5, cx-r*0.2, cy+r*0.5], outline=(140,31,40), width=10)
    d.ellipse([cx+r*0.2, cy-r*0.5, cx+r*1.6, cy+r*0.5], outline=(43,60,43), width=10)
    d.ellipse([cx-r*0.5, cy-r*0.5, cx+r*0.5, cy+r*0.5], fill=(27,27,31))
    d.ellipse([cx-r*0.28, cy-r*0.28, cx+r*0.28, cy+r*0.28], fill=(232,223,200))
    img.save(path, quality=90)

def training_gear_diagram(path, w=900, h=560):
    img = Image.new("RGB", (w,h), (27,27,31))
    d = ImageDraw.Draw(img)
    cx, cy = w//2, int(h*0.55)
    # simple humanoid figure with ODM gear lines
    d.line([(cx,cy-140),(cx,cy+60)], fill=(232,223,200), width=6) # spine
    d.ellipse([cx-30, cy-190, cx+30, cy-130], outline=(232,223,200), width=5) # head
    d.line([(cx,cy-90),(cx-90,cy-40)], fill=(232,223,200), width=6)
    d.line([(cx,cy-90),(cx+90,cy-40)], fill=(232,223,200), width=6)
    d.line([(cx,cy+60),(cx-60,cy+180)], fill=(232,223,200), width=6)
    d.line([(cx,cy+60),(cx+60,cy+180)], fill=(232,223,200), width=6)
    # gear boxes on hips
    d.rectangle([cx-40, cy+30, cx-10, cy+70], outline=(140,31,40), width=4)
    d.rectangle([cx+10, cy+30, cx+40, cy+70], outline=(140,31,40), width=4)
    # cable arcs
    for i in range(4):
        d.arc([cx-250+i*30, cy-260+i*20, cx-40, cy-40], start=0, end=90, fill=(107,112,92), width=2)
        d.arc([cx+40, cy-260+i*20, cx+250-i*30, cy-40], start=90, end=180, fill=(107,112,92), width=2)
    img.save(path, quality=90)

wall_scene("images/wall-maria-dusk.png")
survey_corps_emblem("images/survey-corps-emblem.png")
training_gear_diagram("images/odm-gear-diagram.png")
print("done")
