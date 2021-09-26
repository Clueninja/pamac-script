class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        if len(matrix)!=0:
            self.dim = (len(self.matrix), len(self.matrix[0]))

    def update(self):
        self.dim = (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        temp = Matrix([])
        if self.dim == other.dim:
            for row in range(self.dim[0]):
                temp.matrix.append([self.matrix[row][column] + other.matrix[row][column] for column in range(self.dim[1])])
        temp.update()
        return temp

    def __sub__(self,other):
        temp = Matrix([])
        if self.dim == other.dim:
            for row in range(self.dim[0]):
                temp.matrix.append([self.matrix[row][column] - other.matrix[row][column] for column in range(self.dim[1])])
        temp.update()
        return temp

    def __str__(self):
        string = str()
        for row in range(self.dim[0]):
            for column in range(self.dim[1]):
                string+=str(self.matrix[row][column])+" "
            string+="\n"
        return string
        



    def __mul__(self, other):
        temp = Matrix([])
        for _u in range(self.dim[0]):
            temp.matrix.append([0 for _r in range(other.dim[1])])

        for i in range(self.dim[0]):
            for j in range(other.dim[1]):
                for k in range(other.dim[0]):
                    temp.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return temp
                    

class TwoByTwo(Matrix):
    def __init__(self, matrix):
        super().__init__(matrix)

class Vector(Matrix):
    def __init__(self, list):
        super().__init__(list)

if __name__ == "__main__":
    d = Matrix([[1,2],[3,4],[5,6]])
    e = Matrix([[1,2,3], [4,5,6]])
    d.update()
    e.update()
    print(d)
    print(e)
    d = d*e
    d.update()
    print(d)

