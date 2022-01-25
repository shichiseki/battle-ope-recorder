<template>
  <div class="hello">
      <button v-on:click="greet">test</button>
  <p>The button above has been clicked {{ counter }} times.</p>
  {{ video_device_list.devices }}
  <li v-for="item in video_device_list.devices" :key="item">
    {{ item.id }}
  </li>
<div id="v-model-select-dynamic" class="demo">
  <select v-model="selected">
    <option v-for="item in video_device_list.devices" :key="item" :value="item.id">
      {{ item.name }}
    </option>
  </select>
  <span>Selected: {{ selected }}</span>
</div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      counter: 0,
      selected: '',
      video_device_list: {}
    }

  },
   created: function () {
      this.axios.get('/getvideoinput').then((res) => {
      this.video_device_list = res.data
      })
    }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
