<template>
  <div class="row justify-content-center">
    <div class="col-md-6">
      <!-- Update Client content -->
      <h3 class="text-center">Update Program</h3>
      <form @submit.prevent="handleUpdateForm">
        <div class="form-group">
          <label>Program</label>
          <div id="v-model-select" class="form-group">>
            <select v-model="program.activity">
              <option disabled value="">Please select one</option>
              <option>Adult Education</option>
              <option>Family Support Services</option>
              <option>Early Childhood</option>
              <option>Youth Services</option>
            </select>
            <span>{{ program.activity }}</span>
          </div>
        </div>

        <div class="form-group">
          <label>Client No</label>
          <input
            type="number"
            class="form-control"
            v-model="program.clientNo"
            required
          />
        </div>

        <div class="form-group">
          <label>Start Date</label>
          <input
            type="date"
            class="form-control"
            v-model="program.startDate"
            required
          />
        </div>

        <div class="form-group">
          <label>End Date</label>
          <input
            type="date"
            class="form-control"
            v-model="program.closeDate"
            required
          />
        </div>

        <div class="form-group">
          <label>Services Used</label>
          <input
            type="text"
            class="form-control"
            v-model="program.servicesUsed"
            required
          />
        </div>


        <button class="btn btn-danger mt-3">Update</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      program: {},
    };
  },
  created() {
    let apiURL = `http://localhost:3000/program/${this.$route.params.id}`;

    axios.get(apiURL).then((res) => {
      this.program = res.data;
    });

  },
  methods: {
    handleUpdateForm() {
      let apiURL = `http://localhost:3000/program/${this.$route.params.id}`;

      axios
        .put(apiURL, this.program)
        .then((res) => {
          console.log(res);
          this.$router.push("/program/:id");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>