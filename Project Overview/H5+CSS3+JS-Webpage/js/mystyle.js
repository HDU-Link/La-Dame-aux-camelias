const app = Vue.createApp({
data() {
    return {
        display: "EL",};
},
watch: {
    display(val) {
        this.$nextTick(() => {
            if (window.MathJax) {
                MathJax.typesetPromise();
            }
        });
    },
    immediate:true,
},
components: {
        EL:{ 
            template: `<p>The variational method seeks functions \\( y_1(t), y_2(t), \\dots, y_n(t) \\) that extremize a given functional. 
        For problems involving second derivatives, the general form is
    </p>
    <div class="equation-box">
            \\[
            J\\left[ y_1,y_2,\\cdots ,y_n \\right] =\\int_0^T{f\\left( y_1,y_{1}',y_{1}'',\\cdots ,y_n,y_{n}',y_{n}'' \\right)}\\text{d}t
            \\]
        </div>
    <p>
        The corresponding Euler-Lagrange equation, extended to include second derivatives, is
    </p>
    <div class="equation-box">
        \\[
        \\frac{\\partial f}{\\partial y_i}-\\frac{\\text{d}}{\\text{d}t}\\left( \\frac{\\partial f}{\\partial y_{i}'} \\right) +\\frac{\\text{d}^2}{\\text{d}t^2}\\left( \\frac{\\partial f}{\\partial y_{i}''} \\right) =0
        \\]
    </div>
    `},
    Example:{
        template:`<h2>Physical Example: Two Coupled Particles</h2>
        <p>
            Consider two particles with positions \\( y_1(t) \\) and \\( y_2(t) \\). The action functional is
        </p>
        <div class="equation-box">
            \\[
            J\\left[ y_1,y_2 \\right] =\\int_0^1{\\frac{1}{2}\\left( y_{1}'' \\right) ^2 + \\frac{1}{2}\\left( y_{2}'' \\right) ^2 + \\frac{\\mu}{2}\\left( y_1-y_2 \\right) ^2}\\text{d}t
            \\]
        </div>
        <p>
            Here, \\( y_1'' \\) and \\( y_2'' \\) represent accelerations (kinetic-like energy), while \\( (y_1 - y_2)^2 \\) is a coupling potential. 
            Minimizing this functional leads to the following system of fourth-order differential equations.
        </p>
        <div class="equation-box">
            \\[
            \\begin{cases}
                y_1^{(4)} = \\mu (y_2 - y_1), \\\\[6pt]
                y_2^{(4)} = \\mu (y_1 - y_2), \\\\[6pt]
                y_1(0) = 1,\\; y_1(1) = -1,\\; y_1'(0) = 0,\\; y_1'(1) = 0, \\\\[6pt]
                y_2(0) = -1,\\; y_2(1) = 1,\\; y_2'(0) = 0,\\; y_2'(1) = 0.
            \\end{cases}
            \\]
        </div>
        <p>
            The parameter \\( \\mu \\ge 0 \\) controls the coupling strength. 
            When \\( \\mu = 0 \\) the particles move independently; as \\( \\mu \\) increases, they become strongly synchronized, 
            developing boundary layers near \\( t=0 \\) and \\( t=1 \\).
        </p>
    `},
    Simulation:{
        template: `<h2>Numerical Approach: Shooting Method</h2>
        <p>
            Because the system is a boundary value problem (BVP), we convert it into an initial value problem (IVP) 
            by guessing the missing initial conditions \\( y_1''(0), y_1'''(0), y_2''(0), y_2'''(0) \\). 
            The shooting method minimizes the terminal error.
        </p>
        <div class="equation-box">
            \\[
            \\text{error} = \\bigl(y_1(1)+1\\bigr)^2 + \\bigl(y_1'(1)\\bigr)^2 + \\bigl(y_2(1)-1\\bigr)^2 + \\bigl(y_2'(1)\\bigr)^2
            \\]
        </div>`
    },
    Python:{
        template:`<h2>Python Implementation</h2>
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
            <img src="./svg/Optimization_curve_chart.svg">
        </p>
        `,
    },
    Dynamic:{
        template:`<h2>Behavior with Increasing \\( \\mu \\)</h2>
        <ul class="list">
            <li><strong>\\( \\mu = 0 \\)</strong> – Uncoupled cubic polynomials: \\( y_1(t) = 1 - 12t^2 + 24t^3 \\), \\( y_2(t) = -y_1(t) \\).</li>
            <li><strong>\\( \\mu = 100 \\)</strong> – Weak coupling: slight deviation from the uncoupled case.</li>
            <li><strong>\\( \\mu = 1000 \\)</strong> – Strong coupling: significant change in shape; shooting optimization required.</li>
            <li><strong>\\( \\mu = 2500 \\)</strong> – Very strong coupling: near-synchronization with sharp boundary layers.</li>
        </ul>
        <p>
            The competition between bending energy (\\( \\int (y_i'')^2 \\)) and potential energy (\\( \\int (y_1-y_2)^2 \\)) 
            explains the transition: large \\( \\mu \\) forces \\( y_1 \\approx y_2 \\) in the interior, while boundary conditions 
            force \\( y_1(0)=1, y_2(0)=-1 \\), leading to rapid transitions near the ends.
        </p>
        <p align="center" style="margin-top: -30px;">
            <img src="./svg/Figure_1.svg">
        </p>`
    }
    }
});
window.addEventListener('load', () => {
if (window.MathJax) {
    MathJax.typesetPromise();
}
});
app.mount('#app');

function checkVisible() {
    document.querySelectorAll('.card, .equation-box, .code-card, h1, h2, .list, p').forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight) {
            el.classList.add('show');
        }
    });
}
window.addEventListener('scroll', checkVisible);
window.addEventListener('load', checkVisible);
checkVisible();
