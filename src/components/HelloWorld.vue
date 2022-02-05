<template>
<div class="flex">
  <img :src="'http://localhost:5000/video/' + selected">
  <!-- <div v-if="show" align="left"> -->
    <!-- <div v-if="camid !== ''" align="left"> -->
      <!-- <img src="http://localhost:5000/video/0/"> -->
      <!-- <img :src="camid"> -->
      <!-- <img src="localhost:5000/video/{{ selected }}/"> -->
    <!-- </div> -->
    <!-- <div v-else align="left">
    <img alt="Vue logo" src="../assets/loadimage.png" width="720">
  </div> -->
  <!-- </div> -->
  <!-- <div v-else align="left">
    <img alt="Vue logo" src="../assets/loadimage.png" width="720">
  </div> -->
  <!-- <img src="http://localhost:5000/video/0/"> -->
  {{ video_device_list }}
  {{ selected }}
  <div>
  <button v-on:click="greet">画面表示</button>
  <select v-model="selected">
    <option v-for="item in video_device_list.devices" :key="item" :value="item.id">
      {{ item.name }}
    </option>
  </select>
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
      //     this.axios.post('/post_video_id', {
      //   video_id: this.selected
      // }).then(()=>{
        
      // })

      // this.axios.get(this.camid).then(() => {
      //   this.show = true
      // })
            // this.show = false
      // this.camid = ''
      
      // setTimeout(()=>{
      //     this.camid = "/video/" + this.selected
      // }, 500)

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
.flex{
    /*コレ追加*/
    display: flex;
    border: 1px solid #333;
    
}
.flex div{
    border: 1px solid #333;
    background: #CCC;
}
.right{
    /*コレ追加*/
    width: 200px;
}
.left{

    /*コレ追加*/
    width: calc(100% - 200px);
}
.button{
display:inline-block;/*コレ*/
}
</style>
