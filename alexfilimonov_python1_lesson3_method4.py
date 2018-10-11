def ifparalelogram(x,y):
#ищем координаты середин диагноналей. Если они совпали, то это параллелограмм (свойство параллелограммов)
#например, параллелограммом будет 0 4 5 1 0 0 3 3
    xc1 = ((x[0] + x[2])/ 2)
    xc2 = ((x[1] + x[3])/ 2)
    yc1 = ((y[0] + y[2])/ 2)
    yc2 = ((y[1] + y[3])/ 2)
    if  xc1 == xc2 and yc1 == yc2 : 
        return "This is parallelogram!"
    else :
        return "This is NOT parallelogram!"
print("Please enter coordinates of possible parallelogram by circle!") 
x1 = int(input("x1:"))
x2 = int(input("x2:"))
x3 = int(input("x3:"))
x4 = int(input("x4:"))
y1 = int(input("y1:"))
y2 = int(input("y2:"))
y3 = int(input("y3:"))
y4 = int(input("y4:"))

x = [x1,x2,x3,x4]
y = [y1,y2,y3,y4]
print(ifparalelogram(x,y)) 
