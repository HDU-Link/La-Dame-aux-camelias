<template>
<h2>Python Implementation</h2>
    <p>The core dynamics function converts the fourth-order system into an 8-dimensional first-order system.</p>
    <div class="code-card">
        <div class="code-header">
            <div class="window-dot"></div>
            <div class="window-dot"></div>
            <div class="window-dot"></div>
            <div class="code-title">Euclidean Space - Example 1.py</div>
        </div>
        <div class="code-content">
            <div class="line-numbers">
                1<br>2<br>3<br>4<br>5<br>6<br>7<br>8
            </div>
            <div class="code">
                <code>
<span class="keyword">import</span> numpy <span class="keyword">as</span> np<br>
<span class="keyword">def</span> <span class="function">dynamics</span>(t, state, mu):<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">return</span> np.hstack([<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;state[<span class="number">1</span>:<span class="number">4</span>],           <span class="comment"># y₁', y₁'', y₁'''</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mu*(state[<span class="number">4</span>] - state[<span class="number">0</span>]), <span class="comment"># y₁⁽⁴⁾ = μ(y₂ - y₁)</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;state[<span class="number">5</span>:<span class="number">8</span>],           <span class="comment"># y₂', y₂'', y₂'''</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mu*(state[<span class="number">0</span>] - state[<span class="number">4</span>])  <span class="comment"># y₂⁽⁴⁾ = μ(y₁ - y₂)</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;])
                </code>
            </div>
        </div>
    </div>

    <p>The shooting optimization loop solves for unknown initial conditions combined with optimization (e.g., L-BFGS-B), and the error function iterates and gradually converges.</p>

    <div class="code-card">
        <div class="code-header">
            <div class="window-dot"></div>
            <div class="window-dot"></div>
            <div class="window-dot"></div>
            <div class="code-title">Euclidean Space - Example 1.py</div>
        </div>
        <div class="code-content">
            <div class="line-numbers">
                1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13
            </div>
            <div class="code">
                <code>
<span class="keyword">from</span> scipy.optimize <span class="keyword">import</span> minimize<br>
<span class="keyword">from</span> scipy.integrate <span class="keyword">import</span> solve_ivp<br>
<span class="keyword">def</span> <span class="function">errors</span>(x, mu):<br>
&nbsp;&nbsp;&nbsp;&nbsp;x0 = [<span class="number">1</span>, <span class="number">0</span>, x[<span class="number">0</span>], x[<span class="number">1</span>], -<span class="number">1</span>, <span class="number">0</span>, x[<span class="number">2</span>], x[<span class="number">3</span>]]<br>
&nbsp;&nbsp;&nbsp;&nbsp;sol = solve_ivp(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">lambda</span> t, state: dynamics(t, state, mu),<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(<span class="number">0</span>, <span class="number">1</span>), x0, t_eval=np.linspace(<span class="number">0</span>, <span class="number">1</span>, <span class="number">100</span>), method=<span class="string">'RK45'</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">return</span> (sol.y[<span class="number">0</span>,-<span class="number">1</span>]+<span class="number">1</span>)**<span class="number">2</span> + sol.y[<span class="number">1</span>,-<span class="number">1</span>]**<span class="number">2</span> + \<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(sol.y[<span class="number">4</span>,-<span class="number">1</span>]-<span class="number">1</span>)**<span class="number">2</span> + sol.y[<span class="number">5</span>,-<span class="number">1</span>]**<span class="number">2</span><br>
<span class="comment"># Optimize for μ = 2500</span><br>
res = minimize(<span class="keyword">lambda</span> x: errors(x, <span class="number">2500</span>),<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<span class="number">0</span>,<span class="number">0</span>,<span class="number">0</span>,<span class="number">0</span>], method=<span class="string">'L-BFGS-B'</span>)
                </code>
            </div>
        </div>
    </div>
    <p align="center" style="margin-top: -30px;">
        <img src="../assets/Optimization_curve_chart.svg">
    </p>
</template>
<style>
.code-card {
    background: #1e1e2f;
    border-radius: 1rem;
    width: 100%;
    box-shadow: 0 5px 30px rgba(0,0,0,0.6);
    overflow: hidden;
    transition: all 0.5s;
    margin: 24px 0;
}

.code-header {
    background: #2d2d3a;
    padding: 0.6rem 1.2rem;
    display: flex;
    gap: 0.6rem;
    border-bottom: 1px solid #3c3c4a;
    align-items: center;
}

.window-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #ff5f56;
    transition: all 0.5s;
}
.window-dot:nth-child(2) { background: #ffbd2e; }
.window-dot:nth-child(3) { background: #27c93f; }

.code-title {
    margin-left: auto;
    font-family: 'Fira Code', 'Cascadia Code', 'Monaco', monospace;
    font-size: 0.75rem;
    color: #a0a0b0;
    letter-spacing: 0.5px;
}

.code-content {
    display: flex;
    font-family: 'Fira Code', 'Cascadia Code', 'Monaco', 'Courier New', monospace;
    font-size: 0.85rem;
    line-height: 1.6;
    background: #1e1e2f;
    color: #e4f0fb;
    overflow-x: auto;
}

.line-numbers {
    text-align: right;
    padding: 1rem 0.8rem;
    background: #181825;
    color: #6a6a7a;
    user-select: none;
    border-right: 1px solid #2d2d3a;
    font-size: 0.85rem;
    line-height: 1.6;
}

.code {
    padding: 1rem 1.2rem;
    overflow-x: auto;
    background: #1e1e2f;
    color: #e4f0fb;
    line-height: 1.6;
    font-size: 0.85rem;
    width: 100%;
}

.code code {
    font-family: inherit;
}

.keyword { color: #c792ea; }
.function { color: #82aaff; }
.string { color: #c3e88d; }
.comment { color: #546e7a; font-style: italic; }
.number { color: #f78c6c; }
@media screen and (max-width:660px){
    .line-numbers {
        font-size: 0.65rem;
        padding: 0.8rem 0.5rem;
    }
    .code {
        padding: 0.8rem;
        font-size: 0.7rem;
    }
    img{
        width: 100%;
    }
}
</style>