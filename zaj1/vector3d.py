from Math import sqrt

class Vector3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y
    
    def set_z(self, z):
        self._z = z

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_z(self):
        return self._z
    
    def norm(self):
        return sqrt(self._x**2 + self._y**2 + self._z**2)
    
    def dot(self, other):
        return self._x * other.get_x() + self._y * other.get_y() + self._z * other.get_z()

    def cross(self, other):
        return Vector3D(self._y * other.get_z() - self._z * other.get_y(), self._z * other.get_x() - self._x * other.get_z(), self._x * other.get_y() - self._y * other.get_x())

    def __add__(self, other):
        return Vector3D(self._x + other.get_x(), self._y + other.get_y(), self._z + other.get_z())

    def __sub__(self, other):
        return Vector3D(self._x - other.get_x(), self._y - other.get_y(), self._z - other.get_z())

    def __mul__(self, scalar):
        return Vector3D(self._x * scalar, self._y * scalar, self._z * scalar)

    def __str__(self):
        return f'({self._x}, {self._y}, {self._z})'

    @staticmethod
    def are_orthogonal(v1, v2):
        return v1.dot(v2) == 0
