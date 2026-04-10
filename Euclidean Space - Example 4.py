import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
plt.rcParams.update({
    'font.family': 'Arial',
    'font.sans-serif': ['Arial'],
    'lines.linewidth': 2
})

t_span = (0, 1); t_eval = np.linspace(0, 1, 100)

# Shooting method for initial value
iterations = [];errors_list = []
def dynamics(t, state, mu):
    distance = (state[0]**2+state[4]**2)
    return np.hstack(
        [state[1:4], mu*(state[0]/distance**2),
         state[5:8], mu*(state[4]/distance**2)])

def errors(x, mu):
    initial_value = [-1, 0, x[0], x[1], 0, 0, x[2], x[3]]
    sol = solve_ivp(lambda t, state: dynamics(t, state, mu),
                    t_span, initial_value, t_eval=t_eval, method='RK45')
    err = ((sol.y[0,-1]-1)**2+(sol.y[1,-1])**2
           +(sol.y[4,-1])**2+(sol.y[5,-1])**2)
    return err

def call(x, mu):
    iterations.append(len(iterations) + 1)
    errors_list.append(errors(x, mu))
res1 = minimize(lambda x: errors(x, 0), [0, 0, 0, 0])
res2 = minimize(lambda x: errors(x, 1), [0, 0, 0, 0], method="Nelder-Mead",
                callback = lambda x: call(x, 1))
print(res2)

# Solve and draw y-x trajectory diagram
solutions = []
x1 = [-1, 0, res1.x[0], res1.x[1], 0, 0, res1.x[2], res1.x[3]]
x2 = [-1, 0, res2.x[0], res2.x[1], 0, 0, res2.x[2], res2.x[3]]
cases = [(0, x1, "μ=0"), (1, x2, "μ=1")]
for mu, initial_value, label in cases:
    sol = solve_ivp(lambda t, state: dynamics(t, state, mu),
        t_span, initial_value, t_eval=t_eval, method='RK45')
    solutions.append((sol, label))
    
for sol, label in solutions:
    plt.plot(sol.y[0], sol.y[4], label=label)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.show()

# Optimization curve chart
fig = plt.figure("Optimization curve chart")
plt.plot(iterations, errors_list, '-o', markersize=4)
plt.xlabel("Number of iterations")
plt.ylabel("Value of error function")
plt.yscale('log')
plt.show()
