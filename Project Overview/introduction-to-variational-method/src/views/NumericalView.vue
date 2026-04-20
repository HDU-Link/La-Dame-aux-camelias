<template>
<h2>Numerical Approach: Shooting Method</h2>
<p>
    Because the system is a boundary value problem (BVP), we convert it into an initial value problem (IVP) 
    by guessing the missing initial conditions \( y_1''(0), y_1'''(0), y_2''(0), y_2'''(0) \). 
    The shooting method minimizes the terminal error.
</p>
<div class="equation-box">
    \[
    \text{error} = \bigl(y_1(1)+1\bigr)^2 + \bigl(y_1'(1)\bigr)^2 + \bigl(y_2(1)-1\bigr)^2 + \bigl(y_2'(1)\bigr)^2
    \]
</div>
</template>