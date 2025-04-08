import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# 设置行星轨道半径（单位：AU）
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
orbit_radii = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58, 19.18, 30.07]
orbit_speeds = [4.15, 1.62, 1.0, 0.53, 0.08, 0.03, 0.011, 0.006]  # 相对地球的速度

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-32, 32)
ax.set_ylim(-32, 32)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Solar System Orbits")

# 画出太阳
ax.scatter(0, 0, color='yellow', s=200, label="Sun")

# 画出行星轨道
for r in orbit_radii:
    circle = plt.Circle((0, 0), r, color='gray', fill=False, linestyle="dotted")
    ax.add_patch(circle)

# 画出行星
planets, = ax.plot([], [], 'bo', markersize=5)

# 初始化函数
def init():
    planets.set_data([], [])
    return planets,

# 更新函数
def update(frame):
    x_data = [orbit_radii[i] * np.cos(frame * orbit_speeds[i]) for i in range(len(orbit_radii))]
    y_data = [orbit_radii[i] * np.sin(frame * orbit_speeds[i]) for i in range(len(orbit_radii))]
    planets.set_data(x_data, y_data)
    return planets,

# 创建动画
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 200), init_func=init, blit=True)

# 保存动画
ani.save("solar_system_orbits.gif", writer='pillow', fps=20)
