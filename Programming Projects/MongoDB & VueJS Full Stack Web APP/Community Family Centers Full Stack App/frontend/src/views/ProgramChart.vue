<template>
  <section class="container">
    <h1>Activity Graph</h1>

    <div class="columns">
      <div class="column">
 
      </div>
    <div class="column">

        <h3>Count of Programs used by clients</h3>
        <div>
          <div>
            <!--placeholder for components in ProgramBar -->
            <ProgramBar
              v-if="!loading && !error"
              :label="labels"
              :chart-data="total"
            ></ProgramBar>

            <!-- Start of loading animation -->
            <div class="mt-40" v-if="loading">
              <p
                class="
                  text-6xl
                  font-bold
                  text-center text-gray-500
                  animate-pulse
                "
              >
                Loading...
              </p>
            </div>
            <!-- End of loading animation -->

            <!-- Start of error alert -->
            <div class="mt-12 bg-red-50" v-if="error">
              <h3 class="px-4 py-1 text-4xl font-bold text-white bg-red-800">
                {{ error.title }}
              </h3>
              <p class="p-4 text-lg font-bold text-red-900">
                {{ error.message }}
              </p>
            </div>
            <!-- End of error alert -->
            <br />
            <br />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
//using axios library to make promises
const axios = require("axios");
//retreives components from chart.js library through corresponding labels from AnalysisComponent.vue
import ProgramBar from "@/components/AnalysisComponent.vue";

export default {
  name: "ProgramChart",
  components: {
    ProgramBar
  },
  data() {
    //holds the data in a array
    return {
      labels: [],  
      total: [], 
      count: [], 
      loading: false,
      error: null,
    };
  },
  methods: {
    async fetchData() {
      try {
        this.error = null;
        this.loading = true;
        //the next line of code is the url to retrieve the backend data. Retrieves data from that API.
        const url = `http://localhost:3000/program`;
        const response = await axios.get(url);
        //"re-organizing" - mapping json from the response
        let count = response.data.map((item) => item.activity)
        let q1 = 0
        let q2 = 0
        let q3 = 0
        let q4 = 0
         for (let i = 0; i < response.data.length; i++) { 
          if (count[i] === 'Adult Education') {
          q1 += 1;
         }
         if (count[i] === 'Family Support Services') {
          q2 += 1;
         }
         if (count[i] === 'Early Childhood') {
          q3 += 1;
         }
         if (count[i] === 'Youth Services') {
          q4 += 1;
         }
      }
       
        
            this.labels = [  "Adult Education", "Family Support Services", "Early Childhood", "Youth Services"]
            this.total = [q1, q2, q3, q4]
      } catch (err) {
        if (err.response) {
          // client received an error response (5xx, 4xx)
          this.error = {
            title: "Server Response",
            message: err.message,
          };
        } else if (err.request) {
          // client never received a response, or request never left
          this.error = {
            title: "Unable to Reach Server",
            message: err.message,
          };
        } else {
          // There's probably an error in your code
          this.error = {
            title: "Application Error",
            message: err.message,
          };
        }
      }
      this.loading = false;
    },
  },
  mounted() {
    this.fetchData();
  },
};
</script>
