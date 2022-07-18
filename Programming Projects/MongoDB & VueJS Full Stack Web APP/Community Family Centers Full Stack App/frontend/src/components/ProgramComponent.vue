<!-- This displays the program-->
<template>
    <div class="row">
        <div class="col-md-12">
                <h2>Activties</h2>
                <table class="table table-striped">
                    <thead class="thead-dark">
                        <tr>
                            <th>Activity</th>
                            <th>ClientNo</th>
                            <th>Start Date</th>
                            <th>End Date</th>
                            <th>Services Used</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="program in Programs" :key="program._id">
                            <td>{{ program.activity }}</td>
                            <td>{{ program.clientNo }}</td>
                            <td>{{ program.startDate }}</td>
                            <td>{{ program.closeDate }}</td>
                            <td>{{ program.servicesUsed }}</td>
                            <td>
                                <router-link :to="{name: 'editProgram', params: { id: program._id }}" class="btn btn-success">Edit
                                </router-link>
                            <button @click.prevent="deleteProgram(program._id)" class="btn btn-danger">Delete</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
    import axios from "axios";

    export default {
        data() {
            return {
                Programs: [],
                Clients: [],
                client: {
                   firstName: '',
                   lastName: '',
                  },
                program: {
                   activity: '',
                   clientNo: this.$route.params.id,
                   startDate: '',
                   endDate: '',
                   servicesUsed: '',
                  }
            }
        },
        // this is using created hook 
        created() {
            let apiURL = `http://localhost:3000/program`;
            axios.get(apiURL).then(res => {
                this.Programs = res.data;
            }).catch(error => {
                console.log(error)
            });

            let apiURL1 = `http://localhost:3000/client`;
            axios.get(apiURL1).then(res => {
                this.Clients = res.data;
            }).catch(error => {
                console.log(error)
            });
        },
        methods: {
            deleteProgram(id){
                let apiURL = `http://localhost:3000/program/${id}`;
                let indexOfArrayItem = this.Programs.findIndex(i => i._id === id);

                if (window.confirm("Do you really want to delete?")) {
                    axios.delete(apiURL).then(() => {
                        this.Programs.splice(indexOfArrayItem, 1);
                    }).catch(error => {
                        console.log(error)
                    });
                }
            },           
        }
    }
</script>



<style>
    .btn-success {
        margin-right: 10px;
    }
</style>
