import math
from PIL import Image
from PIL import ImageDraw

def binomial_coefficient(n, k):
    if k == 1: return n

    n_factorial = 1
    for x in range(1, n):
        n_factorial += n_factorial * x

    k_factorial = 1
    for x in range(1, k):
        k_factorial += k_factorial * x

    nk_factorial = 1
    for x in range(1, n - k):
        nk_factorial += nk_factorial * x

    return n_factorial/(k_factorial*nk_factorial)

def bernstein(n, i, t):
    return binomial_coefficient(n, i) * math.pow(t, i) * math.pow(1 - t, n - i)

def bezier_curve(points, steps):
    n = len(points) - 1
    result = []

    # calculate curve point for t
    def point(t):
        x = 0
        y = 0
        for i in range(0, n + 1):
            x += points[i][0] * bernstein(n,i,t)
            y += points[i][1] * bernstein(n,i,t)
        return (x, y)

    # steps for t from 0 to 1
    for x in range(0, steps+1):
        t = x * (1.0/steps)
        result.append( point(t) )
    
    return result

img_size = 475
img = Image.new("RGB", (img_size, img_size))
draw = ImageDraw.Draw(img)

draw.rectangle([0,0,img_size, img_size], fill="#fff")

k = [
    bezier_curve([(10, 10), (50, 10)], 100),
    bezier_curve([(10, 10), (10, 400)], 100),
    bezier_curve([(10, 400), (50, 400)], 100),
    bezier_curve([(50, 10), (50, 150)], 100),
    bezier_curve([(50, 400), (50, 250)], 100),
    bezier_curve([(50, 250), (150, 400)], 100),
    bezier_curve([(150, 400), (200, 400)], 100),
    bezier_curve([(50, 150), (150, 10)], 100),
    bezier_curve([(150, 10), (200, 10)], 100),
    bezier_curve([(200, 10), (65, 200)], 100),
    bezier_curve([(65, 200), (200, 400)], 100),
]

for x in k:
    draw.line(x, fill="#000", width=2)

z = [
    bezier_curve([(250, 10), (470, 10)], 100),
    bezier_curve([(250, 10), (250, 50)], 100),
    bezier_curve([(250, 50), (400, 50)], 100),
    bezier_curve([(400, 50), (250, 400)], 100),
    bezier_curve([(250, 400), (450, 400)], 100),
    bezier_curve([(450, 400), (450, 360)], 100),
    bezier_curve([(450, 360), (320, 360)], 100),
    bezier_curve([(320, 360), (470, 10)], 100),
    bezier_curve([(270, 200), (440, 200)], 100),
    bezier_curve([(270, 230), (440, 230)], 100),
    bezier_curve([(270, 230), (270, 200)], 100),
    bezier_curve([(440, 200), (440, 230)], 100),
]

for x in z:
    draw.line(x, fill="#000", width=2)

img.show()