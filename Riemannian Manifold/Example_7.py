import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, rcParams

rcParams['font.family'] = 'Arial'
rcParams['font.size'] = 12
t_span = (0, 1); t_eval = np.linspace(0, 1, 100)

def hat(v):
    return np.array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])

def vee(Omega):
    return np.array([Omega[2,1], Omega[0,2], Omega[1,0]])

def phi(R):
    return np.arccos(np.clip(1/2*(np.trace(R)-1), -1, 1))

def log_map(Ri, Rj):
    R = Ri.T @ Rj
    if np.sin(phi(R)) < 1e-8:
        return np.zeros(3)
    else:
        return phi(R)/np.sin(phi(R))*vee(R - R.T)

def dynamics_core(t, state, forces=None):
    n = len(state) // 18
    derivatives = np.zeros_like(state)
    
    if forces is None:
        forces = [np.zeros(3) for _ in range(n)]
    
    for i in range(n):
        idx = i * 18
        Ri = state[idx:idx+9].reshape(3,3)
        Xi = state[idx+9:idx+12]
        Vi = state[idx+12:idx+15]
        Ai = state[idx+15:idx+18]
        force = forces[i] if i < len(forces) else np.zeros(3)
        
        DRi = Ri @ hat(Xi)
        derivatives[idx:idx+9] = DRi.flatten()
        derivatives[idx+9:idx+12] = Vi
        derivatives[idx+12:idx+15] = Ai
        derivatives[idx+15:idx+18] = -force-hat(Xi) @ (hat(Vi) @ Xi)
    return derivatives

def dynamics(t, state):
    return dynamics_core(t, state)

def dynamics_aggregation(t, state):
    n = len(state) // 18
    forces = []
    for i in range(n):
        Ri = state[i*18:i*18+9].reshape(3,3)
        force = np.zeros(3)
        for j in range(n):
            if j != i:
                Rj = state[j*18:j*18+9].reshape(3,3)
                force += 10*log_map(Ri, Rj)
        forces.append(force)
    return dynamics_core(t, state, forces)


# Initial condition
R1_0 = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1])
R2_0 = np.array([0, -1, 0, 1, 0, 0, 0, 0, 1])
R3_0 = np.array([np.sqrt(2)/2, -np.sqrt(2)/2, 0,
                 np.sqrt(2)/2, np.sqrt(2)/2, 0,
                 0, 0, 1])
X1_0 = np.array([0, -np.pi/2, 0])
X2_0 = np.array([0, -np.pi/2, 0])
X3_0 = np.array([0, -np.pi/2, 0])
# Shooting method for initial value
iterations = [];errors_list = []

def errors(x):
    initial_value = np.concatenate([
        R1_0, X1_0, x[0:6],
        R2_0, X2_0, x[6:12],
        R3_0, X3_0, x[12:18]
    ])
    sol = solve_ivp(dynamics_aggregation, t_span, initial_value,
                    t_eval=t_eval, method='RK45')
    err = ((sol.y[0,-1])**2+(sol.y[3,-1])**2+(sol.y[6,-1]-1)**2
           +(sol.y[18,-1])**2+(sol.y[21,-1])**2+(sol.y[24,-1]-1)**2
           +(sol.y[36,-1])**2+(sol.y[39,-1])**2+(sol.y[42,-1]-1)**2)
    return err

def call(x):
    iterations.append(len(iterations) + 1)
    errors_list.append(errors(x))
    
res = minimize(errors, np.zeros(18), callback = call)
print("error value:", res.fun)

# Optimization curve chart
fig = plt.figure("Optimization curve chart")
plt.plot(iterations, errors_list, '-o', markersize=4)
plt.xlabel("Number of iterations")
plt.ylabel("Value of error function")
plt.yscale('log')
plt.show()

initial_state = np.concatenate([
    R1_0, X1_0, res.x[0:6],
    R2_0, X2_0, res.x[6:12],
    R3_0, X3_0, res.x[12:18]
])
# Solve ODE
sol = solve_ivp(dynamics_aggregation, t_span, initial_state,
                t_eval=t_eval, method='RK45')
t = sol.t
y = sol.y
q1_traj = y[0:9:3, :].T        # Position of Agent 1
q2_traj = y[18:27:3, :].T      # Position of Agent 2
q3_traj = y[36:45:3, :].T      # Position of Agent 3

# Figure_1 (Positional coordination)
fig = plt.figure("Positional coordination", figsize=(5, 5))
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

# Figure_2 (Control group)
fig = plt.figure("Control group", figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')
# Plot a spherical surface
surf = ax.plot_surface(x, y, z, 
    facecolors = cm.plasma(value),
    linewidth = 0.05, edgecolor = "white",
    antialiased = True, shade = False,
    alpha = 0.6, zorder = 2
)

V1_0 = np.zeros(3)
V2_0 = np.zeros(3)
V3_0 = np.zeros(3)
A1_0 = np.zeros(3)
A2_0 = np.zeros(3)
A3_0 = np.zeros(3)

# Solve the equations
initial_state = np.concatenate([
    R1_0, X1_0, V1_0, A1_0,
    R2_0, X2_0, V2_0, A2_0,
    R3_0, X3_0, V3_0, A3_0
])
sol = solve_ivp(dynamics, t_span, initial_state,
                t_eval=t_eval, method='RK45')
t = sol.t
y = sol.y
q1_traj = y[0:9:3, :].T        # Position of Agent 1
q2_traj = y[18:27:3, :].T      # Position of Agent 2
q3_traj = y[36:45:3, :].T      # Position of Agent 3

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
