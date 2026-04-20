import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, rcParams

rcParams['font.family'] = 'Arial'
rcParams['font.size'] = 12
t_span = (0, 1); t_eval = np.linspace(0, 1, 100)

def log_map(qi, qj):
    cos_theta = np.clip(np.dot(qi, qj), -1.0, 1.0)
    theta = np.arccos(cos_theta)
    if theta < 1e-10:
        return np.zeros(3)
    return theta / np.sqrt(1 - cos_theta**2) * (qj - cos_theta * qi)

def dynamics_core(t, state, forces=None):
    n = len(state) // 12
    derivatives = np.zeros_like(state)
    
    if forces is None:
        forces = [np.zeros(n) for _ in range(n)]
    
    for i in range(n):
        idx = i * 12
        q = state[idx:idx+3]
        v = state[idx+3:idx+6]
        a = state[idx+6:idx+9]
        j = state[idx+9:idx+12]
        force = forces[i] if i < len(forces) else np.zeros(3)
        
        derivatives[idx:idx+3] = v
        derivatives[idx+3:idx+6] = a
        derivatives[idx+6:idx+9] = j
        R_term = np.dot(j,v)*v - np.dot(v,v)*j - 3*np.dot(v,v)*np.dot(v,a)*q
        derivatives[idx+9:idx+12] = -R_term + force - (np.dot(v,v)*a +
            5*np.dot(v,a)*v + (4*np.dot(j,v) + 3*np.dot(a,a) + np.dot(v,v)**2) * q)
    return derivatives

def dynamics(t, state):
    return dynamics_core(t, state)

def dynamics_aggregation(t, state):
    n = len(state) // 12
    forces = []
    for i in range(n):
        qi = state[i*12:i*12+3]
        force = np.zeros(n)
        for k in range(n):
            if k != i:
                qk = state[k*12:k*12+3]
                force += 10*log_map(qi, qk)
        forces.append(force)
    return dynamics_core(t, state, forces)


# Initial condition
q1_0 = np.array([1.0, 0.0, 0.0])
q2_0 = np.array([0.0, 1.0, 0.0])
q3_0 = np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0.0])
v1_0 = np.array([0.0, 0.0, np.pi/2])
v2_0 = np.array([0.0, 0.0, np.pi/2])
v3_0 = np.array([0.0, 0.0, np.pi/2])

D1_0 = np.zeros(3)
D2_0 = np.zeros(3)
D3_0 = np.zeros(3)
s1_0 = np.zeros(3)
s2_0 = np.zeros(3)
s3_0 = np.zeros(3)

a1_0 = D1_0-q1_0*np.linalg.norm(v1_0)**2
a2_0 = D2_0-q2_0*np.linalg.norm(v2_0)**2
a3_0 = D3_0-q3_0*np.linalg.norm(v3_0)**2
j1_0 = s1_0-3*np.dot(v1_0,D1_0)*q1_0-v1_0*np.linalg.norm(v1_0)**2
j2_0 = s2_0-3*np.dot(v2_0,D2_0)*q2_0-v2_0*np.linalg.norm(v2_0)**2
j3_0 = s3_0-3*np.dot(v3_0,D3_0)*q3_0-v3_0*np.linalg.norm(v3_0)**2

