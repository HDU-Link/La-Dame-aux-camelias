import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
plt.rcParams.update({
    'font.family': 'Arial',
    'font.sans-serif': ['Arial'],
    'lines.linewidth': 2
})

t_span = (0, 1); t_eval = np.linspace(0, 1, 100);
n_agents = 4; y0 = [0, 0]
# Shooting method for initial value
iterations = [];errors_list = []
def dynamics(t, state, mu):
    deriv = np.zeros_like(state)
    for i in range(n_agents):
        x, y = state[8*i], state[8*i+4]
        distance = (x-y0[0])**2 + (y-y0[1])**2
        deriv[8*i:8*i+3] = state[8*i+1:8*i+4]
        deriv[8*i+3] = mu*x/distance**2
        deriv[8*i+4:8*i+7] = state[8*i+5:8*i+8]
        deriv[8*i+7] = mu*y/distance**2
    deriv[3] += mu*(state[8] - state[0])
    deriv[11] += mu*(state[0] - state[8])
    deriv[7] += mu*(state[12] - state[4])
    deriv[15] += mu*(state[4] - state[12])
    deriv[19] += mu*(state[24] - state[16])
    deriv[27] += mu*(state[16] - state[24])
    deriv[23] += mu*(state[28] - state[20])
    deriv[31] += mu*(state[20] - state[28])
    return deriv

def errors(x, mu):
    initial_value = [-1, 0, x[0], x[1], 2, 0, x[2], x[3],
                     -1, 0, x[4], x[5], 1, 0, x[6], x[7],
                     -1, 0, x[8], x[9], -1, 0, x[10], x[11],
                     -1, 0, x[12], x[13], -2, 0, x[14], x[15]]
    sol = solve_ivp(lambda t, state: dynamics(t, state, mu),
                    t_span, initial_value, t_eval=t_eval, method='RK45')
    err = ((sol.y[0,-1]-1)**2+(sol.y[1,-1])**2
          +(sol.y[4,-1]-2)**2+(sol.y[5,-1])**2
          +(sol.y[8,-1]-1)**2+(sol.y[9,-1])**2
          +(sol.y[12,-1]-1)**2+(sol.y[13,-1])**2
          +(sol.y[16,-1]-1)**2+(sol.y[17,-1])**2
          +(sol.y[20,-1]+1)**2+(sol.y[21,-1])**2
          +(sol.y[24,-1]-1)**2+(sol.y[25,-1])**2
          +(sol.y[28,-1]+2)**2+(sol.y[29,-1])**2)
    return err

def call(x, mu):
    iterations.append(len(iterations) + 1)
    errors_list.append(errors(x, mu))
res1 = minimize(lambda x: errors(x, 0), np.zeros(n_agents*4))
res2 = minimize(lambda x: errors(x, 10), np.zeros(n_agents*4),
                callback = lambda x: call(x, 10))
print(res2.fun, res2.message)

# Solve and draw y-x trajectory diagram
solutions = []
x1 = [-1, 0, res1.x[0], res1.x[1],
       2, 0, res1.x[2], res1.x[3],
      -1, 0, res1.x[4], res1.x[5],
       1, 0, res1.x[6], res1.x[7],
      -1, 0, res1.x[8], res1.x[9],
      -1, 0, res1.x[10], res1.x[11],
      -1, 0, res1.x[12], res1.x[13],
      -2, 0, res1.x[14], res1.x[15]]
x2 = [-1, 0, res2.x[0], res2.x[1],
       2, 0, res2.x[2], res2.x[3],
      -1, 0, res2.x[4], res2.x[5],
       1, 0, res2.x[6], res2.x[7],
      -1, 0, res2.x[8], res2.x[9],
      -1, 0, res2.x[10], res2.x[11],
      -1, 0, res2.x[12], res2.x[13],
      -2, 0, res2.x[14], res2.x[15]]
cases = [(0, x1, "μ=0"), (10, x2, "μ=10")]
for mu, initial_value, label in cases:
    sol = solve_ivp(lambda t, state: dynamics(t, state, mu),
        t_span, initial_value, t_eval=t_eval, method='RK45')
    solutions.append((sol, label))
    
for sol, label in solutions:
    fig = plt.figure(label)
    plt.scatter(0, 0, color="black", label="$y_0$")
    for i in range(n_agents):
        plt.plot(sol.y[8*i], sol.y[8*i+4], label=fr"$x_{i}$")
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
