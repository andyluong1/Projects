<!--route to App.vue for home page--> 
<template>
  <div class="app">
      <App title="Community Family Centers - CIS 4339: Group 20"/>
      <h1>Welcome to CIS 4339: Group 20 project</h1>
      <p>Created by Andy Luong, Isabella Robinson, and Jolene Ngo</p>
      <br><p>Select the About tab to learn how to use this application.</p>
  </div>
</template>

<script>
import app from '../App.vue'

export default {
  name: 'app',
  components: {
    app
  }
}
</script>
/