initial_state = np.concatenate([
    q1_0, v1_0, a1_0, j1_0,
    q2_0, v2_0, a2_0, j2_0,
    q3_0, v3_0, a3_0, j3_0
])
'''
# Shooting method for initial value
iterations = [];errors_list = []

def errors(x):
    initial_value = [1, 0, 0,   0, 0, np.pi/2,  0, x[0], x[1],  0, x[2], x[3],
    0, 1, 0,   0, 0, np.pi/2,  x[4], 0, x[5],  x[6], 0, x[7],
    np.sqrt(2)/2, np.sqrt(2)/2, 0,   0, 0, np.pi/2,  x[8], -x[8], x[9],  x[10], -x[10], x[11]]
    sol = solve_ivp(dynamics_aggregation, t_span, initial_value, t_eval=t_eval, method='RK45')
    err = ((sol.y[0,-1])**2+(sol.y[1,-1])**2+(sol.y[2,-1]-1)**2
           +(sol.y[12,-1])**2+(sol.y[13,-1])**2+(sol.y[14,-1]-1)**2
           +(sol.y[24,-1])**2+(sol.y[25,-1])**2+(sol.y[26,-1]-1)**2)
    return err

def call(x):
    iterations.append(len(iterations) + 1)
    errors_list.append(errors(x))
    
res = minimize(errors, np.zeros(12), callback = call, method='Nelder-Mead')
print(res.fun)

# Optimization curve chart
fig = plt.figure("Optimization curve chart")
plt.plot(iterations, errors_list, '-o', markersize=4)
plt.xlabel("Number of iterations")
plt.ylabel("Value of error function")
plt.yscale('log')
plt.show()

initial_state = [1, 0, 0,   0, 0, np.pi/2,  0, res.x[0], res.x[1],  0, res.x[2], res.x[3],
0, 1, 0,   0, 0, np.pi/2,  res.x[4], 0, res.x[5],  res.x[6], 0, res.x[7],
np.sqrt(2)/2, np.sqrt(2)/2, 0,   0, 0, np.pi/2,  res.x[8], -res.x[8], res.x[9],  res.x[10], -res.x[10], res.x[11]]
'''
# Solve ODE
sol = solve_ivp(dynamics_aggregation, t_span, initial_state, t_eval=t_eval, method='RK45')
t = sol.t
y = sol.y
q1_traj = y[0:3, :].T        # Position of Agent 1
q2_traj = y[12:15, :].T      # Position of Agent 2
q3_traj = y[24:27, :].T      # Position of Agent 3

# Figure
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')

# Parameters of sphere
n_points = 50; r = 1
phi = np.linspace(0, np.pi, n_points)
theta = np.linspace(0, 2 * np.pi, n_points)
phi, theta = np.meshgrid(phi, theta)
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Plot a spherical surface
u = y*0.8 + z
value = (u - u.min()) / (u.max() - u.min())
surf = ax.plot_surface(x, y, z, 
    facecolors = cm.plasma(value),
    linewidth = 0.05, edgecolor = "white",
    antialiased = True, shade = False,
    alpha = 0.6, zorder = 2
)
# Plot the endpoints
ax.plot(q1_traj[0, 0], q1_traj[0, 1], q1_traj[0, 2],
        marker = 'o', color = 'crimson',
        markeredgecolor = 'w', markersize = 6, zorder = 5)
ax.plot(q2_traj[0, 0], q2_traj[0, 1], q2_traj[0, 2],
        marker = 'o', color = 'steelblue',
        markeredgecolor = 'w', markersize = 6, zorder = 5)
ax.plot(q3_traj[0, 0], q3_traj[0, 1], q3_traj[0, 2],
        marker = 'o', color = 'c',
        markeredgecolor = 'w', markersize = 6,  zorder = 5)
ax.plot(q1_traj[-1, 0], q1_traj[-1, 1], q1_traj[-1, 2],
        marker = 'o', color = 'crimson',
        markeredgecolor = 'w', markersize = 6, zorder = 5)
ax.plot(q2_traj[-1, 0], q2_traj[-1, 1], q2_traj[-1, 2],
        marker = 'o', color = 'steelblue',
        markeredgecolor = 'w', markersize = 6, zorder = 5)
ax.plot(q3_traj[-1, 0], q3_traj[-1, 1], q3_traj[-1, 2],
        marker = 'o', color = 'c',
        markeredgecolor = 'w', markersize = 6,  zorder = 5)

# Plot the trajectories
ax.plot(q1_traj[:, 0], q1_traj[:, 1], q1_traj[:, 2], 
        'w', linewidth=2, label='Agent 1', alpha=0.8, zorder = 4)
ax.plot(q2_traj[:, 0], q2_traj[:, 1], q2_traj[:, 2], 
        'w', linewidth=2, label='Agent 2', alpha=0.8, zorder = 4)
ax.plot(q3_traj[:, 0], q3_traj[:, 1], q3_traj[:, 2], 
        'w', linewidth=2, label='Agent 3', alpha=0.8, zorder = 4)

ax.grid(True, alpha=0.3)
ax.set_xticks(np.linspace(-1,1,5))
ax.set_yticks(np.linspace(-1,1,5))
ax.set_zticks(np.linspace(-1,1,5))
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.view_init(elev=15, azim=45)
plt.tight_layout()
plt.show()
