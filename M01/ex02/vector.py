class Vector:
    def __init__(self,values):
        if isinstance(values,list):
            self.values = values
        elif isinstance(values,int):
            i = 0
            self.values = []
            while i < values:
                self.values.append(i)
                i+=1
        elif isinstance(values,tuple) and len(values) == 2:
            self.values = list(range(values[0],values[1]))
        else:
            raise ValueError("Invalid Vector value")
        self.size = len(self.values)
    def __add__(self,other):
        ret = Vector(self.size)
        i = 0
        if isinstance(other, (int, float)):
            while i < self.size:
                ret.values[i] = self.values[i] + other
                i+=1
            return ret
        elif isinstance(other, Vector):
            if self.size != other.size:
                raise ValueError("the two vectors have diffrent dimentions")
            while i < self.size:
                ret.values[i] = self.values[i] + other.values[i] 
                i+=1
        else:
            raise ValueError("invalid addition")
        return ret

    
    def __radd__(self,other):
        ret = Vector(self.size)
        i = 0
        if not isinstance(other, (int, float)):
            raise ValueError("invalid addition")
        while i < self.size:
            ret.values[i] = self.values[i] + other
            i+=1
        return ret


    def __sub__(self,other):
        ret = Vector(self.size)
        i = 0
        if isinstance(other, (int, float)):
            while i < self.size:
                ret.values[i] = self.values[i] - other
                i+=1
            return ret
        elif isinstance(other, Vector):
            if self.size != other.size:
                raise ValueError("the two vectors have diffrent dimentions")
            while i < self.size:
                ret.values[i] = self.values[i] - other.values[i] 
                i+=1
        else:
            raise ValueError("invalid subtraction")
        return ret

    def __rsub__(self,other):
        ret = Vector(self.size)
        i = 0
        if not isinstance(other, (int, float)):
            raise ValueError("invalid subtraction")
        while i < self.size:
            ret.values[i] = - self.values[i] + other
            i+=1
        return ret

    def __mul__(self,other):
        ret = 0
        i = 0
        if isinstance(other, (int, float)):
            while i < self.size:
                ret += self.values[i] * other
                i+=1
            return ret
        elif isinstance(other, Vector):
            if self.size != other.size:
                raise ValueError("the two vectors have diffrent dimentions")
            while i < self.size:
                ret += self.values[i] * other.values[i] 
                i+=1
        else:
            raise ValueError("invalid dot product")
        return ret
    
    def __rmul__(self,other):
        ret = 0
        i = 0
        if not isinstance(other, (int, float)):
            raise ValueError("invalid dot product")
        while i < self.size:
            ret += self.values[i] * other
            i+=1
        return ret


    def __truediv__(self, other):
        ret = 0
        i = 0
        if other == 0:
            raise ValueError("div on zero")
        if isinstance(other, (int, float)):
            while i < self.size:
                ret += self.values[i] / other
                i+=1
            return ret
        else:   
            raise ValueError("invalid division")
    

    def __rtruediv__(self, other):
        ret = 0
        i = 0
        if 0 in self.values:
            raise ValueError("div on zero")

        if isinstance(other, (int, float)):
            while i < self.size:
                ret += other / self.values[i]
                i+=1
            return ret
        else:   
            raise ValueError("invalid division")

    def __str__(self):
        return "this " + str(self.size) + "D vector values are " + str(self.values)

    def __repr__(self):
        ret = "Vector(" + str(self.size) + "," + str(self.values) + ")"
        return ret


