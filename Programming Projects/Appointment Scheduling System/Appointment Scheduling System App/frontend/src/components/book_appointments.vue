<template>
    <div id="bookAppointmentsComponentBody" style="min-height: 95vh;">
        <div class="row mx-auto mt-5 text-center" style="min-width: 66%; max-width: 90%;">
            <h1 class="fw-light mt-1" style="font-size: min(7vw, 35px);">BOOK AN APPOINTMENT</h1>
            <div v-if="this.currentStep == 1" class="mx-auto mt-4" style="margin-bottom: 80px; min-width: 250px; max-width: 1000px; box-shadow: 0 1px 5px rgb(0 0 0 / 0.4); border-radius: 10px;">
                <h5 style="font-size: min(5.5vw, 22px); margin-top: 75px;">First we need some personal details</h5>
                <div class="mb-5 mt-5 mx-auto" style="min-width: 200px; max-width:400px;">  
                    <form onsubmit="return false">
                        <div class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.firstName" style="font-size: min(4.5vw, 18px);" class="form-control" id="firstNameInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="firstNameInput">First name *</label>
                        </div>
                        <div class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.lastName" style="font-size: min(4.5vw, 18px);" class="form-control" id="firstNameInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="firstNameInput">Last name *</label>
                        </div>
                        <div class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.dob" @change="validateDate()" type="date" style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com">
                            <label style="font-size: min(4.5vw, 18px);" for="floatingInput">Date of birth *</label>
                        </div>
                        <div class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.email" style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">Email address *</label>
                        </div>
                        <div class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.phone" style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">Phone number *</label>
                        </div>
                        <div class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.zip" style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">5 digit zip code *</label>
                        </div>
                        <div class="form-floating mt-2 mb-4">
                            <button v-if="/^[A-Za-z]+$/.test(this.formDetails.firstName) == true && /^[A-Za-z]+$/.test(this.formDetails.lastName) == true && this.formDetails.validDOB == true && this.formDetails.dob.length == 10 && parseInt((this.formDetails.dob).slice(0, 5)) >= 1900 && /[^@\s]+@[^@\s]+\.com/.test(this.formDetails.email) == true && /^\d{3}-\d{3}-\d{4}$/.test(this.formDetails.phone) == true && /^\d{5}$/.test(this.formDetails.zip) == true" class="btn btn-primary" @click="incrementStep()" style="font-size: min(4.5vw, 18px);">Continue</button>
                            <button v-else class="btn btn-primary" @click="incrementStep()" style="font-size: min(4.5vw, 18px);" disabled>Continue</button>
                        </div>
                    </form>
                </div>
            </div>
            <div v-if="this.currentStep == 2" class="mx-auto mt-4" style="margin-bottom: 80px; min-width: 250px; max-width: 1000px; box-shadow: 0 1px 5px rgb(0 0 0 / 0.4); border-radius: 10px;">
                <i @click="decrementStep()" id="backArrow" class="fa-solid fa-circle-arrow-left fa-xl" style="float: left; margin-top: 30px; margin-left: 5px;"></i>
                <h5 style="font-size: min(5.5vw, 22px); margin-top: 75px;">Do you have insurance?</h5>
                <div class="mb-5 mt-5 mx-auto" style="min-width: 200px; max-width:400px;">
                    <form onsubmit="return false">
                        <div class="form-floating" style="margin-bottom: 35px;"> 
                        <input class="form-control" @change="selectInsurance()" list="insuranceOptions" id="dataList" placeholder="Type to search...">
                            <datalist id="insuranceOptions" >
                                <option>No insurance</option>
                                <option>Other</option>
                                <option>Aetna</option>
                                <option>Aflac</option>
                                <option>Allied</option>
                                <option>Always Care</option>
                                <option>AMERICAN NATIONAL (LIFE CARE )</option>
                                <option>Ameritas</option>
                                <option>Anthem Blue Cross</option>
                                <option>APWU Health Plan</option>
                                <option>Assurant Employee Benefits</option>
                                <option>Assurant Health</option>
                                <option>Assurant Supplemental Coverage</option>
                                <option>ASSURE CARE</option>
                                <option>Blue Cross Blue Shield</option>
                                <option>Benefit Management Administrators, Inc</option>
                                <option>Benefits Planners</option>
                                <option>BOON CHAPMAN</option>
                                <option>Careington</option>
                                <option>CENTRAL STATES</option>
                                <option>Cigna</option>
                                <option>CORE SOURCE</option>
                                <option>Crescent Employee Benefits</option>
                                <option>Dearborn National</option>
                                <option>Delta Dental</option>
                                <option>Dental Connection</option>
                                <option>Dentaquest</option>
                                <option>Entrust Inc</option>
                                <option>First Continental Life Insurance Company</option>
                                <option>Fortis</option>
                                <option>GEHA</option>
                                <option>Great-West Healthcare</option>
                                <option>GUARDIAN</option>
                                <option>Health Velocity</option>
                                <option>HealthSmart Benefit Solutions, Inc</option>
                                <option>Humana Dental</option>
                                <option>Interest</option>
                                <option>Jefferson Pilot</option>
                                <option>Lincoln National Life Insurance Company</option>
                                <option>MCNA</option>
                                <option>MEDICAID</option>
                                <option>MERCER ADMINISTRATION</option>
                                <option>Met Life</option>
                                <option>Pacificare Life and Health</option>
                                <option>PERFORMAX</option>
                                <option>Plan Administrators Incorporated</option>
                                <option>PRINCIPAL</option>
                                <option>PRIVATE HEALTH CARE SYSTEMS</option>
                                <option>RELIANCE STANDARD LIFE INS CO.</option>
                                <option>Securian Dental</option>
                                <option>Security Life Insurance Company </option>
                                <option>Sentry Life Insurance Company</option>
                                <option>SMITH ADMINISTRATORS</option>
                                <option>SOUTH CENTRAL</option>
                                <option>Spirit</option>
                                <option>STANDARD INS CO.</option>
                                <option>Sun Life Dental Claims</option>
                                <option>TEXAS CHIP DENTAL SERVICES</option>
                                <option>The Champion Group EBPT, Entrust</option>
                                <option>Tower Life Insurance Co. </option>
                                <option>UMR</option>
                                <option>United Concordia </option>
                                <option>United Health Care </option>
                                <option>United States Life (AIG)</option>
                                <option>Washington Dental Service</option>
                                <option>Wausau</option>
                            </datalist>
                            <label  style="font-size: min(4.5vw, 18px);" for="firstNameInput">Insurance provider *</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == false && this.formDetails.insurance != ''" class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.groupNumber" style="font-size: min(4.5vw, 18px);" class="form-control" id="firstNameInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="firstNameInput">Group number *</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == true || this.formDetails.insurance == ''" class="form-floating" style="margin-bottom: 35px;">
                            <input style="font-size: min(4.5vw, 18px);" class="form-control" id="firstNameInput" placeholder="name@example.com" disabled>
                            <label  style="font-size: min(4.5vw, 18px);" for="firstNameInput">Group number</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == false && this.formDetails.insurance != ''" class="form-floating" style="margin-bottom: 30px;">
                            <input v-model="this.formDetails.memberID" style="font-size: min(4.5vw, 18px);" class="form-control" id="firstNameInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="firstNameInput">Member ID *</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == true || this.formDetails.insurance == ''" class="form-floating" style="margin-bottom: 30px;">
                            <input style="font-size: min(4.5vw, 18px);" class="form-control" id="firstNameInput" placeholder="name@example.com" disabled>
                            <label  style="font-size: min(4.5vw, 18px);" for="firstNameInput">Member ID</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == false && this.formDetails.insurance != ''" class="form-check text-start" style="margin-bottom: 30px;">
                            <input class="form-check-input" @change="sameAsPatient()" type="checkbox" value="" id="sameAsPatient">
                            <label class="form-check-label" for="flexCheckDefault">
                                Policy holder same as patient?
                            </label>
                        </div>
                        <div v-if="this.formDetails.uninsured == true || this.formDetails.insurance == ''" class="form-check text-start" style="margin-bottom: 30px;">
                            <input class="form-check-input" @change="sameAsPatient()" type="checkbox" value="" id="sameAsPatient" disabled>
                            <label class="form-check-label" for="flexCheckDefault">
                                Policy holder same as patient?
                            </label>
                        </div>
                        <div v-if="this.formDetails.uninsured == false && this.formDetails.insurance != ''" class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.phDOB" @change="validatePolicyHolderDate()" type="date" style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">Policy holder date of birth *</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == true || this.formDetails.insurance == ''" class="form-floating" style="margin-bottom: 35px;">
                            <input type="date" style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com" disabled>
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">Policy holder date of birth</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == false && this.formDetails.insurance != ''" class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.phFirstName" style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">Policy holder first name *</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == true || this.formDetails.insurance == ''" class="form-floating" style="margin-bottom: 35px;">
                            <input style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com" disabled>
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">Policy holder first name</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == false && this.formDetails.insurance != ''" class="form-floating" style="margin-bottom: 35px;">
                            <input v-model="this.formDetails.phLastName" style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com">
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">Policy holder last name *</label>
                        </div>
                        <div v-if="this.formDetails.uninsured == true || this.formDetails.insurance == ''" class="form-floating" style="margin-bottom: 35px;">
                            <input style="font-size: min(4.5vw, 18px);" class="form-control" id="floatingInput" placeholder="name@example.com" disabled>
                            <label  style="font-size: min(4.5vw, 18px);" for="floatingInput">Policy holder last name</label>
                        </div>
                        <div class="form-floating mt-2 mb-4">
                            <button v-if="this.formDetails.uninsured == true" class="btn btn-primary" @click="incrementStep(); this.getAppointments()" style="font-size: min(4.5vw, 18px);">Continue</button>
                            <button v-else-if="this.formDetails.uninsured == false && /^[A-Za-z ,.()]+$/.test(this.formDetails.insurance) == true && /^[A-Za-z0-9 -]+$/.test(this.formDetails.groupNumber) == true && /^[A-Za-z0-9 -]+$/.test(this.formDetails.memberID) == true && this.formDetails.phValidDOB == true && this.formDetails.phDOB.length == 10 && parseInt((this.formDetails.phDOB).slice(0, 5)) >= 1900 && /^[A-Za-z]+$/.test(this.formDetails.phFirstName) == true && /^[A-Za-z]+$/.test(this.formDetails.phLastName) == true" class="btn btn-primary" @click="incrementStep(); this.getAppointments()" style="font-size: min(4.5vw, 18px);">Continue</button>
                            <button v-else class="btn btn-primary" @click="incrementStep();" style="font-size: min(4.5vw, 18px);" disabled>Continue</button>
                        </div>
                    </form>
                </div>
            </div>
            <div v-if="this.currentStep == 3" class="mx-auto mt-4" style="margin-bottom: 80px; min-width: 250px; max-width: 1000px; box-shadow: 0 1px 5px rgb(0 0 0 / 0.4); border-radius: 10px;">
                <i @click="decrementStep();" id="backArrow" class="fa-solid fa-circle-arrow-left fa-xl" style="float: left; margin-top: 30px; margin-left: 5px;"></i>
                <h5 style="font-size: min(5.5vw, 22px); margin-top: 75px;">Select an appointment</h5>
                <div class="mt-5">
                    <i id="decDaySelectorArrow" @click="selectDay('decrement');" style="display: inline-block; margin-right: 15px;" i class="fa-solid fa-minus fa-xl"></i>
                    <p class="" id="daySelectorText" style="font-weight: bold; display: inline-block;">{{this.selectedDayDisplay}} </p>
                    <input v-model="calendarSelection" @change="calendarSelector();" type="date" id="calendarSelector" style="width: 31px; border-radius: 5px; display: inline-block;border-style: none;" :min="this.calendarMinSelector" :max="calendarMaxSelector">
                    <i id="incDaySelectorArrow" @click="selectDay('increment');" style="display: inline-block; margin-left: 5px;" class="fa-solid fa-plus fa-xl"></i>
                </div>
                <div class="mt-3 mb-4 overflow-auto" style="max-height: 350px;">
                    <div v-for="appointment in selectedDayAppointments" :key="appointment._id" class="col mb-5" align="center" style="min-width: 200px; max-width:400px; display: inline-block;">
                        <div :id="`appointmentSelectors${appointment.index}`" @click="selectAppointmentTime(appointment.index, appointment.appt_time)" style="width: 150px; height: 50px; box-shadow: 0 1px 5px rgb(0 0 0 / 0.4); padding-top: 13px; background: linear-gradient(130deg, rgba(57,130,224,.75) 0%, rgba(0,129,255,.75) 32%, rgba(65,96,233,.75) 62%);" class="fw-bold">{{appointment.formattedTime}}</div>
                    </div>
                    <div id="appointmentSelectors10000" style=""></div>
                    <div class="mt-2" v-if="this.selectedDayAppointments.length == 0"> No appointments available for this day </div> 
                </div>
                <div class="mx-auto mb-4" style="max-width: 75%;">
                    <h5 class="mt-5" style="font-size: min(5.5vw, 18px);">Pick a service</h5>
                    <select v-model="selectedService" style="" class="form-select mt-3" name="cars" id="cars">
                        <option></option>
                        <option>Examination</option>
                        <option>Restoration</option>
                        <option>Implant(s)</option>
                        <option>Prosthesis</option>
                        <option>Oral Hygiene</option>
                        <option>Periodontics</option>
                        <option>Endodontics</option>
                        <option>Oral Surgery</option>
                        <option>Bonding and Minor Restoration</option>
                        <option>Adjunctive Procedures</option>
                        <option>Whitening</option>
                        <option>Orthodontics</option>
                        <option>Other</option>
                    </select>    
                </div>
                <button v-if="this.selectedTime != null && this.selectedService != ''" @click="bookAppointment(); incrementStep()" class="btn btn-primary mb-5 mt-2"  style="font-size: min(4.5vw, 18px); padding-left: 25px; padding-right: 25px;">Finish</button>
                <button v-else class="btn btn-primary mb-5 mt-2"  style="font-size: min(4.5vw, 18px); padding-left: 25px; padding-right: 25px;" disabled>Finish</button>
            </div>
            <div v-if="this.currentStep == 4" class="mx-auto mt-4" style="margin-bottom: 80px; min-width: 250px; max-width: 1000px; box-shadow: 0 1px 5px rgb(0 0 0 / 0.4); border-radius: 10px; height: 600px;">
                <h5 class="" style="font-size: min(5.5vw, 18px); margin-top: 175px; padding-left: 10%; padding-right: 10%;">Thank you for choosing Smile Architects of Houston. Please Check your Email for confirmation of your appointment.</h5>
                <i class="fa-solid fa-circle-check fa-2xl" style="font-size: min(15vw, 125px); margin-top: 80px;"></i>
            </div>       
        </div>
    </div>
