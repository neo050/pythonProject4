
"""
m1 = Matrix(3, 4)
m1.set_matrix()
print(Pivot_order(m1))
m1 = Matrix_Rating(Pivot_order(m1))
print(m1.M[(1,4)])
"""




class Matrix:
    def __init__(self, row, coll):
        self.M = dict()
        self.Row = row
        self.Coll = coll
        for i in range(1, row + 1):
            for j in range(1, coll + 1):
                if i == j:
                    self.M[(i, j)] = 1
                else:
                    self.M[(i, j)] = 0

    def set_matrix(self):
        for i in range(1, self.Row + 1):
            for j in range(1, self.Coll + 1):
                self.M[(i, j)] = float(input(f'Please Enter M{[i, j]} :\n'))


    def set_matrix_with_Polynomial_interpolation(self, data, vectorB):
        for i in range(1, self.Row + 1):
            for j in range(1, self.Coll+1):
                self.M[(i, j)] = float((data[i-1]**(j-1)))
        for i in range(1, self.Row+1):
            self.M[(i, self.Coll)] = float(vectorB[i-1])

    def Elementary_matrix(self, i, j, value):
        temp = Matrix(self.Row, self.Coll)
        temp.M[(i, j)] = value
        return temp

    def __add__(self, other):
        if self.Row != other.Row or self.Coll != other.Coll:
            return "Error"
        temp = Matrix(self.Row, self.Coll)
        for i in range(1, self.Row + 1):
            for j in range(1, other.Coll + 1):
                temp.M[(i, j)] = self.M[(i, j)] + other.M[(i, j)]
        return temp

    def __mul__(self, other):
        temp = Matrix(self.Row, other.Coll)
        for i in range(1, self.Row + 1):
            for j in range(1, other.Coll + 1):
                if i == j:
                    temp.M[(i, j)] = temp.M[(i, j)] - 1
                for k in range(1, other.Row + 1):
                    temp.M[(i, j)] += self.M[(i, k)] * other.M[(k, j)]

        return temp

    def Line_replacement(self, x, y):
        temp1 = Matrix(self.Row, self.Coll)
        temp2 = Matrix(self.Row, self.Coll)
        for i in range(1, self.Coll + 1):
            temp1.M[(x, i)] = temp2.M[(y, i)]
            temp1.M[(y, i)] = temp2.M[(x, i)]
        print(print_mul(temp1, self))
        return temp1 * self

    def __str__(self):
        x = ''
        for i in range(1, self.Row + 1):
            x += str(list(self.M[(i, j)] for j in range(1, self.Coll + 1))) + '\n'
        return x


def Matrix_Rating(m):
    if m.Coll == m.Row + 1:
        temp = Matrix(m.Row, m.Coll - 1)
    else:
        temp = Matrix(m.Row, m.Coll)

    for i in range(1, m.Coll + 1):
        for j in range(i, m.Row + 1):
            if i == j:
                if m.M[(j, i)] != 1:
                    print(print_mul(temp.Elementary_matrix(j, i, 1 / m.M[(j, i)]), m))
                    m = temp.Elementary_matrix(j, i, 1 / m.M[(j, i)]) * m



            else:
                if m.M[(j, i)] != 0:
                    print(print_mul(temp.Elementary_matrix(j, i, -1 * m.M[(j, i)]), m))
                    m = temp.Elementary_matrix(j, i, -1 * m.M[(j, i)]) * m

    for i in list(range(1, m.Coll).__reversed__()):
        for j in list(range(1, i).__reversed__()):
            if i != j:
                print(print_mul(temp.Elementary_matrix(j, i, -1 * m.M[(j, i)]), m))
                m = temp.Elementary_matrix(j, i, -1 * m.M[(j, i)]) * m
    print("⏬  ⬇️final solution  ⬇️⏬")
    for i in range(1, m.Row + 1):
        print(f'  X[{i}] = {m.M[(i, m.Coll)]}')
    return m


def Pivot_order(m):
    for i in range(1, m.Coll + 1):
        for j in range(i, m.Row + 1):
            if abs(m.M[(j, i)]) > abs(m.M[(i, i)]):
                m = m.Line_replacement(i, j)
    return m


def print_mul(x, y):
    k = ''
    for i in range(1, x.Row + 1):
        if i == int(x.Row / 2 + 1):
            k += str(list(x.M[(i, j)] for j in range(1, x.Coll + 1))) + "  *  " + str(
                list(y.M[(i, j)] for j in range(1, y.Coll + 1))) + '  =  ' + str(
                list((x * y).M[(i, j)] for j in range(1, (x * y).Coll + 1)))
        else:
            k += str(list(x.M[(i, j)] for j in range(1, x.Coll + 1))) + "     " + str(
                list(y.M[(i, j)] for j in range(1, y.Coll + 1))) + "     " + str(
                list((x * y).M[(i, j)] for j in range(1, (x * y).Coll + 1)))
        k += '\n'

    return k


if __name__ == '__main__':
    m1 = Matrix(3, 4)
    m1.set_matrix()
    print(Matrix_Rating(Pivot_order(m1)))

