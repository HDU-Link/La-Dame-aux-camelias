import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from matplotlib.animation import FuncAnimation
import seaborn as sns
plt.rcParams.update({
    'font.family': 'Arial',
    'font.sans-serif': ['Arial'],
    'font.size': 12,
    'lines.linewidth': 2
})
sns.set_style("darkgrid")
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

res = minimize(lambda x: errors(x, 2500), [0, 0, 0, 0])

# Solve and draw trajectory diagram
x0 = [1, 0, -12, 24,     -1, 0, 12, -24]
x1 = [1, 0, res.x[0], res.x[1], -1, 0, res.x[2], res.x[3]]
sol0 = solve_ivp(lambda t, state: dynamics(t, state, 0),
        t_span, x0, t_eval=t_eval, method='RK45')
sol1 = solve_ivp(lambda t, state: dynamics(t, state, 2500),
        t_span, x1, t_eval=t_eval, method='RK45')
fig = plt.figure()
ax1 = fig.add_subplot(221)
theta = np.linspace(0, np.pi*2)
ax1.plot(np.cos(theta), np.sin(theta), color='black', alpha=0.1)
ax1.plot(np.cos(sol0.y[0]), np.sin(sol0.y[0]), color='purple', alpha=0.2)
ax1.set_ylabel("$y$");ax1.set_aspect('equal')
ax2 = fig.add_subplot(222)
ax2.plot(np.cos(theta), np.sin(theta), color='black', alpha=0.1)
ax2.plot(np.cos(sol1.y[0]), np.sin(sol1.y[0]), color='purple', alpha=0.2)
ax2.set_ylabel("$y$");ax2.set_aspect('equal')
ax3 = fig.add_subplot(223)
ax3.plot(np.cos(theta), np.sin(theta), color='black', alpha=0.1)
ax3.plot(np.cos(sol0.y[0]), np.sin(sol0.y[0]), color='purple', alpha=0.2)
ax3.set_xlabel("$x$");ax3.set_ylabel("$y$");ax3.set_aspect('equal')
ax4 = fig.add_subplot(224)
ax4.plot(np.cos(theta), np.sin(theta), color='black', alpha=0.1)
ax4.plot(np.cos(sol1.y[0]), np.sin(sol1.y[0]), color='purple', alpha=0.2)
ax4.set_xlabel("$x$");ax4.set_ylabel("$y$");ax4.set_aspect('equal')
tmp = 25
ax1.plot([np.cos(sol0.y[0, tmp])], [np.sin(sol0.y[0, tmp])], 'o', color='hotpink', markersize=8)
ax1.plot([np.cos(sol0.y[4, tmp])], [np.sin(sol0.y[4, tmp])], 'o', color='steelblue', markersize=8)
ax3.plot([np.cos(sol1.y[0, tmp])], [np.sin(sol1.y[0, tmp])], 'o', color='hotpink', markersize=8)
ax3.plot([np.cos(sol1.y[4, tmp])], [np.sin(sol1.y[4, tmp])], 'o', color='steelblue', markersize=8)
ax1.set_title("$t$ = 0.25 $s$")
tmp = 75
ax2.plot([np.cos(sol0.y[0, tmp])], [np.sin(sol0.y[0, tmp])], 'o', color='hotpink', markersize=8)
ax2.plot([np.cos(sol0.y[4, tmp])], [np.sin(sol0.y[4, tmp])], 'o', color='steelblue', markersize=8)
ax4.plot([np.cos(sol1.y[0, tmp])], [np.sin(sol1.y[0, tmp])], 'o', color='hotpink', markersize=8)
ax4.plot([np.cos(sol1.y[4, tmp])], [np.sin(sol1.y[4, tmp])], 'o', color='steelblue', markersize=8)
ax2.set_title("$t$ = 0.75 $s$")
plt.show()
