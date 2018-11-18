import math
import turtle


class Planet(turtle.Turtle):
    """
    定义行星的类，接收行星以下属性：颜色，半长轴a，半短轴b
    """


    def __init__(self, colour, a, b, s):
        turtle.Turtle.__init__(self)
        self.color(colour)
        self.shape('circle')
        self.ht()
        self.pu()
        self.goto(a + math.sqrt(a ** 2 - b ** 2), 0)
        self.pd()
        self.st()
        self.showturtle()
        self.lt(90)
        self.s = s
        self.long = a
        self.short = b

    def orbit(self, t):
        """利用goto函数以及椭圆的参数方程绘制行星的轨道"""
        c = math.sqrt(self.long ** 2 - self.short ** 2)
        self.goto(self.long * math.cos((t / self.s) / 30) + c,
                  self.short * math.sin((t / self.s) / 30))


#以下是各行星及其参数
sun = Planet('yellow', 0, 0,1)
mercury = Planet('orange', 50, 49.5,10)
venus = Planet('chocolate', 80, 79.5,12)
earth = Planet('blue', 110, 109.5,16)
mars = Planet('red', 150, 149.5,18)
jupiter = Planet('black', 200, 199.2,20)
saturn = Planet('green', 250, 249,24)

planets = [sun, mercury, venus, earth, mars, jupiter, saturn]


def orbit_planets():
    for t in range(1000000):
        for planet in planets:
            planet.orbit(t)

orbit_planets()

turtle.Screen().mainloop()