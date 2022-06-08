import random
import Matrix_tools.Matrix_LU.LU_F as LU
import sympy as sp
from sympy.utilities.lambdify import lambdify
import math

x = sp.symbols('x')


# t = (x*math.e**(-x)+math.log(x**2,math.e))*(2*x**3+2*x**2-3*x-5)

def Bisection_Method(f, a, b, epsilon=10 ** -15):
    f_tag = sp.diff(f, x)
    f_tag = lambdify(x, f_tag)
    f = lambdify(x, f)
    temp = []
    result = 0
    if f(a) * f(b) < 0:
        while b - a > epsilon:
            print('[ %1.6f' % (a) + ', %1.6f ]' % (b))
            result = result + 1
            m = a + (b - a) / 2
            if f(a) * f(m) > 0:
                a = m
            else:
                b = m
        return [(a + b) / 2, result]
    elif f_tag(a) * f_tag(b) < 0:
        while b - a > epsilon:
            temp.append('[ %1.6f' % (a) + ', %1.6f ]' % (b))
            result = result + 1
            m = a + (b - a) / 2
            if f_tag(a) * f_tag(m) > 0:
                a = m
            else:
                b = m
        if abs(f((a + b) / 2)) < epsilon:
            for i in temp:
                print(i)
            return [(a + b) / 2, result]


def Newton_Raphson(f, a, b, epsilon=10 ** -15):
    f_tag = sp.diff(f, x)
    f_tag = lambdify(x, f_tag)
    f = lambdify(x, f)
    temp = []
    result = 0
    if f(a) * f(b) < 0:
        m1 = (a + b) / 2
        m2 = m1 - f(m1) / f_tag(m1)
        while abs(m2 - m1) > epsilon:
            print('[ %1.6f' % (m1) + ', %1.6f ]' % (m2))
            result = result + 1
            m1 = m2
            m2 = m1 - f(m1) / f_tag(m1)
        return [m2, result]
    elif f_tag(a) * f_tag(b) < 0:
        m1 = (a + b) / 2
        m2 = m1 - f(m1) / f_tag(m1)
        while abs(m2 - m1) > epsilon:
            temp.append('[ %1.6f' % (m1) + ', %1.6f ]' % (m2))
            result = result + 1
            m1 = m2
            m2 = m1 - f(m1) / f_tag(m1)
        if abs(f(m2)) < epsilon and (m2 >= a + epsilon or m2 >= a - epsilon) and (
                m2 <= b + epsilon or m2 <= b + epsilon):
            for i in temp:
                print(i)
            return [m2, result]


def secant_method(f, a, b, epsilon=10 ** -15):
    f_tag = sp.diff(f, x)
    f_tag = lambdify(x, f_tag)
    f = lambdify(x, f)
    temp1 = []
    result = 0
    if f(a) * f(b) < 0:
        m1 = a
        m2 = b
        while abs(m2 - m1) > epsilon:
            print('[ %1.6f' % (m1) + ', %1.6f ]' % (m2))
            temp = m2
            result = result + 1
            m2 = (m1 * f(m2) - m2 * f(m1)) / (f(m2) - f(m1))
            m1 = temp
        return [m2, result]
    elif f_tag(a) * f_tag(b) < 0:
        m1 = a
        m2 = b
        while abs(m2 - m1) > epsilon:
            temp1.append('[ %1.6f' % (m1) + ', %1.6f ]' % (m2))
            temp = m2
            result = result + 1
            m2 = (m1 * f(m2) - m2 * f(m1)) / (f(m2) - f(m1))
            m1 = temp
        if abs(f(m2)) < epsilon and (m2 >= a + epsilon or m2 >= a - epsilon) and (
                m2 <= b + epsilon or m2 <= b + epsilon):
            for i in temp1:
                print(i)
            return [m2, result]


