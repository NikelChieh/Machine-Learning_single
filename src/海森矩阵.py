from sympy import pprint, Symbol, diff, solve, symarray, Eq, Expr, roots, simplify, lambdify, hessian
from sympy.matrices import Matrix, zeros, diag, eye, GramSchmidt
from sympy.abc import lamda, x, y, z, t
import numpy as np


def solve_extremum(expr, symList, stagnation_point: tuple = None):
    from sympy import hessian
    import numpy as np
    hsm = np.array(hessian(expr, symList).evalf()).astype(np.float32)
    sym_tup = tuple(symList)
    # 用特征值判断
    eig_val = np.linalg.eigvals(hsm)
    print('\n海森矩阵的特征值：')
    print(eig_val)
    greater = eig_val > 0.0
    less = eig_val < 0.0
    bool_list = [True for i in range(len(eig_val))]
    if np.allclose(bool_list, greater):
        print('\nf{} = {}的海森矩阵是正定矩阵，存在极小值点。\n'.format(sym_tup, expr))
        if stagnation_point:
            print('故{}是极小值点，且极小值f{} = {}\n'.format(stagnation_point, stagnation_point,
                                                   expr.subs({k: v for k, v in zip(symList, stagnation_point)})))
    elif np.allclose(bool_list, less):
        print('\n' + 'f{} = {}的海森矩阵是负定矩阵，存在极大值点。\n'.format(sym_tup, expr))
        if stagnation_point:
            print('故{}是极大值点，且极大值f{} = {}\n'.format(stagnation_point, stagnation_point,
                                                   expr.subs({k: v for k, v in zip(symList, stagnation_point)})))
    else:
        print('\n无法判断极值点\n')


'''三元函数'''
f = x ** 2 + y ** 2 + z ** 2 + 2 * x + 4 * y - 6 * z

# 求驻点
dx = diff(f, x)
dy = diff(f, y)
dz = diff(f, z)
stagnation_point = solve((dx, dy, dz), x, y, z)
if isinstance(stagnation_point, dict):
    point = []
    point.append((stagnation_point[x], stagnation_point[y], stagnation_point[z]))
    stagnation_point = point
for i, point in enumerate(stagnation_point):
    print('驻点{}：{}'.format(i + 1, point))

f_hsm = hessian(f, [x, y, z])  # 海森矩阵
print('\n' + 'f(x,y,z)的海森矩阵：')
pprint(f_hsm)
solve_extremum(f, [x, y, z], stagnation_point[0])

A = Matrix([[-5, -2, 4], [-2, -1, 2], [4, 2, -5]])
# A = Matrix([[-10,-4,-12],[-4,-2,14],[-12,14,-1]])
X = Matrix([x, y, z])
f2 = (X.T * A * X)[0, 0].simplify()

# 求驻点
dx = diff(f2, x)
dy = diff(f2, y)
dz = diff(f2, z)

stagnation_point = solve((dx, dy, dz), x, y, z)
if isinstance(stagnation_point, dict):
    point = []
    point.append((stagnation_point[x], stagnation_point[y], stagnation_point[z]))
    stagnation_point = point
for i, point in enumerate(stagnation_point):
    print('驻点{}：{}'.format(i + 1, point))

f2_hsm = hessian(f2, [x, y, z, t])
print('\n' + 'f(x,y,z)的海森矩阵：')
pprint(f2_hsm)
solve_extremum(f2, [x, y, z], stagnation_point[0])

'''随机生成整数测试'''
# np.random.seed(28)
# 生成在驻点附近的点
arr_x = np.random.uniform(-2, 0, (5,))
arr_y = np.random.uniform(-3, -1, (5,))
arr_z = np.random.uniform(2, 4, (5,))

# sympy中使用numpy高效计算
f = lambdify((x, y, z), f, 'numpy')
print(f(arr_x, arr_y, arr_z))

f2 = lambdify((x, y, z), f2, 'numpy')
print(f2(arr_x, arr_y, arr_z))
