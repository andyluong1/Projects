<template>
    <div style="height: 100vh; width: 100vw;">
        <div class="container-fluid">
            <div class="row flex-nowrap">
                <div class="col-auto bg-dark p-0">
                    <div class="bg-dark" style="width: 116px;"> </div>
                    <div class="bg-dark px-3 pt-2 min-vh-100" style="position:fixed; box-shadow: 0 3px 7px rgb(0 0 0 / 0.6); z-index: 2;">
                        <ul class="nav flex-column mt-4">
                            <li class="mb-4" id="navHead">
                                <div :data-initials="initials" id="profileIcon">
                                    <div id="tooltip1">
                                        <div><span class="fw-bold">Username: </span>{{this.profile}}</div>
                                        <div><span class="fw-bold">Employee: </span>{{this.employeeName}}</div>
                                        <div><span class="fw-bold">Permissions: </span>{{this.permissions}}</div>
                                    </div> 
                                </div>
                            </li>
                            <li class="mb-5 text-white px-4 mt-4">
                                <i @click="swapEmployeeProfiles()" id="sideNavButton1" class="fa-solid fa-user-group fa-xl">
                                    <div id="tooltip1">Employee Profiles</div> 
                                </i>
                            </li>
                            <li class="mb-5 text-white px-4">
                                <i @click="swapScheduleBuilder()" id="sideNavButton2" class="fa-solid fa-calendar-days fa-2xl">
                                    <div id="tooltip2">Scheduling Services</div> 
                                </i> 
                            </li>
                            <li class="mb-5 text-white px-4">
                                <i @click="swapAnalytics()" id="sideNavButton3" class="fa-solid fa-file-lines fa-2xl">
                                    <div id="tooltip3">Analytics</div> 
                                </i>
                            </li>
                            <li class="mb-5 text-white px-4" style="margin-top:650%;">
                                    <i v-on:click="logout()" id="sideNavButton6" class="fa-solid fa-arrow-right-from-bracket fa-2xl">
                                        <div id="tooltip6">Logout</div>
                                    </i>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="col min-vh-100 mx-4">
                    <component :is="component" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import analytics_component from '../components/analytics_component.vue'
import employees_component from '../components/employees_component.vue'
import schedule_component from '../components/schedule_component.vue'

    export default {
        components: {
            analytics_component,
            employees_component,
            schedule_component
        },
        data() {
            return {
                component: 'schedule_component',
                initials: window.sessionStorage.getItem('initials'),
                employeeName: window.sessionStorage.getItem('name'),
                profile: window.sessionStorage.getItem('profile'),
                permissions: null
            }
        },
        methods: {
            logout() {
                window.sessionStorage.setItem('authenticated', 'false')
                window.sessionStorage.setItem('adminPrivileges', 'false')
                window.sessionStorage.removeItem('privilege')
                this.$router.replace({ name: 'login'})
            },
            swapEmployeeProfiles() {
                this.component = 'employees_component'
            },
            swapScheduleBuilder() {
                this.component = 'schedule_component'
            },
            swapAnalytics() {
                this.component = 'analytics_component'
            }
        },
        created() {
            if (window.sessionStorage.getItem('adminPrivileges') == 'true') {
                this.permissions = 'Administrator'
            }
            if (window.sessionStorage.getItem('adminPrivileges') == 'false') {
                if (window.sessionStorage.getItem('privilege') == 'read') {
                    this.permissions = 'Read only'
                }
                if (window.sessionStorage.getItem('privilege') == 'write') {
                    this.permissions = 'Read and write'
                }
            }
        } 
    }
</script>

<style scoped>
#profileIcon:hover #tooltip1 {
    visibility: visible;
    margin-left: 6.5em;
}

#tooltip1 {
    color: black;
    background-color: white;
    padding: 15px;
    visibility: hidden;
    border-radius: 8px;
    position: fixed;
    font-family: Helvetica;
    font-weight: normal;
    font-size: .8em;
    margin-left: 3em;
    margin-bottom:5em;
    box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);
}

#sideNavButton1:hover #tooltip1 {
    visibility: visible;
}


#tooltip2 {
    color: black;
    background-color: white;
    padding: 15px;
    visibility: hidden;
    border-radius: 8px;
    position: fixed;
    font-family: Helvetica;
    font-weight: normal;
    font-size: .59em;
    margin-left: 3em;
    margin-bottom:5em;
    box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);
}

#sideNavButton2:hover #tooltip2 {
    visibility: visible;
}


#tooltip3 {
    color: black;
    background-color: white;
    padding: 15px;
    visibility: hidden;
    border-radius: 8px;
    position: fixed;
    font-family: Helvetica;
    font-weight: normal;
    font-size: .59em;
    margin-left: 3em;
    margin-bottom:5em;
    box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);
}

#sideNavButton3:hover #tooltip3 {
    visibility: visible;
}

#tooltip4 {
    color: black;
    background-color: white;
    padding: 15px;
    visibility: hidden;
    border-radius: 8px;
    position: fixed;
    font-family: Helvetica;
    font-weight: normal;
    font-size: .59em;
    margin-left: 3em;
    margin-bottom:5em;
    box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);
}

#sideNavButton4:hover #tooltip4 {
    visibility: visible;
}

#tooltip5 {
    color: black;
    background-color: white;
    padding: 15px;
    visibility: hidden;
    border-radius: 8px;
    position: fixed;
    font-family: Helvetica;
    font-weight: normal;
    font-size: .59em;
    margin-left: 3em;
    margin-bottom:5em;
    box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);
}

#sideNavButton5:hover #tooltip5 {
    visibility: visible;
}

#tooltip6 {
    color: black;
    background-color: white;
    padding: 15px;
    visibility: hidden;
    border-radius: 8px;
    position: fixed;
    font-family: Helvetica;
    font-weight: normal;
    font-size: .59em;
    margin-left: 3em;
    margin-bottom:5em;
    box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);
}

#sideNavButton6:hover #tooltip6 {
    visibility: visible;
}

#sideNavButton1:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.1s;
}

#sideNavButton2:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.1s;
}

#sideNavButton3:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.1s;
}

#sideNavButton4:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.1s;
}

#sideNavButton5:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.1s;
}

#sideNavButton6:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.1s;
}

#loginBackground {
    background-image: url("../assets/login_background.png");
    background-repeat: no-repeat;
    background-size: cover;
}

#navHead {
    border-bottom-style: solid;
    border-color: white;
    padding-bottom: 30px;
}

i:hover {
    color: rgba(202, 202, 202, 0.795);
}

[data-title]:hover:after {
    opacity: 1;
    transition: all .7s ease 0.1s;
    visibility: visible;
}
[data-title]:after {
    content: attr(data-title);
    background-color: white;
    color: #111;
    font-size: 125%;
    position: absolute;
    padding: 1px 5px 2px 5px;
    bottom: 1.6em;
    left: 100%;
    white-space: nowrap;
    box-shadow: 1px 1px 3px #222222;
    opacity: 0;
    border-radius: 5px;
    visibility: hidden;
}
[data-title] {
    position: relative;
}

[data-initials]:before {
background: rgb(255,255,255); 
background: linear-gradient(0deg, rgba(12, 220, 235, 0.979) 0%, rgba(0,181,255,1) 48%, rgba(65,100,233,1) 100%);
color: white;
opacity: 1; 
content: attr(data-initials); 
display: inline-block; 
font-size: 25px;
font-weight: 450;
border-radius: 50%; 
vertical-align: middle; 
margin-right: 0.5em;
margin-left: 0.5em; 
width: 60px; 
height: 60px; 
line-height: 60px; 
text-align: center; 
}
</style>