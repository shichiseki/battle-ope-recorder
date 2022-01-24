<template>
  <div class="hello">
      <button v-on:click="greet">test</button>
  <p>The button above has been clicked {{ counter }} times.</p>
  {{ message }}
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
      message: ''
    }

  },
   methods: {
    greet: function () {
      this.axios.get('/getvideoinput').then((res) => {
      this.message = res.data
      // this.rows = res.data
      // alert(res.data)
      })
    }
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
