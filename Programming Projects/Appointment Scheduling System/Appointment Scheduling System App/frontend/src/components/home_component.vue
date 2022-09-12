<template>
    <div id="homeComponentBody" style="min-height: 95vh;">
      
        <video playsinline muted playbackRate="0.80" style="width: 100%; height: 95vh; min-width: 1500px; position:absolute;">
          <source src="../assets/video2.mp4" type="video/mp4">
        </video>
        
  </div>
</template>

<script>
import video1 from '../assets/video.mp4'
import video2 from '../assets/video2.mp4'
import video3 from '../assets/video3.mp4'
export default {
    name: 'home_component',
    data() {
      return {
        video: 0,
        source: '../assets/video.mp4'
      }
    },
    methods: {
      switchVideo() {
        if (this.video == 0) {
          this.video = 1
          return
        }
        if (this.video == 1) {
          this.video = 2
          return
        }
        if (this.video == 2) {
          this.video = 0
        }
      }
    },
    mounted() {
      const video = document.querySelector('video');
      video.play()
      video.addEventListener('ended', () => {
        this.switchVideo()
        if (this.video == 1) {
          video.src = video1
          video.play()
          return
        }
        if (this.video == 0) {
          video.src = video2
          video.play()
          return
        }
        if (this.video == 2) {
          video.src = video3
          video.play()
        }
      });

    }
}
</script>

<style scoped>

#banner {
  background: #f0f0f0;
  position: absolute;
  top: 38%;
  left: 50%;
  transform: translate(-50%, -50%);
}
video {
  object-fit: cover;
  position: absolute;
  top: 1;
  left: 50%;
  height: 100%;
  width: 100%;
  transform: translate(-50%)
}

#textArea {
  margin-top: 1%;
  margin-bottom: 12%;
  width: 75%;
  min-width: 290px;
  max-width: 700px;
}

#logo {
  margin-top: 3%;
  max-width: 550px;
  min-width: 295px;
  width: 95%;
}

#dentist {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  max-width: 350px;
  min-width: 215px;
  border-radius: 50%;
  box-shadow: 0 1px 5px rgb(0 0 0 / 0.4);
}


p {
  font-size: min(5.5vw, 15px);
}
</style>