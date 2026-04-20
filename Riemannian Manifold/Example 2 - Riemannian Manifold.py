import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from matplotlib.animation import FuncAnimation
import seaborn as sns
plt.rcParams.update({
    'font.family': 'Arial',
    'font.sans-serif': ['Arial'],
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
ax1 = fig.add_subplot(121)
theta = np.linspace(0, np.pi*2)
ax1.plot(np.cos(theta), np.sin(theta), color='black', alpha=0.1)
ax1.plot(np.cos(sol0.y[0]), np.sin(sol0.y[0]), color='purple', alpha=0.2)
ax1.set_ylabel("$y$");ax1.set_xlabel("$x$");ax1.set_aspect('equal')
ax2 = fig.add_subplot(122)
ax2.plot(np.cos(theta), np.sin(theta), color='black', alpha=0.1)
ax2.plot(np.cos(sol1.y[0]), np.sin(sol1.y[0]), color='purple', alpha=0.2)
ax2.set_xlabel("$x$");ax2.set_aspect('equal')
point1, = ax1.plot([], [], 'o', color='hotpink', markersize=8)
point2, = ax1.plot([], [], 'o', color='steelblue', markersize=8)
point3, = ax2.plot([], [], 'o', color='hotpink', markersize=8)
point4, = ax2.plot([], [], 'o', color='steelblue', markersize=8)

def init():
    point1.set_data([], [])
    point2.set_data([], [])
    point3.set_data([], [])
    point4.set_data([], [])
    return point1, point2, point3, point4

def update(frame):
    if frame > 0:
        point1.set_data([np.cos(sol0.y[0, frame-1])], [np.sin(sol0.y[0, frame-1])])
        point2.set_data([np.cos(sol0.y[4, frame-1])], [np.sin(sol0.y[4, frame-1])])
        point3.set_data([np.cos(sol1.y[0, frame-1])], [np.sin(sol1.y[0, frame-1])])
        point4.set_data([np.cos(sol1.y[4, frame-1])], [np.sin(sol1.y[4, frame-1])])
    return point1, point2, point3, point4

ani = FuncAnimation(
    fig=fig, func=update, frames=len(t_eval),
    init_func=init, interval=20, blit=True, repeat=True
)
plt.show()
ani.save('S1_animation.gif', writer='pillow', fps=50)
