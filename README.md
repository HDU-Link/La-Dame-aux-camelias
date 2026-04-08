# 变分法求解泛函极值问题

考虑依赖于多个函数及其导数的泛函：

$$
J\left[ y_1,y_2,\cdots ,y_n \right] =\int_0^T{f\left( y_1,y_{1}^{'},y_{1}^{''},\cdots ,y_n,y_{n}^{'},y_{n}^{''} \right)}\text{d}t
$$

对于上述泛函，其极值曲线满足以下欧拉-拉格朗日方程：

$$
\frac{\partial f}{\partial y_i}-\frac{\text{d}}{\text{d}t}\left( \frac{\partial f}{\partial y_{i}^{'}} \right) +\frac{\text{d}^2}{\text{d}t^2}\left( \frac{\partial f}{\partial y_{i}^{''}} \right) =0
$$

## 例1：双质点耦合系统

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
