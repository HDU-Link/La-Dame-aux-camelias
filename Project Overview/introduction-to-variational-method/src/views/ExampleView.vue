<template>
  <h2>Physical Example: Two Coupled Particles</h2>
  <p>
      Consider two particles with positions \( y_1(t) \) and \( y_2(t) \). The action functional is
  </p>
  <div class="equation-box">
      \[
      J\left[ y_1,y_2 \right] =\int_0^1{\frac{1}{2}\left( y_{1}'' \right) ^2 + \frac{1}{2}\left( y_{2}'' \right) ^2 + \frac{\mu}{2}\left( y_1-y_2 \right) ^2}\text{d}t
      \]
  </div>
  <p>
      Here, \( y_1'' \) and \( y_2'' \) represent accelerations (kinetic-like energy), while \( (y_1 - y_2)^2 \) is a coupling potential. 
      Minimizing this functional leads to the following system of fourth-order differential equations.
  </p>
  <div class="equation-box">
      \[
      \begin{cases}
          y_1^{(4)} = \mu (y_2 - y_1), \\[6pt]
          y_2^{(4)} = \mu (y_1 - y_2), \\[6pt]
          y_1(0) = 1,\; y_1(1) = -1,\; y_1'(0) = 0,\; y_1'(1) = 0, \\[6pt]
          y_2(0) = -1,\; y_2(1) = 1,\; y_2'(0) = 0,\; y_2'(1) = 0.
      \end{cases}
      \]
  </div>
  <p>
      The parameter \( \mu \ge 0 \) controls the coupling strength. 
      When \( \mu = 0 \) the particles move independently; as \( \mu \) increases, they become strongly synchronized, 
      developing boundary layers near \( t=0 \) and \( t=1 \).
  </p>
</template>