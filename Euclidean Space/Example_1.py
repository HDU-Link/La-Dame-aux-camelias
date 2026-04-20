import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

class BasicConfig:
    def plot_trajectory(solutions, ylabel):
        for sol, label in solutions:
            plt.plot(sol.t, sol.y[0], label=label)
        plt.xlabel("$t$")
        plt.ylabel(ylabel)
        plt.legend()
        plt.show()
        
    def plot_velocity_derivative(solutions):
        fig = plt.figure("Velocity derivative plot")
        for sol, label in solutions:
            plt.plot(sol.t, sol.y[1], label=label)
        plt.xlabel("$t$")
        plt.ylabel("$y'$")
        plt.legend()
        plt.show()
    def plot_optimization_curve(iterations, errors_list):
        fig = plt.figure("Optimization curve chart")
        plt.plot(iterations, errors_list, '-o', markersize=4)
        plt.xlabel("Number of iterations")
        plt.ylabel("Value of error function")
        plt.yscale('log')
        plt.show()
        
    @classmethod
    def apply(cls, style):
        plt.rcParams.update({
            'font.family': 'Arial',
            'lines.linewidth': 2
        })
        if style == 'default':
            plt.rcParams.update({
                'font.size': 16
            })
        elif style == 'paper':
            plt.rcParams.update({
                'font.size': 12
            })
        else:
            pass
if __name__ == "__main__":
    BasicConfig.apply('default')
    t_span = (0, 1); t_eval = np.linspace(0, 1, 100)

    # Shooting method for initial value
    iterations = [];errors_list = []
    def dynamics(t, state, mu):
        return np.hstack(
            [state[1:4], mu*(state[4]-state[0]),
             state[5:8], mu*(state[0]-state[4])])

    def errors(x, mu):
        initial_value = [1, 0, x[0], x[1], -1, 0, x[2], x[3]]
        sol = solve_ivp(lambda t, state: dynamics(t, state, mu),
                        t_span, initial_value, t_eval=t_eval, method='RK45')
        err = ((sol.y[0,-1]+1)**2+(sol.y[1,-1])**2
               +(sol.y[4,-1]-1)**2+(sol.y[5,-1])**2)
        return err

    def call(x, mu):
        iterations.append(len(iterations) + 1)
        errors_list.append(errors(x, mu))
    res2 = minimize(lambda x: errors(x, 200), [0, 0, 0, 0])
    res3 = minimize(lambda x: errors(x, 1000), [0, 0, 0, 0],
                    callback = lambda x: call(x, 1000), method = "L-BFGS-B")
    print(res3)

    # Solve and draw y[0]-t trajectory diagram
    solutions = []
    x0 = [1, 0, -12, 24,     -1, 0, 12, -24]
    x1 = [1, 0, -16.13, 71.30,     -1, 0, 16.13, -71.30]
    x2 = [1, 0, res2.x[0], res2.x[1], -1, 0, res2.x[2], res2.x[3]]
    x3 = [1, 0, res3.x[0], res3.x[1], -1, 0, res3.x[2], res3.x[3]]
    cases = [(0, x0, "$α$ = 0"), (100, x1, "$α$ = 50"),
            (200, x2, "$α$ = 100"), (1000, x3, "$α$ = 500")]
    for mu, initial_value, label in cases:
        sol = solve_ivp(lambda t, state: dynamics(t, state, mu),
            t_span, initial_value, t_eval=t_eval, method='RK45')
        solutions.append((sol, label))
        
    BasicConfig.plot_trajectory(solutions, "$y$")

    # Velocity derivative plot
    BasicConfig.plot_velocity_derivative(solutions)
    
    # Optimization curve chart
    BasicConfig.plot_optimization_curve(iterations, errors_list)
