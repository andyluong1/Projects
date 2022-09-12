<template>
    <div id="employeesComponentBody" style="min-width: 1400px;">
        <div class="bg-dark text-white" style="height: 60px; width: 100%; margin-top: 35px; border-radius: 10px; box-shadow: 0 3px 5px rgb(0 0 0 / 0.4);">
            <p class="mx-3" style="padding-top: 12px; font-weight: bold; font-size: 25px;">Analytics</p>
        </div>
        <div style="box-shadow: 0 2px 5px rgb(0 0 0 / 0.4); min-width: 1350px; margin-right: 20px; margin-left: 20px; height: 965px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;" >
            <div class="row mx-auto" style="min-width: 1400px; margin-top: 0px;">
                <table class="table-borderless" style="margin-top: 35px;">
                    <tbody>
                        <tr>
                            <td align="center"><DoughnutChart style="width: 17.5vw; min-width: 365px;"/></td>
                            <div style="border-style: solid; height: 450px; width: 5px; border-radius: 10px; margin-top: 20px; border-color: #292b2c;"></div>
                            <td align="center"><BarChart style="width: 17.5vw; min-width: 365px;"/></td>
                            <div style="border-style: solid; height: 450px; width: 5px; border-radius: 10px; margin-top: 20px; border-color: #292b2c"></div>
                            <td align="center"><PieChart style="width: 17.5vw; min-width: 365px;"/></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="row mt-4 mx-auto justify-content-center">
                <div style="min-width: 1367px; width: 91.3%;"> 
                    <input v-model="this.filter" type="text" id="searchBar" style="display: inline-block; width: 60%; border-radius: 0px; margin-right: 1.3%;" class="form-control" placeholder="Search appointment records...">
                    <input v-model="this.start" :max="this.max" type="date" id="searchBar" style="display: inline-block; width: 12%; border-radius: 0px; margin-right: 1.3%;" class="form-control" placeholder="From: ">
                    <input v-model="this.end" :max="this.max" type="date" id="searchBar" style="display: inline-block; width: 12%; border-radius: 0px; margin-right: 1.3%;" class="form-control" placeholder="To: ">
                    <div @click="searchAppointments()" align="center" class="form-control" id="magnifier" style="display: inline-block; width: 12%; border-radius: 0px;">
                        <i class="fa-solid fa-magnifying-glass fa-xl"></i>
                    </div>
                </div>
            </div>
            <div class="row mx-auto mt-3" style="min-width: 1340px; width: 90%;">
                <div class="overflow-auto p-0" style="max-height: 331px;">
                    <table class="table table-light table-striped table-hover" style="">
                        <thead class="thead-dark bg-light sticky-top" style="box-shadow: 0 1px 4px rgb(0 0 0 / 0.4); z-index: 1;">
                            <tr>
                                <th @click="sort()">Date</th>
                                <th>Time</th>
                                <th>Service</th>
                                <th>Zip</th>
                                <th>Phone</th>
                                <th>Email</th>
                                <th>First Name</th>
                                <th>Last Name</th>
                            </tr>
                        </thead>
                        <tbody v-if="this.filter == ''">
                            <tr v-for="appointment in this.appointments" :key="appointment._id">
                                <td>{{appointment.appt_formatted_date}}</td>
                                <td>{{appointment.appt_formatted_time}}</td>
                                <td>{{appointment.service}}</td>
                                <td>{{appointment.patient_zip}}</td>
                                <td>{{appointment.patient_phone}}</td>
                                <td>{{appointment.patient_email}}</td>
                                <td>{{appointment.patient_first_name}}</td>
                                <td>{{appointment.patient_last_name}}</td>
                            </tr>
                        </tbody>
                        <tbody v-if="this.filter != ''">
                            <tr v-for="appointment in this.appointments" :key="appointment._id">
                                <td v-if="appointment['service'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_first_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_last_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_email'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_phone'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_zip'].toLowerCase().includes(this.filter.toLowerCase())">{{appointment.appt_formatted_date}}</td>
                                <td v-if="appointment['service'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_first_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_last_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_email'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_phone'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_zip'].toLowerCase().includes(this.filter.toLowerCase())">{{appointment.appt_formatted_time}}</td>
                                <td v-if="appointment['service'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_first_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_last_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_email'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_phone'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_zip'].toLowerCase().includes(this.filter.toLowerCase())">{{appointment.service}}</td>
                                <td v-if="appointment['service'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_first_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_last_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_email'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_phone'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_zip'].toLowerCase().includes(this.filter.toLowerCase())">{{appointment.patient_zip}}</td>
                                <td v-if="appointment['service'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_first_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_last_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_email'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_phone'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_zip'].toLowerCase().includes(this.filter.toLowerCase())">{{appointment.patient_phone}}</td>
                                <td v-if="appointment['service'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_first_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_last_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_email'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_phone'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_zip'].toLowerCase().includes(this.filter.toLowerCase())">{{appointment.patient_email}}</td>
                                <td v-if="appointment['service'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_first_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_last_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_email'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_phone'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_zip'].toLowerCase().includes(this.filter.toLowerCase())">{{appointment.patient_first_name}}</td>
                                <td v-if="appointment['service'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_first_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_last_name'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_email'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_phone'].toLowerCase().includes(this.filter.toLowerCase()) || appointment['patient_zip'].toLowerCase().includes(this.filter.toLowerCase())">{{appointment.patient_last_name}}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import PieChart from './PieChart.vue'
