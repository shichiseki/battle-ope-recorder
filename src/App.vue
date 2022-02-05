<template>
<div>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <Camera/>
</div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Camera from './components/VideoCamera.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Camera
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
