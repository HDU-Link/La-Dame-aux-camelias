<template>
  <div class="card">
    <div class="card-header">
      <h1 style="transition: all 0.6s ease;">Introduction to Variational Method</h1>
    </div>
    <div>
      <ul class="nav-tabs">
        <li class="nav-item">
          <router-link to="/" active-class="active">Introduction</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/example" active-class="active">Physical Example</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/numerical" active-class="active">Numerical Approach</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/code" active-class="active">Python Code</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/behavior" active-class="active">Dynamic Behavior</router-link>
        </li>
      </ul>
    </div>
    <div class="content">
      <router-view/>
    </div>
  </div>
</template>
<script>
export default {
  name: 'App',
  watch: {
    $route: {
      handler() {
        this.$nextTick(() => {
          if (window.MathJax) {
            window.MathJax.typesetPromise()
          }
        })
      },
      immediate: true
    }
  }
}
</script>
<style>
body{
    background:linear-gradient(145deg, #f9f4f0 0%, #ecebd9 100%);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem 1rem;
    line-height: 30px;
    min-height: calc(100vh - 3rem);
}
.card{
    margin: 10px;
    border-radius: 0.5rem;
    box-shadow: 0 20px 50px -10px rgba(100, 100, 50, 0.5);
    max-width: 860px;
    width: 100%;
    background-color:#FFFFFF80;
    overflow: hidden;
    transition: all 0.6s ease;
}
.card-header{
    background: linear-gradient(135deg, rgb(211, 165, 8) 0%, #a21010 100%);
    padding: 0.5rem 1rem 1rem 1rem;
    color: white;
    text-align: center;
    align-items: center;
    gap:1rem;
}
.card-header a{
    flex:1;
    text-decoration: none;
}
.content{
    padding: 0 28px 28px 28px;
}
.nav-tabs {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    border-bottom: 1px solid #ddd;
    justify-content: space-between;
}
.nav-item {
    text-align: center;
}

.nav-item a {
  display: block;
  padding: 10px 20px;
  text-decoration: none;
  color: #000;
  transition: all 0.5s ease;
}

.nav-item a.active {
    color: crimson;
    font-weight: bold;
    border-bottom: 3px solid crimson;
    background: #f9f9e8;
    transition: all 0.5s ease;
}
@media screen and (max-width:660px){
    .card-header{
        padding: 0.5rem 0.5rem;
    }
    .card-header h1{
        font-size: 18px;
        transition: all 0.6s ease;
    }
    .card{
        font-size: 14px;
    }
    .card h2{
        font-size: 16px;
        transition: all 0.6s ease;
    }
    .nav-item a{
        padding: 10px 10px;
        font-size: 12px;
    }
    .content{
        padding: 0 16px 16px 16px;
    }
    img{
        width: 100%;
    }
}
</style>
