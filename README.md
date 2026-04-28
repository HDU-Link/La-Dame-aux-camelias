## 📚 多智能体协同避障变分问题的相关研究

考虑依赖于多个函数及其导数的泛函：

$$
J\left[ y_1,y_2,\cdots ,y_n \right] =\int_0^T{f\left( y_1,y_{1}',y_{1}'',\cdots ,y_n,y_{n}',y_{n}'' \right)}\text{d}t
$$

对于上述泛函，其极值曲线满足以下欧拉-拉格朗日方程：

$$
\frac{\partial f}{\partial y_i}-\frac{\text{d}}{\text{d}t}\left( \frac{\partial f}{\partial y_{i}'} \right) +\frac{\text{d}^2}{\text{d}t^2}\left( \frac{\partial f}{\partial y_{i}''} \right) =0
$$

## 📝 例1：双质点耦合系统（位置协同）

考虑以下泛函

$$
J\left[ y_1,y_2 \right] =\int_0^1{\frac{1}{2}\left( y_{1}'' \right) ^2+}\frac{1}{2}\left( y_{2}'' \right) ^2+\frac{\mu}{2}\left( y_1-y_2 \right) ^2\text{d}t
$$

其中：

- $y_1(t)$ 和 $y_2(t)$ 分别表示两个质点的位置
- $y_1''$ 和 $y_2''$ 表示加速度（与动能相关）
- $(y_1 - y_2)^2$ 表示弹性势能（耦合项）

求解该泛函极值，得到相应的欧拉-拉格朗日方程为

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

当 $\mu$ 从 0 增加到 $\infty$，系统从"独立运动"连续过渡到"强制同步"，数值求解难度也会相应增加。

在 `Example_1.py` 中给出不同 $\mu$ 下对应的 $y-t$ 图、 $y'-t$ 图、以及利用打靶法寻找初值的优化曲线。

在 `Example_2.py` 用 $\theta$ 替换问题中的 $y$ ，给出坐标为 $(\cos\theta, \sin\theta)$ 相应的 $y-x$ 动画演示、关键时间节点定格位置图。

在Project Overview中基于H5+CSS3+JS开发/Vue开发的网页中，给出了本例实现的具体详细介绍（英文版），二者在内容上无本质区别，仅是本人网页设计与开发的初次尝试和练习。

## 📝 例2：双质点耦合系统（速度协同）

考虑以下泛函

$$
J\left[ y_1,y_2 \right] =\int_0^1{\frac{1}{2}\left( y_{1}'' \right) ^2+}\frac{1}{2}\left( y_{2}'' \right) ^2+\frac{\mu}{2}\left( y_1'-y_2' \right) ^2\text{d}t
$$

其中：

- $y_1(t)$ 和 $y_2(t)$ 分别表示两个质点的位置
- $y_1''$ 和 $y_2''$ 表示加速度（与动能相关）
- $(y_1' - y_2')^2$ 表示速度差耦合项


对泛函 $J[y_1, y_2]$ 求变分，可得如下欧拉-拉格朗日方程组：

$$
\quad y_1^{(4)} = \mu (y_1'' - y_2''), \quad \quad y_2^{(4)} = \mu (y_2'' - y_1'')
$$

给定边值，考虑以下问题：

$$
\begin{cases}
y_1^{(4)} = \mu (y_1'' - y_2''), \\
y_2^{(4)} = -\mu (y_1'' - y_2''), \\
y_1(0) = 1,\quad y_1(1) = -1,\quad y_1'(0) = 0,\quad y_1'(1) = 0, \\
y_2(0) = -1,\quad y_2(1) = 1,\quad y_2'(0) = 0,\quad y_2'(1) = 0.
\end{cases}
$$

随 $\mu$ 增大，方程呈现刚性（高阶导数与强耦合项竞争），需要更精细的数值方法。

在 `Example_3.py` 中给出不同 $\mu$ 下对应的 $y-t$ 图、 $y'-t$ 图、以及利用打靶法寻找初值的优化曲线。

## 📝 例3：单质点避障

考虑以下泛函

$$
\begin{aligned}
&J\left[ p\left( x,y \right) \right]= \int_0^1{\frac{1}{2}\left[ \left( p'' \right)^2 + \mu \Psi \left( p,p_0 \right) \right]}\text{d}t \\
&= J\left[ x,y \right] = \int_0^1{\frac{1}{2}\left[ \left( x'' \right)^2 + \left( y'' \right)^2 + \mu \frac{1}{\left( x-x_0 \right)^2 + \left( y-y_0 \right)^2} \right]}\text{d}t
\end{aligned}
$$

其中：

- $(x(t),y(t))$ 是质点 $p(t)$ 的位置坐标， $(x_0,y_0)$ 是障碍物 $p_0$ 的位置坐标
- $x''$ 和 $y''$ 表示加速度（与动能相关）
- $\Psi$ 是避障人工势函数（artificial potential function, APF），这里选取了 $\Psi \left( p,p_0 \right) =\left( p-p_0 \right) ^{-2} $

对泛函 $J[x,y]$ 求变分，可得如下欧拉-拉格朗日方程组：

$$
\quad 
x^{(4)} = \mu \cdot \frac{(x - x_0)}{\left[(x - x_0)^2 + (y - y_0)^2\right]^2},
\quad \quad 
y^{(4)} = \mu \cdot \frac{(y - y_0)}{\left[(x - x_0)^2 + (y - y_0)^2\right]^2}
$$

给定边值，选取静态障碍物位置为坐标原点 $p_0(0,0)$，考虑以下问题：

$$
\begin{cases}
x^{(4)} = \mu \cdot \frac{x}{\left(x^2 + y^2\right)^2}, \\
y^{(4)} = \mu \cdot \frac{y}{\left(x^2 + y^2\right)^2}, \\
x(0) = -1, \quad x(1) = 1, \quad x'(0) = 0, \quad x'(1) = 0, \\
y(0) = 0, \quad y(1) = 0, \quad y'(0) = 0, \quad y'(1) = 0,
\end{cases}
$$

随 $\mu$ 增大，方程呈现刚性，表现为质点轨迹在靠近障碍物处急剧弯曲，需要更精细的数值方法。

在 `Example_4.py` 中给出不同 $\mu$ 下对应的 $y-x$ 图以及利用打靶法寻找初值的优化曲线。

## 📝 例4：多智能体协同避障（位置协同+避障）

考虑以下泛函

$$
J\left[ p_1,p_2,p_3,p_4 \right] =\frac{1}{2}\int_0^1{\sum_{i=1}^4{\left[ \left( p_i'' \right) ^2+\Psi \left( p_i,p_0 \right) +\sum_{j\in \mathcal{N}_i}{\Phi \left( p_i,p_j \right)} \right]}\text{d}t}
$$

其中：

- $p_i(t) = (x_i(t), y_i(t))$ 表示第 $i$ 个质点的位置坐标
- $p_i''$ 表示加速度（与动能相关）
- $\Psi(p_i, p_0)$ 是避障人工势函数，这里选取 $\Psi(p_i, p_0) = \dfrac{\kappa}{1 + (p_i - p_0)^2}$
- $\Phi(p_i, p_j)$ 是智能体之间的协同势函数，这里选取 $\Phi(p_i, p_j) = \mu (p_i - p_j)^2$
- $\mathcal{N}_i$ 表示第 $i$ 个智能体的邻居集合

设障碍物位置为 $p_0(0,0)$，对泛函 $J[p_1, p_2, p_3, p_4]$ 求变分，可得如下欧拉-拉格朗日方程组：

$$
x_i^{(4)} = \frac{\kappa x_i}{\left(1+x_i^2 + y_i^2\right)^2} + \mu \cdot \sum_{j\in \mathcal{N}_i} (x_j - x_i), \quad y_i^{(4)} = \frac{\kappa y_i}{\left(1+x_i^2 + y_i^2\right)^2} + \mu \cdot \sum_{j\in \mathcal{N}_i} (y_j - y_i), \quad i = 1,2,3,4
$$

给定边值，设邻居集 $\mathcal{N}_1=\mathcal{N}_2=$ &lbrace; $1,2$ &rbrace; , $\mathcal{N}_3=\mathcal{N}_4=$ &lbrace; $3,4$ &rbrace; ， 考虑以下问题：

$$
\begin{cases}
x_i^{(4)} = \frac{\kappa x_i}{\left(1+x_i^2 + y_i^2\right)^2} + \mu \cdot \sum_{j\in \mathcal{N}_i} (x_j - x_i), \\
y_i^{(4)} = \frac{\kappa y_i}{\left(1+x_i^2 + y_i^2\right)^2} + \mu \cdot \sum_{j\in \mathcal{N}_i} (y_j - y_i), \\
x_i'(0) = 0, \quad x_i'(1) = 0, \quad y_i'(0) = 0, \quad y_i'(1) = 0, \quad i = 1,2,3,4, \\
x_1(0) = -1, \quad x_1(1) = 1, \quad y_1(0) = 2, \quad y_1(1) = 2,\\
x_2(0) = -1, \quad x_2(1) = 1, \quad y_2(0) = 1, \quad y_2(1) = 1,\\
x_3(0) = -1, \quad x_3(1) = 1, \quad y_3(0) = -1, \quad y_3(1) = -1,\\
x_4(0) = -1, \quad x_4(1) = 1, \quad y_4(0) = -2, \quad y_4(1) = -2
\end{cases}
$$

随 $\kappa$ 和 $\mu$ 增大，系统呈现更强的耦合与刚性，表现为智能体轨迹在靠近障碍物处弯曲，同时相互之间保持编队或避免碰撞，需要更精细的数值方法。

在 `Example_5.py` 中给出普通避障、协同避障的两幅图可进行对比，以及利用打靶法寻找初值的优化曲线。


## 📝 例5：黎曼流形上的多智能体协同避障变分问题

考虑以下泛函

$$
J\left[ y_1,y_2 \right] =\int_0^1{\frac{1}{2}\left( y_{1}'' \right) ^2+}\frac{1}{2}\left( y_{2}'' \right) ^2+\frac{\mu}{2}\left( y_1-y_2 \right) ^2\text{d}t
$$

其中：

- $y_1(t)$ 和 $y_2(t)$ 分别表示两个质点的位置
- $y_1''$ 和 $y_2''$ 表示加速度（与动能相关）
- $(y_1 - y_2)^2$ 表示弹性势能（耦合项）

求解该泛函极值，得到相应的欧拉-拉格朗日方程为

$$
\quad y_1^{(4)} = \mu (y_2 - y_1), \quad \quad y_2^{(4)} = \mu (y_1 - y_2)
$$

在 `Example_6.py` 中给出不同 $\mu$ 下对应的智能体运动轨迹曲线。

在 `Example_7.py` 用李群约化方程后，进一步求解边值问题。
## 🧩 项目结构

```plaintext
La-Dame-aux-camelias/
├── Euclidean Space/          # 欧氏空间仿真示例
│   ├── Example_1.py          # 考虑一维位置协同问题，定义基本配置类
│   ├── Example_2.py          # 演示一维位置协同问题的轨迹动画
│   ├── Example_3.py          # 考虑一维速度协同问题
│   ├── Example_4.py          # 考虑二维单质点避障问题
│   └── Example_5.py          # 考虑二维多智能体协同避障问题
├── Riemannian Manifold/      # 黎曼流形仿真示例
│   ├── Example_6.py          # 考虑三维多智能体协同问题
│   └── Example_7.py          # 考虑协同问题在李群上的约化方程
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
