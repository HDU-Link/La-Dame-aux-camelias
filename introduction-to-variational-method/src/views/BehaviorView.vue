<template>
<h2>Behavior with Increasing \( \mu \)</h2>
<ul class="list">
    <li><strong>\( \mu = 0 \)</strong> – Uncoupled cubic polynomials: \( y_1(t) = 1 - 12t^2 + 24t^3 \), \( y_2(t) = -y_1(t) \).</li>
    <li><strong>\( \mu = 100 \)</strong> – Weak coupling: slight deviation from the uncoupled case.</li>
    <li><strong>\( \mu = 1000 \)</strong> – Strong coupling: significant change in shape; shooting optimization required.</li>
    <li><strong>\( \mu = 2500 \)</strong> – Very strong coupling: near-synchronization with sharp boundary layers.</li>
</ul>
<p>
    The competition between bending energy (\( \int (y_i'')^2 \)) and potential energy (\( \int (y_1-y_2)^2 \)) 
    explains the transition: large \( \mu \) forces \( y_1 \approx y_2 \) in the interior, while boundary conditions 
    force \( y_1(0)=1, y_2(0)=-1 \), leading to rapid transitions near the ends.
</p>
<p align="center" style="margin-top: -30px;">
    <img src="../assets/Figure_1.svg">
</p>
</template>