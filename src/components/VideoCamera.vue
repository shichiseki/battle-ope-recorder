<template>
  <div>
    <button class="button-snap" v-on:click="toggleShow">
        <span v-if="!isCameraOpen">映像表示</span>
        <span v-else>映像停止</span>
      </button>
  <select v-model="selected" v-on:change="selectdevice">
  <option v-for="item in devices" :key="item.DeviceName" :value="item.DeviceId">
      {{ item.DeviceName }}
    </option>
  </select>
  <!-- {{ selected }} -->
  <video v-show="isCameraOpen" id="video-device" class="camera-video" ref="camera" :width="640" :height="360" autoplay playsinline ></video>
  <canvas ref="canvas" id="canvasforimg"></canvas>
  <img id="imageprocessed"/>
  <h1>
    {{ judge }}
  </h1>
  </div>
  
</template>

<script>
export default {
  name: 'Camera',
  data() {
    return {
      isCameraOpen: false,
      isPhotoTaken: false,
      devices: [],
      selected:'',
      captureTimer: '',
      width: 1920,
      height: 1080,
      interval: 500,
      judge: ''
    }
  },
  methods: {
    selectdevice (){
      this.stopCameraStream()
      this.createCameraElement()
    },
    createCameraElement () {
      const constraints = (window.constraints = {
        audio: false,
        video: {
          deviceId:this.selected,
          width: this.width,
          height: this.height
        }
      })
      navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
          this.$refs.camera.srcObject = stream
        })
        .catch(error => {
          alert(error, "May the browser didn't support or there is some errors.")
        })
    },
    stopCameraStream () {
      const tracks = this.$refs.camera.srcObject.getTracks()

      tracks.forEach(track => {
        track.stop()
      })
      console.log('CameraClosed')
    },

    toggleShow () {
      this.isCameraOpen ^= true
      console.log('toggle')
      if (this.isCameraOpen) {
        this.startCapture()
      }else{
        this.stopCapture()
      }
    },

    startCapture () {
      this.createCameraElement()
      this.captureTimer = setInterval(() => {
        this.capture()
      }, this.interval)
    },
    stopCapture (){
      this.stopCameraStream()
      clearInterval(this.captureTimer)
    },

    capture () {
      const canvas = document.getElementById('canvasforimg');
      const ctx = canvas.getContext('2d'); //canvasの描画モードを2Dに指定
      const videoElm = document.getElementById('video-device'); //相手側の映像要素
      const w = this.width
      const h = this.height
      canvas.setAttribute("width", w);
      canvas.setAttribute("height", h);
      ctx.drawImage(videoElm, 0, 0)
      const img_base64 = canvas.toDataURL('image/png');
      const fd = new FormData()
      fd.append("image", img_base64)
      this.axios.post('/img', fd).then(res => {
        // const processedimg = document.getElementById('imageprocessed')
        // processedimg.setAttribute("width", 640);
        // processedimg.setAttribute("height", 360);
        // processedimg.src = res.data
        console.log(res.data)
        this.judge = res.data
      })
        }
  },
  created: function(){
        let self = this
        navigator.mediaDevices
        .enumerateDevices()
        .then(devices => {
          devices.forEach(function(device) {
            if (device.kind === 'videoinput'){
              let device_info = {DeviceId: device.deviceId, DeviceName: device.label}
              self.devices.push(device_info)
            }
          })
        })
        .catch(error => {
          alert(error, "May the browser didn't support or there is some errors.")
        })
        this.createCameraElement()
  },  
}
</script>

<style>
#canvasforimg {
 display: none !important;
}
</style>