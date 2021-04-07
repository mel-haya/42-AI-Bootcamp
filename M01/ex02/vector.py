class Vector:
    def __init__(self,values):
        if isinstance(values,list):
            self.values = values
        elif isinstance(values,int):
            i = 0.0
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
        count = max(self.size,other.size)
        ret = Vector(count)
        