import BarChart from './BarChart.vue'
import DoughnutChart from './DougnutChart.vue'
var localizedFormat = require('dayjs/plugin/localizedFormat')
var customParseFormat = require('dayjs/plugin/customParseFormat')
import axios from 'axios'
import dayjs from "dayjs"
import advancedFormat from 'dayjs/plugin/advancedFormat'
dayjs.extend(advancedFormat)
dayjs.extend(localizedFormat)
dayjs.extend(customParseFormat)
export default {
    name: 'analytics_component',
    components: {
        BarChart, 
        DoughnutChart, 
        PieChart
    }, 
    data() {
        return {
            start: null,
            end: null,
            appointments: null,
            max: null,
            sorted: 'inc',
            filter: ''
        }
    },
    methods: {
        sort() {
            if (this.sorted == 'inc') {
                this.appointments.sort((a, b) => (dayjs(dayjs(a.appt_date).format('YYYY-MM-DD') + a.appt_time).isBefore(dayjs(dayjs(b.appt_date).format('YYYY-MM-DD') + b.appt_time))) ? 1: - 1)
                this.sorted = 'dec'
                return
            }
            if (this.sorted == 'dec') {
                this.appointments.sort((a, b) => (dayjs(dayjs(a.appt_date).format('YYYY-MM-DD') + a.appt_time).isAfter(dayjs(dayjs(b.appt_date).format('YYYY-MM-DD') + b.appt_time))) ? 1: - 1)
                this.sorted = 'inc'
                return
            }
        },
        searchAppointments() {
            if (dayjs(this.start).isBefore(dayjs(this.end)) && dayjs(this.start).isBefore(dayjs()) && dayjs(this.end).isBefore(dayjs())) {
                let start = dayjs(this.start).format('YYYY-MM-DD')
                let end = dayjs(this.end).format('YYYY-MM-DD')
                let apiURL = `http://localhost:3000/dashboard/analytics/appointmentHistory/${start}/${end}`
                axios.get(apiURL).then(res => {
                    this.appointments = res.data
                    for (let i = 0; i < this.appointments.length; i++) {
                        this.appointments.sort((a, b) => (dayjs(dayjs(a.appt_date).format('YYYY-MM-DD') + a.appt_time).isAfter(dayjs(dayjs(b.appt_date).format('YYYY-MM-DD') + b.appt_time))) ? 1: - 1)
                    }
                    for (let i = 0; i < this.appointments.length; i++) {
                        this.appointments[i].patient_first_name = (this.appointments[i].patient_first_name).slice(0, 1).toUpperCase() + (this.appointments[i].patient_first_name).slice(1).toLowerCase()
                        this.appointments[i].appt_formatted_date = dayjs(this.appointments[i].appt_date).format('MMMM Do, YYYY')
                        this.appointments[i].appt_formatted_time = dayjs('1/1/1 ' + this.appointments[i].appt_time).format('h:mm a')
                    }
                })
            }
            else {
                alert('Please ensure the "From" date is before the "To" date')
            }
        }
    },
    created() {
        this.max = dayjs().add(-1, 'day').format('YYYY-MM-DD')
        let start = dayjs().add(-32, 'day').format('YYYY-MM-DD')
        let end = dayjs().add(-1, 'day').format('YYYY-MM-DD')
        let apiURL = `http://localhost:3000/dashboard/analytics/appointmentHistory/${start}/${end}`
        axios.get(apiURL).then(res => {
            this.appointments = res.data
            for (let i = 0; i < this.appointments.length; i++) {
                this.appointments.sort((a, b) => (dayjs(dayjs(a.appt_date).format('YYYY-MM-DD') + a.appt_time).isAfter(dayjs(dayjs(b.appt_date).format('YYYY-MM-DD') + b.appt_time))) ? 1: - 1)
            }
            for (let i = 0; i < this.appointments.length; i++) {
                this.appointments[i].patient_first_name = (this.appointments[i].patient_first_name).slice(0, 1).toUpperCase() + (this.appointments[i].patient_first_name).slice(1).toLowerCase()
                this.appointments[i].patient_last_name = (this.appointments[i].patient_last_name).slice(0, 1).toUpperCase() + (this.appointments[i].patient_last_name).slice(1).toLowerCase()
                this.appointments[i].appt_formatted_date = dayjs(this.appointments[i].appt_date).format('MMMM Do, YYYY')
                this.appointments[i].appt_formatted_time = dayjs('1/1/1 ' + this.appointments[i].appt_time).format('h:mm a')
            }
        })  
    }
}
</script>

<style scoped>
#searchBar:focus::-webkit-input-placeholder 
{
    color: transparent;
}

#searchBar:focus {
    border-color:#292b2c;
    outline: 0px;
    box-shadow: none;
}

input[type="date"]:before {
    content: attr(placeholder) !important;
    color: #292b2c;
    margin-right: 0.5em;
}

#magnifier:hover {
    background: linear-gradient(141deg, rgba(32,185,233,1) 0%, rgba(129,159,242,1) 51%, rgba(0,198,255,1) 100%);
    border-color: #292b2c;
}

::-webkit-scrollbar {
    width: 15px;
}

::-webkit-scrollbar-thumb {
background:#292b2c;
border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
background:rgb(54, 56, 58); 
}
</style>