def main():
    e = math.e
    my_f = sp.simplify(math.sin(x**4 +5*x -6)/2*math.e**(2*x+5))
    f_tag = sp.diff(my_f, x)
    f_tag = lambdify(x, f_tag)
    f = lambdify(x, my_f)
    start_point = -1.5
    end_point = 1.5
    step = 0.1
    epsilon = 10 ** -6
    print('Please select the method you want to find the roots of the equation : \n')
    choice = input('1 - Bisection Method\n2 - Newton Raphson\n3 - secant method\n')
    while choice != '3' and choice != '2' and choice != '1':
        print('Error input please try again...\n')
        choice = input('1 - Bisection Method\n2 - Newton Raphson\n3 - secant method\n')
    if choice == '1':
        while end_point > start_point:
            if f(start_point) * f(start_point + step) < 0 or f_tag(start_point) * f_tag(start_point + step) < 0:
                temp = Bisection_Method(my_f, start_point, start_point + step, epsilon)
                if temp is not None:
                    print(f'The number of iterations to find the root is {temp[1]}')
                    print(f'The root of the function ==> %1.6f' % (temp[0]))
            start_point = start_point + step
    elif choice == '2':
        while end_point > start_point:
            if f(start_point) * f(start_point + step) < 0 or f_tag(start_point) * f_tag(start_point + step) < 0:
                temp = Newton_Raphson(my_f, start_point, start_point + step, epsilon)
                if temp is not None:
                    print(f'The number of iterations to find the root is {temp[1]}')
                    print(f'The root of the function ==> %1.6f' % (temp[0]))
            start_point = start_point + step
    elif choice == '3':
        while end_point > start_point:
            if f(start_point) * f(start_point + step) < 0 or f_tag(start_point) * f_tag(start_point + step) < 0:
                temp = secant_method(my_f, start_point, start_point + step, epsilon)
                if temp is not None:
                    print(f'The number of iterations to find the root is {temp[1]}')
                    print(f'The root of the function ==> %1.6f' % (temp[0]))
            start_point = start_point + step


# main()
print(math.log(10, math.e))

table12 = ((1, 0.8415), (2, 0.9093),
           (3, 0.1411), (4, -0.7568),
           (5, -0.9589), (6, -0.2794))
table3 = ((5.5, 3.14), (6.8, 4.35), (8.3, 5.70))
table4 = {(0, 0): [1, 0], (1, 1): [1.2, 0.112463],
          (2, 2): [1.3, 0.167996], (3, 3): [1.4, 0.222709]}
X_to_find = 2.5

# PAR5
values_table = tuple([[5.5,6.8,7.2, 8.3], [3.14, 4.35, 2.74, 5.70]])
x_f = 7.0
size = len(values_table[0]) - 2

print(table4[3, 3][0])
print(table4[3, 3][1])

iteraion = []
for i in range(len(table4)):
    iteraion.append(i)
iteraion.reverse()


def calc_nevil(fx, i, s, table4, P):
    step = int(s)
    remainder = step - 1
    C1 = fx - (table4[i, i][0])
    C2 = P[(i+1), (i+1+remainder)]
    C3 = fx - (table4[(i+step), (i+step)][0])
    C4 = P[i, (i+remainder)]
    numerator = ((fx - (table4[i, i][0])) * (P[(i+1), (i+1+remainder)])) - ((fx - (table4[(i+step), (i+step)][0])) * (P[i, (i+remainder)]))
    denominator = ((table4[i+step, i+step][0]) - (table4[i, i][0]))
    val = numerator / denominator
    return val


def Neville_Algorithm(table4):
    fx = 1.28
    P = {}
    for i in range(len(table4)):
        P[i, i] = table4[i, i][1]

    iteraion = []
    step = []
    for i in range(1, len(table4)):
        iteraion.append(i)
        step.append(i)
    iteraion.reverse()

    loop = len(table4.keys())
    for s in step:
        for i in range(loop-s):
            P[i, i+s] = calc_nevil(fx, i, s, table4, P)
    return P[0, len(table4)-1]




def data_from_table(table):
    size_of_solutions = 3  # input(f' how much parameters do you wan to send in the vectorB')
    tempVector = list(range(1, size_of_solutions + 1))
    tempMatrix = list(range(1, size_of_solutions + 1))
    index = 0
    for i in table:
        tempMatrix[index] = i[0]
        tempVector[index] = i[1]
        index += 1
        if index == size_of_solutions:
            break

    return tempMatrix, tempVector


