class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def subtraction(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def multiplication(self, scalyar):
        if scalyar >= 0:
            return Vector(self.x * scalyar, self.y * scalyar)
        else:
            return Vector(self.y * scalyar, self.x * scalyar)

    def __str__(self):
        return f'{self.x}, {self.y}'


vector1 = Vector(5, 7)
vector2 = Vector(12, 9)
vector3 = Vector(-2, -5)


print(vector1)
print(vector2)
print(vector3)
