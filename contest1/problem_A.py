def solution(x1, y1, x2, y2, x, y):
    options = {
        (x < x1, y < y1): "SW",
        (x < x1, y > y2): "NW",
        (x < x1, y1 <= y <= y2): "W",
        (x > x2, y < y1): "SE",
        (x > x2, y > y2): "NE",
        (x > x2, y1 <= y <= y2): "E",
        (x1 <= x <= x2, y < y1): "S",
        (x1 <= x <= x2, y > y2): "N"
    }
    return options.get((True, True), "")

coords = [int(input()) for _ in range(6)]
x1, y1, x2, y2, x, y = coords

closest = solution(x1, y1, x2, y2, x, y)
print(closest)
