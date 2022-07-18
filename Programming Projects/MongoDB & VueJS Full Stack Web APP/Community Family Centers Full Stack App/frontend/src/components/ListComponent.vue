<!--Used to VIEW the list of client already in the database, user will see a small preview as to what information is stored on the client. 
In order to view everything, the user will have to select edit-->
<template>
    <div class="row">
        <div class="col-md-12">
            <table class="table table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>ClientNo</th>
                        <th>FamilyNo</th>
                        <th>StartDate</th>
                        <th>CloseDate</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="client in Clients" :key="client._id">
                        <td>{{ client.firstName }}</td>
                        <td>{{ client.lastName }}</td>
                        <td>{{ client.clientNo }}</td> 
                        <td>{{ client.familyNo }}</td> 
                        <td>{{ client.startDate }}</td> 
                        <td>{{ client.closeDate }}</td> 

                        <td>
                            <router-link :to="{name: 'editClient', params: { id: client._id }}" class="btn btn-success ">Edit
                            </router-link>
                            <router-link :to="{name: 'addProgram', params: { id: client.clientNo }}" class="btn btn-info"> Add a Program
                            </router-link>
                            <button @click.prevent="deleteClient(client._id)" class="btn btn-danger mx-2">Delete</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    export default {
        data() {
            return {
                Clients: []
            }
        },
        created() {
            let apiURL = 'http://localhost:3000/client';
            axios.get(apiURL).then(res => {
                this.Clients = res.data;
            }).catch(error => {
                console.log(error)
            });
        },
        methods: {
            deleteClient(id){
                console.log(id)
                let apiURL = `http://localhost:3000/client/${id}`;
                let indexOfArrayItem = this.Clients.findIndex(i => i._id === id);
                if (window.confirm("Do you really want to delete this client?")) {
                    axios.delete(apiURL).then(() => {
                        this.Clients.splice(indexOfArrayItem, 1);
                    }).catch(error => {
                        console.log(error)
                    });
                }
            }
        }
    }
</script>



<style>
    .btn-success {
        margin-right: 10px;
    }
</style>