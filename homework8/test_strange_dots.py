import strange_dots

a = strange_dots.Dots(0,40)
print(*a[5])
print(a[0:5])
print(a[2:5])
print(a[4:5])
print(a[7:5])
print(a[-7:5])
print(*a[1:3:5])
print(*a[:3:5])
print(*a[2::5])
print(*a[::5])
print(*a[-2:6:5])
