math = input('Expression: ')
x,y,z = math.split()
x = float(x)
z = float(z)
if y == '+':
    ans = x + z
elif y == '-':
    ans = x - z
elif y == '/':
    ans = x / z
else:
    ans = x * z
ans = round(ans,1)
print(ans)