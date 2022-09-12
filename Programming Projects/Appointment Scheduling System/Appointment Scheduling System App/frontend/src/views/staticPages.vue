<template>
    <div id="pageBody">
        <nav class="navbar sticky-top navbar-expand-xxl navbar-dark bg-dark" style="box-shadow: 0 3px 10px rgb(0 0 0 / 0.5);">
            <div class="container-fluid">
                <a style="font-size: 17px; margin-left: 3.7%;" class="navbar-brand" id="navbar-brand" @click="componentSwap('home')" href="#" >Smile Architects of Houston</a>
                <div class="" id="bookAppointment">
                    <div id="appointmentLeft" style="float: left; font-size: 15px;">
                        <button class="text-white" @click="componentSwap('bookAppointment')" style="border: none; border-radius: 5px; background-color: transparent">
                            <span id="appointmentText"> Book Appointment <i id="appointmentText" class="navbar-brand fa-regular fa-calendar-check " style="margin-left: 10px; padding-top: 8px; padding-bottom: 8px;"></i></span>
                        </button>
                    </div>
                    <div id="appointmentRight" style="float: right;">
                        <button class="navbar-toggler" id="navBarToggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <i id="togglerIcon" class="fas fa-bars fa-lg"></i>
                        </button>
                    </div>
                </div>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0" style="margin-right: 4%; margin-left: 3%">
                        <li class="nav-item ms-auto">
                            <a class="nav-link" @click="componentSwap('home')" id="link1" href="#">Home</a>
                        </li>
                        <li class="nav-item ms-auto">
                            <a class="nav-link" @click="componentSwap('meetOurOffice')" id="link2" href="#">Meet our office</a>
                        </li>
                        <li class="nav-item ms-auto">
                            <a class="nav-link" @click="componentSwap('dentalServices')" id="link3" href="#">Dental services</a>
                        </li>
                        <li class="nav-item ms-auto">
                            <a class="nav-link" @click="componentSwap('patientResources')" id="link4" href="#">Patient resources</a>
                        </li>
                        <li class="nav-item ms-auto">
                            <a class="nav-link" @click="componentSwap('contactUs')" id="link5" href="#">Contact us</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <component :is="component" />

        <div class="footer">
            <footer id="footer" class="bg-dark text-center text-white">
                <div class="container p-3">
                    <a class="btn" href="https://www.facebook.com/Smilearchitectsofhouston/" role="button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-facebook" viewBox="0 0 16 16">
                            <path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"/>
                        </svg>
                    </a>
                    <a class="btn" href="https://www.yelp.com/biz/smile-architects-houston" role="button">
                        <i class="fab fa-yelp fa-xl"></i>
                    </a>
                    <a class="btn" href="http://localhost:8080/login" role="button">
                        <i class="fa-solid fa-chart-line fa-xl"></i>
                    </a>
                    <div>
                        <div class="mt-2">11322 Bellaire Blvd #112 Houston, TX 77072  |  smilearchitects1100@yahoo.com | (281)-498-1100 </div> 
                        <div class="mt-3 mb-3 fw-bold">Business Hours: </div>
                        <div>Monday: 10:00 AM - 6:00 PM</div> 
                        <div>Tuesday: 10:00 AM - 6:00 PM</div> 
                        <div>Wednesday: closed</div> 
                        <div>Thursday: 10:00 AM - 6:00 PM</div>  
                        <div>Friday: 10:00 AM - 6:00 PM</div>
                        <div>Saturday: 9:00 AM - 3:00 PM</div>
                    </div>
                </div>
            </footer>
        </div>
    </div>
</template>

<script>
import home_component from '../components/home_component.vue'
import meet_our_office_component from '../components/meet_our_office_component.vue'
import services_component from '../components/services_component.vue'
import patient_resources_component from '../components/patient_resources_component.vue'
import contact_us_component from '../components/contact_us_component.vue'
import book_appointments_component from '../components/book_appointments.vue'
export default {
    components: {
        home_component, 
        meet_our_office_component, 
        services_component, 
        patient_resources_component,
        contact_us_component, 
        book_appointments_component
    },
    data() {
        return {
            component: 'home_component'
        }
    },
    methods: {
        componentSwap(selector) {
            if (selector == 'home') {
                this.component = 'home_component'
            }
            if (selector == 'meetOurOffice') {
                this.component = 'meet_our_office_component'
            }
            if (selector == 'dentalServices') {
                this.component = 'services_component'
            }
            if (selector == 'patientResources') {
                this.component = 'patient_resources_component'
            }
            if (selector == 'contactUs') {
                this.component = 'contact_us_component'
            }
            if (selector == 'bookAppointment') {
                this.component = 'book_appointments_component'
            }
        }
    } 
}
</script>

<style scoped>
#bookAppointment {
    border-radius: 5px;
    padding-left: 10px;
    background: rgb(57,130,224);
    background: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    margin-right:4%;
    margin-left:2%;
}
#bookAppointment:hover {
}
#appointmentLeft:hover #appointmentText {
    opacity: 40%;
    transition: 0.3s;
}
#appointmentRight:hover #togglerIcon {
    opacity: 40%;
    transition: 0.3s;
}
#navBarToggler {
    border-color: #232324;
    font-size: 17px; 
    border-radius: 0px; 
    border-right: none; 
    border-top: none; 
    border-bottom: none; 
    margin-top: 17%;
}
.navbar-toggler:focus {
    box-shadow: none !important;
}

#link1 {
    color: white;
}
#link1:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.3s;
}
#link2 {
    color: white;
}
#link2:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.3s;
}
#link3 {
    color: white;
}
#link3:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.3s;
}
#link4 {
    color: white;
}
#link4:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.3s;
}
#link5 {
    color: white;
}
#link5:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.3s;
}
#link6 {
    color: white;
}
#link6:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.3s;
}
.btn {
    color: white;
}
.btn:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.3s;
}
#navbar-brand {
    margin-left:3%;
}
#navbar-brand:hover {
    color: rgb(57,130,224);
    color: linear-gradient(0deg, rgba(57,130,224,1) 0%, rgba(0,129,255,1) 32%, rgba(65,96,233,1) 62%);
    transition: 0.3s;
}
</style>