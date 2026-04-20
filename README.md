## 📚 变分法求解泛函极值问题

考虑依赖于多个函数及其导数的泛函：

$$
J\left[ y_1,y_2,\cdots ,y_n \right] =\int_0^T{f\left( y_1,y_{1}^{'},y_{1}^{''},\cdots ,y_n,y_{n}^{'},y_{n}^{''} \right)}\text{d}t
$$

对于上述泛函，其极值曲线满足以下欧拉-拉格朗日方程：

$$
\frac{\partial f}{\partial y_i}-\frac{\text{d}}{\text{d}t}\left( \frac{\partial f}{\partial y_{i}^{'}} \right) +\frac{\text{d}^2}{\text{d}t^2}\left( \frac{\partial f}{\partial y_{i}^{''}} \right) =0
$$

## 📝 例1：双质点耦合系统

考虑以下泛函（两个耦合的质点系统）

$$
J\left[ y_1,y_2 \right] =\int_0^1{\frac{1}{2}\left( y_{1}^{''} \right) ^2+}\frac{1}{2}\left( y_{2}^{''} \right) ^2+\frac{\mu}{2}\left( y_1-y_2 \right) ^2\text{d}t
$$

### 物理意义

- $y_1(t)$ 和 $y_2(t)$ 分别表示两个质点的位置
- $y_1''$ 和 $y_2''$ 表示加速度（与动能相关）
- $(y_1 - y_2)^2$ 表示弹性势能（耦合项）

### 欧拉-拉格朗日方程

$$
\quad y_1^{(4)} = \mu (y_2 - y_1), \quad \quad y_2^{(4)} = \mu (y_1 - y_2)
$$

给定边值，考虑以下问题：

$$
\begin{cases}
y_1^{(4)} = \mu (y_2 - y_1), \\
y_2^{(4)} = \mu (y_1 - y_2), \\
y_1(0) = 1,\quad y_1(1) = -1,\quad y_1'(0) = 0,\quad y_1'(1) = 0, \\
y_2(0) = -1,\quad y_2(1) = 1,\quad y_2'(0) = 0,\quad y_2'(1) = 0.
\end{cases}
$$

当 $\mu$ 从 0 增加到 $\infty$，系统从"独立运动"连续过渡到"强制同步"，数值求解难度也会相应增加

## 🧩 项目结构

```plaintext
La-Dame-aux-camelias/
├── Euclidean Space/          # 欧氏空间仿真示例
│   ├── Example 1 - Euclidean Space.py # 考虑位置协同问题，绘制不同参数下智能体位置-时间轨迹曲线、优化曲线（绘图输出下同）
│   ├── Example 2 - Euclidean Space.py # 考虑位置协同问题
│   ├── Example 3 - Euclidean Space.py # 考虑速度协同问题
│   ├── Example 4 - Euclidean Space.py # 考虑位置协同问题
│   └── Example 5 - Euclidean Space.py # 考虑合作竞争网络多智能体的协同避障问题
├── Riemannian Manifold/      # 黎曼流形仿真示例
│   ├── Example 1 - Riemannian Manifold.py
│   └── Example 2 - Riemannian Manifold.py
├── Project Overview/         # 变分法简介网页
│   ├── H5+CSS3+JS-Webpage/   # 基于H5+CSS3+JS开发的简介页面
│   │   ├── Introduction to Variational Method.html
│   │   ├── css/
│   │   │   └──mystyle.css    # 样式文件
│   │   ├── js/
│   │   │   └──myscript.js    # 交互逻辑
│   │   └── svg/
│   │       ├──Figure_1.svg   # 不同参数下智能体位置-时间轨迹曲线
│   │       └──Optimization_curve_chart.svg # 优化曲线
│   └── introduction-to-variational-method/ # 基于Vue开发的简介页面
│       ├── public/           # 静态资源
│       │   └── index.html
│       ├── src/              # 源代码
│       │   ├── main.ts       # 入口文件
│       │   ├── App.vue       # 根组件
│       │   ├── assets/       # 静态资源
│       │   ├── components/   # 公共组件
│       │   ├── router/       # 路由配置
│       │   ├── store/        # Vuex状态管理
│       │   └── views/        # 页面视图
│       ├── package.json      # 依赖配置
│       ├── vue.config.js     # Vue CLI配置
│       └── README.md         # 安装依赖与开发构建说明
└── README.md                 # 项目说明
```
