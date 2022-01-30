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
  <!-- <span>Selected: {{ selected }}</span> -->
  <!-- <img :src="imgSrc" fit="fill"> -->

<div v-if="show">
  <!-- <img :src="'/video/' + selected" fit="fill"> -->
  <img :src="camid" fit="fill" width="720">
  {{ '/video/' + camid }}
</div>
<!-- </div> -->
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
      video_device_list: {},
      imgSrc:'',
      show:false,
      camid:''
    }

  },
  methods:{
    greet(){
      // this.axios.get('/video/' + this.selected).then((res) =>{
      //   this.imgSrc = res.data
      // })
      this.show = true
      // this.axios.post('/post_video_id', {
      //   video_id: this.selected
      // })
      // this.show = false
      // this.axios.get('/video/' + this.selected).then((res) => {
      //   console.log(res.status)
      //   if (res.status === 200){
      //     this.show = true
      //   }
        
      // })
      }
      
    },
   created: function () {
      this.axios.get('/getvideoinput').then((res) => {
      this.video_device_list = res.data
      })
    },
    watch: {
      selected: function() {
          this.camid = "/video/" + this.selected
          this.axios.post('/post_video_id', {
        video_id: this.selected
      }).then(()=>{
        
      })

      this.axios.get(this.camid).then(() => {
        this.show = true
      })
            // this.show = false
      this.camid = ''
      
      setTimeout(()=>{
          this.camid = "/video/" + this.selected
      }, 500)

        // this.show = true
      //   this.axios.get('/video/' + this.selected).then((res) =>{
      //   this.imgSrc = res.data
      // })
      //   this.show = false
      // this.axios.get('/video/' + this.selected).then((res) => {
      //   console.log(res.status)
      //   if (res.data !== -1){
      //     this.show = true
      //   }
        
      // })
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
