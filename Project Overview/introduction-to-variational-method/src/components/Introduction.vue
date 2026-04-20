<template>
  <p> The variational method seeks functions \( y_1(t), y_2(t), \dots, y_n(t) \) that extremize a given functional. 
    For problems involving second derivatives, the general form is
  </p>
  <div class="equation-box">
    \[
    J\left[ y_1,y_2,\cdots ,y_n \right] =\int_0^T{f\left( y_1,y_{1}',y_{1}'',\cdots ,y_n,y_{n}',y_{n}'' \right)}\text{d}t
    \]
  </div>
  <p>
      The corresponding Euler-Lagrange equation, extended to include second derivatives, is
  </p>
  <div class="equation-box">
    \[
    \frac{\partial f}{\partial y_i}-\frac{\text{d}}{\text{d}t}\left( \frac{\partial f}{\partial y_{i}'} \right) +\frac{\text{d}^2}{\text{d}t^2}\left( \frac{\partial f}{\partial y_{i}''} \right) =0
    \]
  </div>
</template>

<script>
export default {
  name: 'IntroSection',
}
</script>

<style>
.list{
    list-style-type: decimal;
    padding-left: 20px;
}
.list li{
    margin: 8px 0;
}
.equation-box {
    background: #f5f2e8;
    padding: 0px;
    border-radius: 12px;
    margin: 20px 0;
    overflow-x: auto;
    border-left: 4px solid #d4a017;
}
</style>