def linear_interpolation(val, table):
    """
    :param val: is the X we wan to find he's Y.
    :param table: are vals in dict, [i,j],i=x1,j=y1.
    :return:

    """
    theLastI = ()
    for i in table:
        if val >= i[0]:
            theLastI = i
        else:
            answer = calcLinear(theLastI, i, val)
            return answer


def calcLinear(X1, X2, val):
    """

    :param X1: Point 1 <val
    :param X2: Point 2> val
    :param val: Are X to find
    :return: Result
    """
    return ((X1[1] - X2[1]) / (X1[0] - X2[0])) * val + (((X2[1] * X1[0]) - (X1[1] * X2[0])) / (X1[0] - X2[0]))


def polynomial_interpolation():
    """
    create matrix from are data and replace here to vectorA and vectorB solution
    you haft to import are file tools Matrix from HW1
    :return: sum of the polynomial
    """
    polinum_matrix_vals, vectorB = data_from_table(table12)
    matrix_n_n = LU.Matrix(3, 4)
    matrix_n_n.set_matrix_with_Polynomial_interpolation(polinum_matrix_vals, vectorB)
    matrix_n_n = LU.Matrix_Rating(LU.Pivot_order(matrix_n_n))
    parameters_polinum = get_param_from_matrix(matrix_n_n)
    return final_step_polynomial_interpolation(parameters_polinum)


def final_step_polynomial_interpolation(parameters_polinum):
    sum = 0
    for i in range(0, len(parameters_polinum)):
        sum += parameters_polinum[i] * X_to_find ** i
    return sum


def get_param_from_matrix(matrix):
    temp = list(range(1, matrix.Row + 1))
    for i in range(1, matrix.Row + 1):
        temp[i - 1] = matrix.M[(i, matrix.Coll)]
    return temp


def Interrogation_of_Lagrange(X):
    x = 7  # you can change your param to find here
    L0 = ((x - X[1][0]) / (X[0][0] - X[1][0])) * ((x - X[2][0]) / (X[0][0] - X[2][0]))
    L1 = ((x - X[0][0]) / (X[1][0] - X[0][0])) * ((x - X[2][0]) / (X[1][0] - X[2][0]))
    L2 = ((x - X[0][0]) / (X[2][0] - X[0][0])) * ((x - X[1][0]) / (X[2][0] - X[1][0]))
    print (L0,L1,L2)
    return L0 * X[0][1] + L1 * X[1][1] + L2 * X[2][1]



def exchange(row, row_replace):
    unit_matrix = temp_elementary = make_unit_matrix()
    temp_elementary[row], temp_elementary[row_replace] = unit_matrix[row_replace], unit_matrix[row]
    return temp_elementary
def make_unit_matrix():
    unit_matrix = []
    for i in range(0, size):
        temp = []

        for j in range(0, size):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        unit_matrix.append(temp)
    return unit_matrix

def multiply_two_matrix(matrix1, matrix2):
    result = []
    for r in range(len(matrix1)):
        helper_res = []
        for c in range(len(matrix1)):
            helper_res.append(0)
        result.append(helper_res)
    for i in range(len(matrix1)):
        # iterating by column by B
        for j in range(len(matrix2[0])):
            # iterating by rows of B
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
def make_elementary_matrix(pivot, num1, row, col):
    temp_elementary = make_unit_matrix()
    temp_elementary[row][col] = -1 * (num1 / pivot)
    return temp_elementary

def exchange(row, row_replace):
    unit_matrix = temp_elementary = make_unit_matrix()
    temp_elementary[row], temp_elementary[row_replace] = unit_matrix[row_replace], unit_matrix[row]
    return temp_elementary
