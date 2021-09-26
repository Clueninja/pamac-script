
class Tablaux:
    def __init__(self, dim, matrix):
        self.dim = dim
        self.tablaux = matrix

    def simplex(self):
        temp_tabloux = Tablaux(self.dim, self.tablaux)
        while True:
            most_negative = [0,-1]
            for num in range(temp_tabloux.dim[1]):
                if temp_tabloux.tablaux[0][num]<most_negative[0]:
                    most_negative = [temp_tabloux.tablaux[0][num], num]
            
            if most_negative[0]!=0:
                pivot_column = most_negative[1]
                temp_constraints = []
                for index in range(temp_tabloux.dim[0]):
                    temp_constraints.append(temp_tabloux.tablaux[index][-1] / temp_tabloux.tablaux[index][pivot_column])
                
                coord_of_constraint_pivot = [pivot_column, temp_tabloux.tablaux.index(min(temp_tabloux.tablaux))]

                for index in range(temp_tabloux.dim[1]):
                    temp_tabloux.tablaux[coord_of_constraint_pivot[1]][index] = temp_tabloux.tablaux[coord_of_constraint_pivot[1]][index]/temp_tabloux.tablaux [coord_of_constraint_pivot[1]][coord_of_constraint_pivot[0]]
                
                

                for row in range(temp_tabloux.dim[0]):
                    temp_row = temp_tabloux.tablaux[coord_of_constraint_pivot[1]]
                    if row != temp_row:
                        multiplier = temp_tabloux.tablaux[row][coord_of_constraint_pivot[1]]/temp_row[coord_of_constraint_pivot[1]]
                        for n in temp_row:
                            n = n*multiplier
                        
                        for column in range(temp_tabloux.dim[1]):
                            temp_tabloux.tablaux[row] [column] = temp_tabloux.tablaux[row][column] - temp_row[column]
                    
            else:
                break
        return temp_tabloux
        

    def __str__(self):
        string = str()
        for row in range(self.dim[0]):
            for column in range(self.dim[1]):
                string+=str(self.tablaux[row][column])+" "
            string+="\n"
        return string
        

            

        
if __name__ == "__main__":
    A = Tablaux([4,7], [[1,-1,-0.8,0,0,0,0],[0,1,1,1,0,0,1000],[0,2,1,0,1,0,1500],[0,3,2,0,0,1,2400]])
    B = A.simplex()
    print(B)



