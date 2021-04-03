<template>
  <div class="md:container md:mx-auto ">
    <column-1/>
</div>
</template>

<script>
import column1  from './components/column1.vue'
export default {
  name: 'App',
  components: {
    column1
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