def gauss_method(matrix):
    mul = make_unit_matrix()
    for r in range(size):
        maxi = abs(matrix[r][r])
        flag = 0
        for c in range(r, size):
            if abs(matrix[c][r]) > maxi:
                maxi = abs(matrix[c][r])
                flag = 1
                c_max = c
        if flag != 0:
            temp_matrix = exchange(r, c_max)
            mul = multiply_two_matrix(temp_matrix, mul)
            matrix = multiply_two_matrix(temp_matrix, matrix)
    for r in range(size):
        for c in range(r, size):
            if matrix[r][r] == 1 and r != c:
                temp_matrix = make_elementary_matrix(matrix[r][r], matrix[c][r], c, r)
                mul = multiply_two_matrix(temp_matrix, mul)
                matrix = multiply_two_matrix(temp_matrix, matrix)
            else:
                temp_matrix = make_unit_matrix()
                if matrix[r][r] < 0:
                    temp_matrix[r][r] = 1 / matrix[r][r]
                else:
                    temp_matrix[r][r] = 1 / matrix[r][r]
                mul = multiply_two_matrix(temp_matrix, mul)
                matrix = multiply_two_matrix(temp_matrix, matrix)
    for r in range(size-1, -1, -1):
        for c in range(r, -1, -1):
            if r != c:
                temp_matrix = make_elementary_matrix(matrix[r][r], matrix[c][r], c, r)
                mul = multiply_two_matrix(temp_matrix, mul)
                matrix = multiply_two_matrix(temp_matrix, matrix)
    return mul

def Spline_Kobe(arr, x_f1):
    hi = []
    gama = []
    mi = []
    di = []
    new_matrix = []
    final_result1 = []
    s_x = 0
    for i in range(len(arr[0])):
        if i == len(arr[0])-1:
            hi.append(0)
        else:
            hi.append(arr[0][i+1] - arr[0][i])
    for i in range(len(hi)):
        if i == len(hi)-1 or i == 0:
            mi.append(0)
            gama.append(0)
        else:
            gama.append(hi[i]/(hi[i]+hi[i-1]))
            mi.append(1-gama[i])
    for i in range(1, len(arr[0])-1):
        di.append((6/(hi[i-1]+hi[i]))*(((arr[1][i+1]-arr[1][i])/hi[i])-((arr[1][i]-arr[1][i-1])/hi[i-1])))
    for i in range(size):
        helper = []
        for j in range(size):
            if i == j:
                helper.append(2)
            elif j == i+1:
                helper.append(gama[j])
            elif j == i-1:
                helper.append(mi[i+1])
            else:
                helper.append(0)
        new_matrix.append(helper)
    multiply_elementary_matrix = gauss_method(new_matrix)
    for i in range(len(multiply_elementary_matrix)+1):
        final_result1.append(0)
    for r in range(len(multiply_elementary_matrix)):
        for c in range(len(multiply_elementary_matrix)):
            final_result1[r] += multiply_elementary_matrix[r][c] * di[c]

    counter = 0
    for i in range(len(arr[0])):
        if i > 1:
            counter += 1
        if arr[0][i] > x_f1:
            x_1 = arr[0][i - 1]
            x_2 = arr[0][i]
            s_x = (((x_2-x_f1)**3)*final_result1[counter-1]+((x_f1-x_1)**3)*final_result1[counter])/(6*hi[counter])+(((x_2-x_f1)*arr[1][i-1]+(x_f1-x_1)*arr[1][i])/hi[counter]) -(((x_2-x_f1)*final_result1[counter-1]+(x_f1-x_1)*final_result1[counter])*hi[counter])/6
            print(final_result1)
            break
    return s_x



def menu():
    #print(f'\nMethod: "Linear interpolation" with the val:{X_to_find} is -> {linear_interpolation(X_to_find, table12)}\n***********************************\n')
    #print(f'\nMethod: "polynomial_interpolation" with the val:{X_to_find} is -> {polynomial_interpolation()}\n***********************************\n')
    print(f'\nMethod: "Interrogation of Lagrange" is -> {Interrogation_of_Lagrange(table3)}\n***********************************\n')
   # print(f'\nMethod: "Neville_Algorithm" is -> {Neville_Algorithm(table4)}\n***********************************\n')
    print(f'Method: "Spline_Kobe method" the result is: {Spline_Kobe(values_table, x_f)}')

if __name__ == '__main__':
    menu()
