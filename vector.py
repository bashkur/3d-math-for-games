import math

class Vector:
    """
    This is a base, general purpose Vector class.
    """
    def __init__(self, *args):
        """
        The constructor
        :param args: scalars to create a vector like this:
                v = Vector(1, 2, 3)
        """
        self.mData = []
        for value in args:
            self.mData.append(float(value))
        self.mDim = len(self.mData)

    def __str__(self):
        """
        :return: The string representation of this vector. Format:
                <Vector2: -0.3, 1.9> or <Vector3: 2.9, 0.1, -2.4)
        """
        s = f'Vector{len(self)}: '
        for i in range(len(self)):
            s += f'{str(round(self.mData[i], 1))}'
            if i < len(self) - 1:
                s += ', '
        s += '>'
        return s

    def __len__(self):
        """
        :return: The dimension of this vector.
        """
        return self.mDim

    def __getitem__(self, index):
        """
        Allows square bracket [] access to items in this vector like this:
            v = Vector(1, 2, 3)
            print(v[0])     # 1
            print(v[-1])    # 3
        :param index: an integer
        :return: the float value at the given index
        """
        return self.mData[index]

    def __setitem__(self, index, value):
        """
        Allows assigning values to this vector via square brackets []. Example:
            v = Vector(1, 2, 3)
            v[0] = 5
            print(v)        # <Vector3: 5, 2, 3>
        :param index: an integer
        :param value: a float
        :return: None
        """
        self.mData[index] = float(value)

    def __eq__(self, other):
        """
        Check if two vectors are equal by comparing their contents.
        This method gets called when a vector is on the left-hand-side of ==.
        :param other: any value to compare to
        :return: a boolean. True if other is a Vector and contents are the same as this Vector. False otherwise.
        """
        if isinstance(other, Vector) and len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        else:
            return False

    def copy(self):
        """
        Creates a deep copy of this vector and returns it.
        :return: a new vector that is a deep copy of this vector
        """
        v = Vector(*self.mData)
        # Ensure the new vector is the same type as the original vector.
        # This is important for specialized vectors like Vector2 and Vector3.
        v.__class__ = self.__class__
        return v

    @property
    def i(self):
        """
        :return: a tuple of all elements contained in this vector, converted to integers (useful in PyGame)
        """
        L = []
        for v in self.mData:
            L.append(int(v))
        return tuple(L)



class Vector2(Vector):
    """
    This is a specialization of the Vector, representing a 2-dimensional vector.
    """
    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def x(self):
        return self.mData[0]

    @x.setter
    def x(self, value):
        self.mData[0] = float(value)

    @property
    def y(self):
        return self.mData[1]

    @y.setter
    def y(self, value):
        self.mData[1] = float(value)

    @property
    def radians(self):
        """
        Calculates the radians of this Cartesian vector in Polar space.
        :return: float
        """
        return math.atan2(self.mData[1], self.mData[0])
    
    @property
    def degrees(self):
        """
        Calculates the degrees of this Cartesian vector in Polar space.
        :return: float
        """
        return math.degrees(math.atan2(self.mData[1], self.mData[0]))



class Vector3(Vector):
    """
    This is a specialization of the Vector, representing a 3-dimensional vector.
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @property
    def x(self):
        return self.mData[0]

    @x.setter
    def x(self, value):
        self.mData[0] = float(value)

    @property
    def y(self):
        return self.mData[1]

    @y.setter
    def y(self, value):
        self.mData[1] = float(value)

    @property
    def z(self):
        return self.mData[2]

    @z.setter
    def z(self, value):
        self.mData[2] = float(value)

def polar_to_vector2(radians, hypotenuse):
    """
    :param radians: radian value
    :param hypotenuse: distance from origin
    :return: Vector2
    """
    return Vector2(hypotenuse * math.cos(radians), hypotenuse * math.sin(radians))

