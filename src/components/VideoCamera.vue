<template>
  <!-- <div class="camera">
    <div class="wrapper">
      <button @click="this.$parent.showCamera = false" class="button-close">x</button>
       <button class="button-snap" @click="toggleCamera()">
        <span v-if="!isCameraOpen">Open Camera</span>
        <span v-else>Close Camera</span>
      </button>
       <div class="video-container">
        <video v-show="isCameraOpen" class="camera-video" ref="camera" :width="450" :height="337" autoplay playsinline ></video>
        <canvas id="photoTaken" v-show="isPhotoTaken" class="canvas-photo" ref="canvas" :width="450" :height="337"></canvas>
      </div>
       <button v-if="!isPhotoTaken && isCameraOpen" class="button-snap" @click="takePhoto">
        <span>Snap!</span>
      </button>
      <button v-show="isPhotoTaken && isCameraOpen" class="camera-download">
        <a id="downloadPhoto" download="VueRocksPhoto.jpg" class="button" role="button" @click="downloadImage">
          Download
        </a>
      </button>
      <select v-model="selected">
    <option v-for="item in devices" :key="item.DeviceName" :value="item.DeviceId">
      {{ item.DeviceName }}
    </option>
  </select>
    </div>
    {{ selected }}
  </div> -->
  <div>
    <!-- <button class="button-snap" @click="toggleShow()"> -->
    <button class="button-snap" v-on:click="isCameraOpen ^= true">
        <span v-if="!isCameraOpen">映像表示</span>
        <span v-else>映像停止</span>
      </button>
  <select v-model="selected" v-on:change="selectdevice">
  <option v-for="item in devices" :key="item.DeviceName" :value="item.DeviceId">
      {{ item.DeviceName }}
    </option>
  </select>
  <video v-show="isCameraOpen" class="camera-video" ref="camera" :width="450" :height="337" autoplay playsinline ></video>
  {{ selected }}
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
      selected:''
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
          deviceId:this.selected
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
    },
    takePhoto () {
      this.isPhotoTaken = !this.isPhotoTaken

      const context = this.$refs.canvas.getContext('2d')
      const photoFromVideo = this.$refs.camera

      context.drawImage(photoFromVideo, 0, 0, 450, 337)
    },
    downloadImage() {
    const download = document.getElementById("downloadPhoto");
    const canvas = document.getElementById("photoTaken").toDataURL("image/jpeg")
      .replace("image/jpeg", "image/octet-stream");
    download.setAttribute("href", canvas);
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

      const constraints = {
        audio: false,
        video: {
          deviceId:this.selected
        }
      }
      navigator.mediaDevices
        .getUserMedia(constraints)
        .then(stream => {
          this.$refs.camera.srcObject = stream
        })
        .catch(error => {
          alert(error, "May the browser didn't support or there is some errors.")
        })
    
  },  
}
</script>