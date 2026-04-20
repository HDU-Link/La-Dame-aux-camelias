<template>
  <h2>Behavior with Increasing \( \mu \)</h2>
  <ul class="list">
    <li v-for="item in mu.list" :key="item.name">
      <strong>{{ item.name }}</strong> – {{ item.value }}
    </li>
  </ul>
  <p>
    The competition between bending energy (\( \int (y_i'')^2 \)) and potential energy (\( \int (y_1-y_2)^2 \)) 
    explains the transition: large \( \mu \) forces \( y_1 \approx y_2 \) in the interior, while boundary conditions 
    force \( y_1(0)=1, y_2(0)=-1 \), leading to rapid transitions near the ends.
  </p>
  <p align="center" style="margin-top: -30px;">
    <img src="../assets/Figure_1.svg" alt="Figure 1">
  </p>
</template>

<script setup>
import { ref, reactive, inject, onMounted } from "vue";
const axios = inject("axios");
const mu = reactive({ list: [] });
onMounted(() => {
  getJson();
});
function getJson() {
  axios.get("/data/parameter.json")
    .then(function(response) {
      mu.list = response.data;
    })
    .catch(function(error) {
      console.error("Failed to load parameter.json:", error);
    });
}
</script>