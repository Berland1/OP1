a = int(input('Введите точку "a" : '))
b = int(input('Введите точку "b" : '))
R = int(input('Введите радиус : '))
def inside(x, y , a, b, R):
    distance = (x - a)**2 + (y - b)**2
    if distance < 2 * R:
        return True
    else:
        return False
Px = int(input('Введите координату x точки "P" : '))
Py = int(input('Введите координату y точки "P" : '))
Fx = int(input('Введите координату x точки "F" : '))
Fy = int(input('Введите координату y точки "F" : '))
Lx = int(input('Введите координату x точки "L" : '))
Ly = int(input('Введите координату y точки "L" : '))
points_inside = 0
if inside(Px, Py, a, b, R):
    points_inside += 1
if inside(Fx, Fy, a, b, R):
    points_inside += 1
if inside(Lx, Ly, a, b, R):
    points_inside += 1
print(f'Количетсво точек, лежащих внутри окружности : {points_inside}')