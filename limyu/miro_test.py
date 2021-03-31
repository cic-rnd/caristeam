import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML


fig = plt.figure(figsize=(5,5))
ax = plt.gca()

plt.plot([1, 1], [0, 1], color='red', linewidth=2)
plt.plot([1, 2], [2, 2], color='red', linewidth=2)
plt.plot([2, 2], [2, 1], color='red', linewidth=2)
plt.plot([2, 3], [1, 1], color='red', linewidth=2)

plt.text(0.5, 2.5, 'S0', size=14, ha='center')
plt.text(1.5, 2.5, 'S1', size=14, ha='center')
plt.text(2.5, 2.5, 'S2', size=14, ha='center')
plt.text(0.5, 1.5, 'S3', size=14, ha='center')
plt.text(1.5, 1.5, 'S4', size=14, ha='center')
plt.text(2.5, 1.5, 'S5', size=14, ha='center')
plt.text(0.5, 0.5, 'S6', size=14, ha='center')
plt.text(1.5, 0.5, 'S7', size=14, ha='center')
plt.text(2.5, 0.5, 'S8', size=14, ha='center')
plt.text(0.5, 2.3, 'START', ha='center')
plt.text(2.5, 0.3, 'GOAL', ha='center')

ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=False, right=False, left=False, labelleft=False
                )

line, = ax.plot([0.5], [2.5], marker="o", color="g", markersize=60)

#plt.show()

theta_0 = np.array([
    [np.nan , 1 , 1 , np.nan],
    [np.nan , 1 , np.nan , 1],
    [np.nan , np.nan , 1 , 1],
    [1 , 1 , 1 , np.nan],
    [np.nan , np.nan , 1 , 1],
    [1 , np.nan , np.nan , np.nan],
    [1 , np.nan , np.nan , np.nan],
    [1 , 1 , np.nan , np.nan],
])


def simple_convert_into_pi_from(theta):
    [m, n] = theta.shape
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])

    pi = np.nan_to_num(pi)
    return pi

#pi_0 = simple_convert_into_pi_from(theta_0)

def get_next_s(pi, s):
    direction = ["up", "right", "down", "left"]
    next_direction = np.random.choice(direction, p=pi[s, :])

    if next_direction == 'up' :
        s_next = s - 3
    elif next_direction == 'right':
        s_next = s+1
    elif next_direction == 'down' :
        s_next = s+3
    elif next_direction == 'left':
        s_next = s+1
    return s_next


def goal_maze(pi):
    s = 0
    state_history = [0]

    while(1):
        next_s = get_next_s(pi, s)
        state_history.append(next_s)

        if next_s == 8:
            break
        else:
            s = next_s
    return state_history


#state_history = goal_maze(pi_0)
#print(state_history)
#print("목표지점에 이르기까지 걸린 단계 수는 >>> " + str(len(state_history) - 1))

'''
def init():
    line.set_data([], [])
    return (line,)

def animate(i):
    state = state_history[i]
    x = (state % 3) + 0.5
    y = 2.5 - int(state / 3)
    line.set_data(x, y)
    return (line,)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(state_history), interval=200, repeat=False)

HTML(anim.to_jshtml())
'''

def softmax_convert_into_pi_from_theta(theta):
    beta = 1.0
    [m, n] = theta.shape
    pi = np.zeros((m, n))

    exp_theta = np.exp(beta * theta)

    for i in range(0, m):
        pi[i, :] = exp_theta[i, :] / np.nansum(exp_theta[i, :])

    pi = np.nan_to_num(pi)
    return pi

pi_0 = softmax_convert_into_pi_from_theta(theta_0)
print(pi_0)

def get_action_and_next_s(pi, s):
    direction = ["up", "right", "down", "left"]
    next_direction = np.random.choice(direction, p=pi[s, :])

    if next_direction == 'up' :
        action = 0
        s_next = s - 3
    elif next_direction == 'right':
        action = 1
        s_next = s+1
    elif next_direction == 'down' :
        action = 2
        s_next = s+3
    elif next_direction == 'left':
        action = 3
        s_next = s+1
    return [action, s_next]

def goal_maze_ret_s_a(pi):
    s = 0
    s_a_history = [[0, np.nan]]

    while(1):
        [action, next_s] = get_action_and_next_s(pi, s)
        s_a_history[-1][1] = action

        s_a_history.append([next_s, np.nan])

        if next_s == 8:
            break
        else:
            s = next_s
    return s_a_history

s_a_history  = goal_maze_ret_s_a(pi_0)
print(s_a_history)
print("목표지점에 이르기까지 걸린 단계 수는 >>> " + str(len(s_a_history) - 1))