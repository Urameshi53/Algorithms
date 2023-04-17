import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self,v):
        # new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        n = len(self.coordinates)
        new_coordinates = []
        for i in range(n):
            new_coordinates.append(self.coordinates[i]+v.coordinates[i])
        return Vector(new_coordinates)
    
    def minus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def sub(self,s):
        new_coordinates = [x-s for x in self.coordinates]
        return Vector(new_coordinates)
    
    def mult(self,c):
        new_coordinates = [x*c for x in self.coordinates]
        return Vector(new_coordinates)
    
    def normalize(self):
        try: 
            magnitude = self.magnitude()
            return self.mult(1./magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
        
    def magnitude(self):
        s = 0
        for i in self.coordinates:
            s += i**2
        ans = s**0.5
        return ans
    
    def unitv(self):
        m = self.magnitude()
        new_coordinates = [(1/m)*x for x in self.coordinates]
        return Vector(new_coordinates)
    
    def dot(self,v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
        # s = 0 
        # for i in range(self.dimension):
        #     s+=self.coordinates[i]*v.coordinates[i]
        # return s
    
    def angle(self,v):
        t = math.acos((self.dot(v))/(self.magnitude()*v.magnitude()))
        return t
    
    def angle_with(self,v,degrees=False):
        try:
            u1 = self.normalize()
            u2 = v.normalize()
            angle_in_radians = math.acos(u1.dot(u2))
            
            if degrees:
                return math.degrees(angle_in_radians)
            else:
                return angle_in_radians
        except Exception as e:
            if str(e)==self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else: 
                raise e
                
    def is_orthogonal(self,v,tolerance=1e-10):
        return abs(self.dot(v))<tolerance
    
    def is_parallel_to(self,v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle(v)==0 or
                self.angle(v)==math.pi)
    
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
        
    
# v1 = Vector([3,4])
# v2 = v1.mult(5)
# # print(v1.mult(3))
# # print(v1.plus(v2))
# v3 = Vector([-0.221,7.437])
# v4 = Vector([8.813,-1.331,-6.247])
# # print(v4.magnitude())
# v5 = Vector([5.581, -2.136])
# v6 = Vector([1.996,3.108,-4.554])
# # print(v6.unitv())

# v7 = Vector([7.887,4.138])
# v8 = Vector([-8.802,6.776])
# # print(v7.dot(v8))

# v9 = Vector([-5.955,-4.904,-1.874])
# v10 = Vector([-4.496,-8.755,7.103])
# # print(v9.dot(v10))

# v11 = Vector([1,-2,3])
# u = Vector([1,0,-1])
# # print(math.degrees(v11.angle(u)))

# u1 = Vector([3.183,-7.627])
# u2 = Vector([-2.668,5.319])
# # print(u1.angle(u2))

# u3 = Vector([7.35,0.221,5.188])
# u4 = Vector([2.751,8.259,3.985])
# # print(math.degrees(u3.angle(u4)))

# u5 = Vector([-7.579,-7.88])
# u6 = Vector([22.737,23.64])
# print("Parallel: ",u5.is_parallel_to(u6))
# print("Orthogonal: ",u5.is_orthogonal(u6))

# u7 = Vector([-2.029,9.97,4.172])
# u8 = Vector([-9.231,-6.639,-7.245])
# print("Parallel: ",u7.is_parallel_to(u8))
# print("Orthogonal: ",u7.is_orthogonal(u8))

# u9 = Vector([-2.328,-7.284,-1.214])
# u10 = Vector([-1.821,1.072,-2.94])
# print("Parallel: ",u9.is_parallel_to(u10))
# print("Orthogonal: ",u9.is_orthogonal(u10))

# u11 = Vector([2.118,4.827])
# u12 = Vector([0,0])
# print("Parallel: ",u11.is_parallel_to(u12))
# print("Orthogonal: ",u11.is_orthogonal(u12))

# v1 = Vector([2,-3])
# v2 = Vector([-3,0])
# v3 = Vector([-1,-1])
# v1 = v1.mult(2)
# v2 = v2.mult(-1)
# v3 = v3.mult(3)
# # print(v1,v2,v3)
# a = v1.minus(v2).minus(v3)
# # print(a.magnitude())

# v4 = Vector([4,0,3])
# v5 = Vector([-2,1,5])
# b = v4.minus(v5)
# print(b.magnitude())
# print(v4.unitv())

# if __name__ == '__main__':
    