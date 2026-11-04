from math import sqrt

# находит расстояние между центрами тяжести двух прямоугольников
def cg_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    cx1 = (x1 + x2) / 2
    cy1 = (y1 + y2) / 2

    cx2 = (x3 + x4) / 2
    cy2 = (y3 + y4) / 2

    return sqrt((cx2 - cx1) ** 2 + (cy2 - cy1) ** 2)

def corner_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    top_left = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    bottom_right = sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)

    return top_left + bottom_right

def main():
    print(cg_distance(1, 2, 3, 0, 3, 4, 5, 2))

if __name__ == '__main__':
    main()
