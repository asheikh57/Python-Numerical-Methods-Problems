from math import pi

def closestRectangle(radius: float, rect_side_a: float):
    circleArea = radius * radius * pi
    b, rectArea = 0, 0
    while(rectArea < circleArea):
        b += 1
        rectArea = b * rect_side_a

    return b-1

if __name__ == "__main__":
    print(closestRectangle(10.6, 1.3))