</template>

<script>
var localizedFormat = require('dayjs/plugin/localizedFormat')
var customParseFormat = require('dayjs/plugin/customParseFormat')
import axios from "axios"
import dayjs from "dayjs"
import advancedFormat from 'dayjs/plugin/advancedFormat'
dayjs.extend(advancedFormat)
dayjs.extend(localizedFormat)
dayjs.extend(customParseFormat)
export default {
    name: 'book_appointments_component',
    data() {
        return {
            currentStep: 1,
            selectedDayAppointments: null,
            selectedDay: null,
            selectedTime: null,
            selectedService: '',
            selectedDayFormatter: null,
            selectedDayDisplay: null,
            selectedDayIncrementer: 0,
            selectedDayIncrementerMin: null,
            lastTimeSelected: null,
            calendarMinSelector: dayjs().format('YYYY-MM-DD'),
            calendarMaxSelector: dayjs().day(41).format('YYYY-MM-DD'),
            calendarSelection: dayjs().day(1).format('YYYY-MM-DD'),
            formDetails: {
                firstName: '',
                lastName: '',
                dob: '',
                email: '',
                phone: '',
                zip: '',
                insurance: '',
                groupNumber: '',
                memberID: '',
                phDOB: '',
                phFirstName: '',
                phLastName: '',
                appointmentDate: '',
                appointmentTime: '',
                service: '',
                validDOB: false,
                phValidDOB: false,
                uninsured: false
            }
        }
    },
    methods: {
        sameAsPatient() {
            if (document.getElementById('sameAsPatient').checked == true) {
                this.formDetails.phDOB = this.formDetails.dob
                this.formDetails.phFirstName = this.formDetails.firstName
                this.formDetails.phLastName = this.formDetails.lastName
            }
            if (document.getElementById('sameAsPatient').checked == false) {
                this.formDetails.phDOB = ''
                this.formDetails.phFirstName = ''
                this.formDetails.phLastName = ''
            }
        },
        calendarSelector() {
            if (dayjs(this.calendarSelection).format('dddd') != 'Wednesday' && dayjs(this.calendarSelection).format('dddd') != 'Sunday') {
                if (dayjs().day(1).format('YYYY-MM-DD') == dayjs(this.calendarSelection).format('YYYY-MM-DD')) {
                    this.selectedDayIncrementer = 0
                    this.selectedDay =  dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                }
                else {
                    this.selectedDayIncrementer = dayjs(this.calendarSelection).diff(dayjs().day(1), 'day') + 1
                    this.selectedDay =  dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                }
            }
        },
        selectDay(option) {
            if (option == 'increment' && this.selectedDayIncrementer < 40) {
                if (this.selectedDayFormatter == 'Monday') {
                    this.selectedDayIncrementer += 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
                if (this.selectedDayFormatter == 'Tuesday') {
                    this.selectedDayIncrementer += 2
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
                if (this.selectedDayFormatter == 'Thursday') {
                    this.selectedDayIncrementer += 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
                if (this.selectedDayFormatter == 'Friday') {
                    this.selectedDayIncrementer += 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
                if (this.selectedDayFormatter == 'Saturday') {
                    this.selectedDayIncrementer += 2
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
            }
            if (option == 'decrement' && this.selectedDayIncrementer > this.selectedDayIncrementerMin) {
                if (this.selectedDayFormatter == 'Monday') {
                    this.selectedDayIncrementer -= 2
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
                if (this.selectedDayFormatter == 'Tuesday') {
                    this.selectedDayIncrementer -= 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
                if (this.selectedDayFormatter == 'Thursday') {
                    this.selectedDayIncrementer -= 2
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
                if (this.selectedDayFormatter == 'Friday') {
                    this.selectedDayIncrementer -= 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
                if (this.selectedDayFormatter == 'Saturday') {
                    this.selectedDayIncrementer -= 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.getAppointments()
                    return
                }
            }
        },
        selectAppointmentTime(index, time) {
            if (index == 'reset' && time == 'reset') {
                if (this.lastTimeSelected == null) {
                    return
                }
                if (this.lastTimeSelected > this.selectedDayAppointments.length - 1) {
                    this.lastTimeSelected = null
                    return
                }
                if (this.lastTimeSelected <= this.selectedDayAppointments.length - 1) {
                    document.getElementById(`appointmentSelectors${this.lastTimeSelected}`).style.cssText = 'width: 150px; height: 50px; box-shadow: 0 1px 5px rgb(0 0 0 / 0.4); padding-top: 13px; background: linear-gradient(130deg, rgba(57,130,224,.75) 0%, rgba(0,129,255,.75) 32%, rgba(65,96,233,.75) 62%);'
                    this.lastTimeSelected = null
                    return
                }
            }
            for (let i = 0; i < this.selectedDayAppointments.length; i++) {
                document.getElementById(`appointmentSelectors${i}`).style.cssText = 'width: 150px; height: 50px; box-shadow: 0 1px 5px rgb(0 0 0 / 0.4); padding-top: 13px; background: linear-gradient(130deg, rgba(57,130,224,.75) 0%, rgba(0,129,255,.75) 32%, rgba(65,96,233,.75) 62%);'
            }
            document.getElementById(`appointmentSelectors${index}`).style.cssText = 'width: 150px; height: 50px; box-shadow: 0 1px 5px rgb(0 0 0 / 0.4); padding-top: 13px; background-color: #292b2c; color: white;';
            this.selectedTime =  time
            this.lastTimeSelected = index
        },
        selectInsurance() {
            this.formDetails.insurance = document.getElementById('dataList').value
            if (this.formDetails.insurance == 'No insurance') {
                this.formDetails.uninsured = true
            }
            if (this.formDetails.insurance != 'No insurance') {
                this.formDetails.uninsured = false
            }
            console.log(this.formDetails.insurance)
        },
        validateDate() {
            if (dayjs(this.formDetails.dob).isValid() == true) {
                this.formDetails.validDOB = true
            }
            if (dayjs(this.formDetails.dob).isValid() == false) {
                this.formDetails.validDOB = false
            }
        },
        validatePolicyHolderDate() {
            if (dayjs(this.formDetails.phDOB).isValid() == true) {
                this.formDetails.phValidDOB = true
            }
            if (dayjs(this.formDetails.phdob).isValid() == false) {
                this.formDetails.phValidDOB = false
            }
        },
        incrementStep() {
            this.currentStep += 1
        },
        decrementStep() {
            this.currentStep -= 1
        },
        bookAppointment() {
            let apptSignUpForm = {
                patient_first_name: this.formDetails.firstName,
                patient_last_name: this.formDetails.lastName,
                patient_dob: this.formDetails.dob,
                patient_email: this.formDetails.email,
                patient_phone: this.formDetails.phone,
                patient_zip: this.formDetails.zip,
                insurance_name: this.formDetails.insurance,
                group_number: this.formDetails.groupNumber,
                member_id: this.formDetails.memberID,
                ph_first_name: this.formDetails.phFirstName,
                ph_last_name: this.formDetails.phLastName,
                ph_dob: this.formDetails.phDOB,
                appt_time: this.selectedTime,
                appt_date: dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD'),
                service: this.selectedService,
            }
            axios.post('http://localhost:3000/bookAppointment', apptSignUpForm).then(res => {
                console.log(res.data)
            })
        },
        getAppointments() {
            let apiURL = `http://localhost:3000/bookAppointment/${dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')}`;
            axios.get(apiURL).then(res => {
                res.data.sort((a, b) => (a.appt_time > b.appt_time) ? 1: - 1)
                for (let i = 0; i < res.data.length; i++) {
                    if (dayjs(dayjs(res.data[i].appt_date).format('YYYY-MM-DD') + 'T' + res.data[i].appt_time).isBefore(dayjs().add(2, 'hour'))) {
                        res.data.splice(i, 1)
                        i -= 1
                        continue
                    }
                    res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                    res.data[i].index = i
                }
                this.selectedDayAppointments = res.data
                this.selectedDayDisplay = dayjs().day(1 + this.selectedDayIncrementer).format('ddd MMMM Do')
                if (this.currentStep == 3) {
                    this.selectAppointmentTime('reset', 'reset') 
                }
                }).catch(error => {
                console.log(error)
            })
        }
    },
    created() {
        if (dayjs().format('YYYY-MM-DD') == dayjs().day(0).format('YYYY-MM-DD') || dayjs().format('YYYY-MM-DD') == dayjs().day(1).format('YYYY-MM-DD')) {
            this.selectedDay = dayjs().day(1).format('dddd MMMM Do, YYYY')
            this.selectedDayFormatter = dayjs(dayjs().day(1).format('YYYY MM DD')).format('dddd')
            this.selectedDayIncrementer = 0 
            this.calendarMinSelector = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
            this.selectedDayIncrementerMin = this.selectedDayIncrementer

        }
        if (dayjs().format('YYYY-MM-DD') == dayjs().day(2).format('YYYY-MM-DD')) {
            this.selectedDay = dayjs().day(2).format('dddd MMMM Do, YYYY')
            this.selectedDayFormatter = dayjs(dayjs().day(2).format('YYYY MM DD')).format('dddd')
            this.selectedDayIncrementer = 1 
            this.selectedDayIncrementerMin = this.selectedDayIncrementer
        }
        if (dayjs().format('YYYY-MM-DD') == dayjs().day(3).format('YYYY-MM-DD') || dayjs().format('YYYY-MM-DD') == dayjs().day(4).format('YYYY-MM-DD')) {
            this.selectedDay = dayjs().day(4).format('dddd MMMM Do, YYYY')
            this.selectedDayFormatter = dayjs(dayjs().day(4).format('YYYY MM DD')).format('dddd')
            this.selectedDayIncrementer = 3 
            this.calendarMinSelector = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
            this.selectedDayIncrementerMin = this.selectedDayIncrementer
        }
        if (dayjs().format('YYYY-MM-DD') == dayjs().day(5).format('YYYY-MM-DD')) {
            this.selectedDay = dayjs().day(5).format('dddd MMMM Do, YYYY')
            this.selectedDayFormatter = dayjs(dayjs().day(5).format('YYYY MM DD')).format('dddd')
            this.selectedDayIncrementer = 4 
            this.calendarMinSelector = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
            this.selectedDayIncrementerMin = this.selectedDayIncrementer
        }
        if (dayjs().format('YYYY-MM-DD') == dayjs().day(6).format('YYYY-MM-DD')) {
            this.selectedDay = dayjs().day(6).format('dddd MMMM Do, YYYY')
            this.selectedDayFormatter = dayjs(dayjs().day(6).format('YYYY MM DD')).format('dddd')
            this.selectedDayIncrementer = 5
            this.calendarMinSelector = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
            this.selectedDayIncrementerMin = this.selectedDayIncrementer
        }
        this.getAppointments()
        this.validDOB = false
    }

}
</script>

<style scoped>
#appointmentSelectors {
    background: rgb(57,130,224, .75);
    background: linear-gradient(130deg, rgba(57,130,224,.75) 0%, rgba(0,129,255,.75) 32%, rgba(65,96,233,.75) 62%);
}

#backArrow:hover {
    opacity: 75%;
}

#appointmentSelectors:hover {
    opacity: 85%;
}

div:focus {
    background-color:#292b2c;       
}

::-webkit-scrollbar {
width: 10px;
}

::-webkit-scrollbar-track {
box-shadow: inset 0 0 5px grey; 
border-radius: 10px;
}

::-webkit-scrollbar-thumb {
background:#292b2c;
border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
background:rgb(54, 56, 58); 
}

::-webkit-calendar-picker-indicator{
    margin-left: 0px;
    margin-right: 10px;
}
</style>