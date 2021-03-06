import math
class rectangle():
    def __init__(self,width,height):
        self.square=width*height
    
class square(rectangle):
    def __init__(self,sideLine):
        self.square=sideLine**2

class ellipse(rectangle):
    def __init__(self,width,height):
        self.square=math.pi*width*height

class circle(ellipse):
    def __init__(self,radius):
        self.square=math.pi*radius**2

def compute_area(list):
    sum=0
    for i in list:
        sum+=i.square
        #print(i.square)
    return sum

shapes=[ellipse(10,20),square(15),circle(5),rectangle(20,15),circle(5),square(15),ellipse(10,20)]
total_area=compute_area(shapes)
print('%.2f'%total_area)   
