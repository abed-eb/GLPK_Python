from pymprog import *


def model_1():
    begin('bike production')
    verbose(True)
    x, y = var('x, y')  # variables
    maximize(15 * x + 10 * y, 'profit')
    x <= 3  # mountain bike limit
    y <= 4  # racer production limit
    x + y <= 5  # metal finishing limit
    solve()
    print("###>Objective value: %f" % vobj())
    sensitivity()
    end()  # Good habit: do away with the model


def model_2():
    c = (10, 6, 4)
    A = [(1, 1, 1),
         (9, 4, 5),
         (2, 2, 6)]
    b = (10, 60, 30)
    begin('basic')  # begin modelling
    verbose(True)  # be verbose
    x = var('x', 3)  # create 3 variables
    maximize(sum(c[i] * x[i] for i in range(3)))
    for i in range(3):
        sum(A[i][j] * x[j] for j in range(3)) <= b[i]
    solve()  # solve the model
    print("###>Objective value: %f" % vobj())
    sensitivity()  # sensitivity report
    end()  # Good habit: do away with the model


def model_3():
    begin('game')
    # gain of player 1, a free variable
    v = var('game_value', bounds=(None, None))
    # mixed strategy of player 2
    p = var('p', 2)
    # probability sums to 1
    sum(p) == 1
    # player 2 chooses p to minimize v
    minimize(v)
    # player 1 chooses the better value
    r1 = v >= 5 * p[0] + 9 * p[1]
    r2 = v >= 8 * p[0] + 6 * p[1]
    solve()
    print('Game value: %g' % v.primal)
    print("Mixed Strategy for player 1:")
    print("A1: %g, A2: %g" % (r1.dual, r2.dual))
    print("Mixed Strategy for player 2:")
    print("B1: %g, B2: %g" % (p[0].primal, p[1].primal))
    end()


def main():
    model_1()
    print("----------------------------------------------------------------------------------------------------------------------")
    model_2()
    print("----------------------------------------------------------------------------------------------------------------------")
    model_3()
if __name__ == '__main__':
    main()
