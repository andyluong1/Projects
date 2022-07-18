<!-- This is the program create code, this wil display when a client is created to allow the user to attach that client to a program -->
<!-- User will have to fill out this form and the activity -->
<template>
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h3 class="text-center">Create Program</h3>
            <form @submit.prevent="handleSubmitForm">
                <div id="v-model-select" class="form-group">
                    <label>Program</label>
                    <select v-model="program.activity">
                        <option disabled value="">Please select one</option>
                        <option>Adult Education</option>
                        <option>Family Support Services</option>
                        <option>Early Childhood</option>
                        <option>Youth Services</option>
                    </select>
                    <span>{{ program.activity }}</span>
                </div>
                <div class="form-group">
                    <label>Start Date</label>
                    <input type="date" class="form-control" v-model="program.startDate" required>
                </div>
                <div class="form-group">
                    <label>End Date</label>
                    <input type="date" class="form-control" v-model="program.closeDate" required>
                </div>
                <div class="form-group">
                    <label>Services Used</label>
                    <input type="text" class="form-control" v-model="program.servicesUsed" required>
                </div>
                <div class="form-group">
                    <label>Client Number</label>
                    <input type="number" class="form-control" v-model="program.clientNo" required>
                </div>

                <button class="btn btn-danger mt-3">Create</button>
            </form>
        </div>



       
    </div>

    
</template>



<script>
    import axios from "axios";

    export default {
        name: 'program',
        data() {
            return {
                program: {
                   activity: '',
                   startDate: '',
                   closeDate: '',
                   servicesUsed: ''
                },
                
            }
        },
        methods:{
        handleSubmitForm(){
            axios.post('http://localhost:3000/program', this.program) 
                 .then(() => {
    alert('Form was submitted successfully')
  })         
        }
    }
           
    }
</script>
