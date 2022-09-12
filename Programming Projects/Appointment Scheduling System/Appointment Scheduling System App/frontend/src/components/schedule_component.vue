<template>
    <div id="employeesComponentBody" style="min-width: 1945px;">
        <div class="bg-dark text-white" style="height: 60px; width: 100%; margin-top: 35px; border-radius: 10px; box-shadow: 0 3px 5px rgb(0 0 0 / 0.4);">
            <p class="mx-3" style="padding-top: 12px; font-weight: bold; font-size: 25px;">Scheduling Services</p>
        </div>
        <div class="mx-1 mt-4">
            <div style="width: 30%; min-width: 600px; float: left;">
                <div id="dateWindow">
                    <div class="bg-dark mt-4 text-white" style="height: 60px; border-top-left-radius: 10px; border-top-right-radius: 10px;">
                        <div>
                            <div id="decDaySelectorDiv">
                                <i id="decDaySelectorArrow" @click="selectDay('decrement')" style="margin-left: 5%; float: left; margin-top: 30px;" class="fa-solid fa-angle-left fa-xl"></i>
                            </div>
                            <p class="" id="daySelectorText" style="font-weight: bold; margin-left: 10%; float: left; margin-top: 18px;">  View Appointments: {{this.selectedDay}} </p>
                            <input v-model="calendarSelection" @change="calendarSelector();" type="date" id="calendarSelector" style="width: 28px; border-radius: 5px; float: left; margin-top: 16px; margin-left: 5px;" :min="this.calendarMinSelector" :max="calendarMaxSelector">
                            <div id="incDaySelectorDiv">
                                <i id="incDaySelectorArrow" @click="selectDay('increment')" style="margin-right: 5%; float: right; margin-top: 30px;" class="fa-solid fa-angle-right fa-xl"></i>
                            </div>
                        </div>
                    </div>
                    <div class="overflow-auto" style="max-height: 330px; min-height: 330px;">
                        <table class="table table-hover">
                                <thead class="thead-dark bg-light sticky-top" style="box-shadow: 0 0px 4px rgb(0 0 0 / 0.4); z-index: 1;">
                                    <tr>
                                        <th>Time Slot</th>
                                        <th>Patient</th>
                                        <th>Service</th>
                                        <th>Select</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="appointment in selectedDayAppointments" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> 
                                            <span v-if="appointment.patient_first_name != null && appointment.patient_last_name != null"> {{ (appointment.patient_first_name).substring(0, 1).toUpperCase() + (appointment.patient_first_name).substring(1).toLowerCase() + ' ' + (appointment.patient_last_name).substring(0, 1).toUpperCase() + (appointment.patient_last_name).substring(1).toLowerCase()}} </span>
                                            <span v-if="appointment.patient_first_name == null && appointment.patient_last_name == null">  </span>
                                            </td>
                                        <td> 
                                            <span v-if="appointment.service != null"> {{ appointment.service}} </span>
                                            <span v-if="appointment.service == null">  </span>
                                        </td>
                                        <td><input v-if="appointment.sign_up_id != null" @click="viewAppointmentDetails(appointment)" type="radio" name="viewAppointmentDetailsRadioButton"></td>
                                    </tr>
                                </tbody>
                        </table>
                    </div>
                    <div class="row bg-light fw-bold" style="padding-top: 2px; height: 40px; border-style: none; border-top: none; border-left: none; border-right: none; border-color: #292b2c; border-width: thin; box-shadow: 0 1px 4px rgb(0 0 0 / 0.4); z-index: 1; width: 99.9%; margin-left: .1px;">
                        <div class="col px-2">
                            <p class="mt-2" style="color: #292b2c; float: left;">Patient Information: {{this.patientInformation.appointmentDate}} <span v-if="this.patientInformation.appointmentDate != ''">{{' at '}}</span> <span v-if="this.patientInformation.appointmentDate == ''">{{' No appointment selected '}}</span> {{this.patientInformation.appointmentTime}}</p>
                            <div v-if="this.adminPrivilege == 'true' || this.privilege == 'write'">
                                <button v-if="this.patientInformation.showCancel == true" @click="cancelAppointment()" class="btn btn-info btn-sm mt-1" style="float: right; margin-right: 10px;">Cancel Appointment</button>
                            </div>
                        </div>
                    </div>
                    <div v-if="this.patientInformation.appointmentDate == ''" id="test" class="overflow-auto mt-1" style="max-height: 470px; min-height: 470px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;">
                        <div class="text-center" style="max-height: 470px; min-height: 470px; backdrop-filter: blur(3px);">
                            <div>
                                <h1 class="fw-light" style="font-size: 25px; padding-top: 33%;"><span class="bg-dark text-white" style="border-radius: 10px; padding-left: 50px; padding-right: 50px; padding-bottom: 4px; box-shadow: 1px 1px 5px rgb(0 0 0 / 0.6);">Select an Appointment</span></h1>
                            </div>
                        </div>
                    </div>
                    <div v-if="this.patientInformation.appointmentDate != ''" class="overflow-auto" style="max-height: 474px; min-height: 474px;">
                        <div class="row mt-2">
                            <div class="col-5 mx-2 mb-2 mt-2">
                                <p class="mb-0 fw-bold">Date of birth:</p>
                                <p class="mx-2">{{this.patientInformation.patientDOB}}</p>
                            </div>
                            <div class="col mb-2 mt-2">
                                <p class="mb-0 fw-bold">Email:</p>
                                <p class="mx-2">{{this.patientInformation.patientEmail}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-5 mx-2 mb-2 mt-2">
                                <p class="mb-0 fw-bold">Phone number:</p>
                                <p class="mx-2">{{this.patientInformation.patientPhone}}</p>
                            </div>
                            <div class="col mb-2 mt-2">
                                <p class="mb-0 fw-bold">Zip code:</p>
                                <p class="mx-2">{{this.patientInformation.patientZip}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-5 mx-2 mb-2 mt-2">
                                <p class="mb-0 fw-bold">Insurance provider:</p>
                                <p class="mx-2">{{this.patientInformation.insuranceProvider}}</p>
                            </div>
                            <div class="col mb-2 mt-2">
                                <p class="mb-0 fw-bold">Group number:</p>
                                <p class="mx-2">{{(this.patientInformation.groupNumber).substring(0).toUpperCase()}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-5 mx-2 mb-2 mt-2">
                                <p class="mb-0 fw-bold">Member ID:</p>
                                <p class="mx-2">{{(this.patientInformation.memberID).substring(0).toUpperCase()}}</p>
                            </div>
                            <div class="col">
                                <p class="mb-0 fw-bold">Policy holder first name:</p>
                                <p class="mx-2">{{(this.patientInformation.phFirstName).substring(0, 1).toUpperCase() + (this.patientInformation.phFirstName).substring(1).toLowerCase() }}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-5 mx-2 mb-2 mt-2">
                                <p class="mb-0 fw-bold">Policy holder last name:</p>
                                <p class="mx-2">{{(this.patientInformation.phLastName).substring(0, 1).toUpperCase() + (this.patientInformation.phLastName).substring(1).toLowerCase() }}</p>
                            </div>
                            <div class="col mb-2 mt-2">
                                <p class="mb-0 fw-bold">Policy holder date of birth:</p>
                                <p class="mx-2"> {{this.patientInformation.phDOB}}</p>
                            </div>
                        </div>
                    </div>
                </div>  
            </div>



            <div class="mt-4" style="width: 68%; float: left; margin-left: 19.87px;">
                <div id="dateWindow" style="height: 904px;">
                    <div class="row text-center text-white bg-dark fw-bold" style="width: 100%; height: 60px; border-top-left-radius: 10px; border-top-right-radius: 10px; margin-left: 0px;">
                        <div class="col" style="border-style: solid; border-left: none; border-top: none; border-bottom: none;">
                            <p v-if="displayWeeklyTableBool('Monday') == true" class="mt-3">Monday <i v-if="this.adminPrivilege == 'true' || this.privilege == 'write'" @click="deleteDayAppointments('Monday')" id="deleteDayButton" class="fa-solid fa-circle-xmark" style="color:white; font-weight: normal;"></i></p>
                            <p v-if="displayWeeklyTableBool('Monday') == false" class="mt-3">Monday</p>
                        </div>
                        <div class="col" style="border-style: solid; border-left: none; border-top: none; border-bottom: none;">
                            <p v-if="displayWeeklyTableBool('Tuesday') == true" class="mt-3">Tuesday <i v-if="this.adminPrivilege == 'true' || this.privilege == 'write'" @click="deleteDayAppointments('Tuesday')" id="deleteDayButton" class="fa-solid fa-circle-xmark" style="color:white; font-weight: normal;"></i></p>
                            <p v-if="displayWeeklyTableBool('Tuesday') == false" class="mt-3">Tuesday</p>
                        </div>
                        <div class="col" style="border-style: solid; border-left: none; border-top: none; border-bottom: none;">
                            <p v-if="displayWeeklyTableBool('Thursday') == true" class="mt-3">Thursday <i v-if="this.adminPrivilege == 'true' || this.privilege == 'write'" @click="deleteDayAppointments('Thursday')" id="deleteDayButton" class="fa-solid fa-circle-xmark" style="color:white; font-weight: normal;"></i></p>
                            <p v-if="displayWeeklyTableBool('Thursday') == false" class="mt-3">Thursday</p>
                        </div>
                        <div class="col" style="border-style: solid; border-left: none; border-top: none; border-bottom: none;">
                            <p v-if="displayWeeklyTableBool('Friday') == true" class="mt-3">Friday <i v-if="this.adminPrivilege == 'true' || this.privilege == 'write'" @click="deleteDayAppointments('Friday')" id="deleteDayButton" class="fa-solid fa-circle-xmark" style="color:white; font-weight: normal;"></i></p>
                            <p v-if="displayWeeklyTableBool('Friday') == false" class="mt-3">Friday</p>
                        </div>
                        <div class="col">
                            <p v-if="displayWeeklyTableBool('Saturday') == true" class="mt-3">Saturday <i v-if="this.adminPrivilege == 'true' || this.privilege == 'write'" @click="deleteDayAppointments('Saturday')" id="deleteDayButton" class="fa-solid fa-circle-xmark" style="color:white; font-weight: normal;"></i></p>
                            <p v-if="displayWeeklyTableBool('Saturday') == false" class="mt-3">Saturday</p>
                        </div>
                    </div>
                    <div style="width: 100%; margin-left: 0px;">
                        <div class="overflow-auto" style="padding: 0px; width: 261px; float: left; max-height: 331px; min-height: 331px;">
                            <table class="table table-hover" style="min-width: 261px;">
                                <tbody v-if="displayWeeklyTableBool('Monday') == true">
                                    <tr v-for="appointment in selectedWeekAppointments.monday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> 
                                            <div v-if="this.adminPrivilege == 'true' || this.privilege == 'write'">
                                                <i v-if="appointment.sign_up_id == null" @click="deleteAppointment(appointment.appt_time, appointment.appt_date)" id="deleteScheduleBuilderButton" class="fa-solid fa-circle-xmark" style="float: right; margin-top: 4px;"></i>  
                                            </div>
                                            <i v-if="appointment.sign_up_id != null" class="fa-solid fa-person" style="float: right; margin-top: 4px; margin-right: 3.5px;"></i>
                                        </td>
                                    </tr>
                                </tbody>
                                <tbody v-if="displayWeeklyTableBool('Monday') == false" class="bg-light">
                                    <tr v-for="appointment in selectedWeekAppointments.monday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="overflow-auto" style="padding: 0px; width: 261px; margin-left: 3px; float: left; max-height: 331px; min-height: 331px;">
                            <table class="table table-hover" style="min-width: 261px;">
                                <tbody v-if="displayWeeklyTableBool('Tuesday') == true">
                                    <tr v-for="appointment in selectedWeekAppointments.tuesday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> 
                                            <div v-if="this.adminPrivilege == 'true' || this.privilege == 'write'">
                                                <i v-if="appointment.sign_up_id == null" @click="deleteAppointment(appointment.appt_time, appointment.appt_date)" id="deleteScheduleBuilderButton" class="fa-solid fa-circle-xmark" style="float: right; margin-top: 4px;"></i>  
                                            </div>
                                            <i v-if="appointment.sign_up_id != null" class="fa-solid fa-person" style="float: right; margin-top: 4px; margin-right: 3.5px;"></i>
                                        </td>
                                    </tr>
                                </tbody>
                                <tbody v-if="displayWeeklyTableBool('Tuesday') == false" class="bg-light">
                                    <tr v-for="appointment in selectedWeekAppointments.tuesday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="overflow-auto" style="padding: 0px; width: 261px; margin-left: 3px; float: left; max-height: 331px; min-height: 331px;">
                            <table class="table table-hover" style="min-width: 260px;">
                                <tbody v-if="displayWeeklyTableBool('Thursday') == true">
                                    <tr v-for="appointment in selectedWeekAppointments.thursday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> 
                                            <div v-if="this.adminPrivilege == 'true' || this.privilege == 'write'">
                                                <i v-if="appointment.sign_up_id == null" @click="deleteAppointment(appointment.appt_time, appointment.appt_date)" id="deleteScheduleBuilderButton" class="fa-solid fa-circle-xmark" style="float: right; margin-top: 4px;"></i>  
                                            </div>
                                            <i v-if="appointment.sign_up_id != null" class="fa-solid fa-person" style="float: right; margin-top: 4px; margin-right: 3.5px;"></i>
                                        </td>
                                    </tr>
                                </tbody>
                                <tbody v-if="displayWeeklyTableBool('Thursday') == false" class="bg-light">
                                    <tr v-for="appointment in selectedWeekAppointments.thursday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="overflow-auto" style="padding: 0px; width: 261px; margin-left: 3px; float: left; max-height: 331px; min-height: 331px;">
                            <table class="table table-hover" style="min-width: 261px;">
                                <tbody v-if="displayWeeklyTableBool('Friday') == true">
                                    <tr v-for="appointment in selectedWeekAppointments.friday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> 
                                            <div v-if="this.adminPrivilege == 'true' || this.privilege == 'write'">
                                                <i v-if="appointment.sign_up_id == null" @click="deleteAppointment(appointment.appt_time, appointment.appt_date)" id="deleteScheduleBuilderButton" class="fa-solid fa-circle-xmark" style="float: right; margin-top: 4px;"></i>  
                                            </div>
                                            <i v-if="appointment.sign_up_id != null" class="fa-solid fa-person" style="float: right; margin-top: 4px; margin-right: 3.5px;"></i>
                                        </td>
                                    </tr>
                                </tbody>
                                <tbody v-if="displayWeeklyTableBool('Friday') == false" class="bg-light">
                                    <tr v-for="appointment in selectedWeekAppointments.friday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="overflow-auto" style="padding: 0px; width: 261px; margin-left: 3px; float: left; max-height: 331px; min-height: 331px;">
                            <table class="table table-hover">
                                <tbody v-if="displayWeeklyTableBool('Saturday') == true">
                                   <tr v-for="appointment in selectedWeekAppointments.saturday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> 
                                            <div v-if="this.adminPrivilege == 'true' || this.privilege == 'write'">
                                                <i v-if="appointment.sign_up_id == null" @click="deleteAppointment(appointment.appt_time, appointment.appt_date)" id="deleteScheduleBuilderButton" class="fa-solid fa-circle-xmark" style="float: right; margin-top: 4px;"></i>  
                                            </div>
                                            <i v-if="appointment.sign_up_id != null" class="fa-solid fa-person" style="float: right; margin-top: 4px; margin-right: 3.5px;"></i>
                                        </td>
                                    </tr>
                                </tbody>
                                <tbody v-if="displayWeeklyTableBool('Saturday') == false" class="bg-light">
                                   <tr v-for="appointment in selectedWeekAppointments.saturday" :key="appointment._id">
                                        <td> {{ appointment.formattedTime }} </td>
                                        <td> </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <div class="bg-light fw-bold" style="margin-top: 330px; padding-top: 2px; height: 40px; border-style: none; border-top: none; border-left: none; border-right: none; border-color: #292b2c; border-width: thin; box-shadow: 0 1px 4px rgb(0 0 0 / 0.4); z-index: 1;">
                        <div id="decWeekSelectorDiv" @click="selectWeek('decrement'); copyWeeks();" class="text-center h-100" style="float: left; margin-left: 2%; margin-top: 2px; padding: 5px;">
                            <i id="decWeekSelectorArrow" class="fa-solid fa-angle-left fa-xl text-start"></i>
                        </div>
                        <div class="h-100" style="float: left; margin-left: 26%; margin-bottom: 10px;">
                            <div v-if="this.adminPrivilege == 'true' || this.privilege == 'write'" style="float:left;">
                                <button v-if="this.visibility == 'not visible'" @click="toggleVisibility()" class="btn btn-info btn-sm mt-1" style="float: left;">Schedule Hidden</button>
                                <button v-if="this.visibility == 'visible'" @click="toggleVisibility()" class="btn btn-danger btn-sm mt-1" style="float: left;">Schedule Visible</button>
                            </div>
                            <div v-if="this.privilege == 'read'" style="float:left;">
                                <button v-if="this.visibility == 'not visible'"  class="btn btn-dark btn-sm mt-1" style="float: left;" disabled>Schedule Hidden</button>
                                <button v-if="this.visibility == 'visible'"  class="btn btn-dark btn-sm mt-1" style="float: left;" disabled>Schedule Visible</button>
                            </div>
                            <p class="mt-2 mx-2" style="color: #292b2c; margin-bottom: 10px; float: left;"> Build Schedule: Week of {{this.selectedWeek}}</p>
                        </div>
                        <div id="incWeekSelectorDiv" @click="selectWeek('increment'); copyWeeks();" class="text-center h-100" style="float: right; margin-right: 2%; margin-top: 2px; padding: 5px;">
                            <i id="incWeekSelectorArrow" class="fa-solid fa-angle-right fa-xl"></i>
                        </div>
                    </div>
                    <div v-if="this.privilege == 'read'" id="scheduleBuilderBackground" class="text-center" style="height: 477px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;">
                        <div class="text-center" style="max-height: 477px; min-height: 477px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px; backdrop-filter: blur(3px);">
                            <div>
                                <h1 class="fw-light" style="font-size: 25px; padding-top: 15.3%;"><span class="bg-dark text-white" style="border-radius: 10px; padding-left: 50px; padding-right: 50px; padding-bottom: 4px; box-shadow: 1px 1px 5px rgb(0 0 0 / 0.6);">you do not have permission to use this area</span></h1>
                            </div>
                        </div>
                    </div>
                    <div v-if="this.adminPrivilege == 'true' || this.privilege == 'write'" style="margin-top: 5%;">
                        <div class="row">
                            <div class="col mx-5 p-0 bg-light" style="border-radius: 10px; box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);">
                                <form onsubmit="return false">
                                    <div class="text-center fw-bold" id="addAppointment" style="height: 60px; border-top-left-radius: 10px; border-top-right-radius: 10px; border-bottom: solid;">
                                        <div class="pt-3">Add Appointment</div>
                                    </div>
                                    <div class="row p-2 mt-2">
                                        <div class="col-2">
                                            <label class="px-1" for="addAppointmentDaySelector" style="margin-top: 90%;">
                                                Day:
                                            </label>
                                        </div>
                                        <div class="col">
                                            <div @click="selectWeekDays()">
                                                <select v-model="addAppointmentDay" class="form-select mx-1 mt-4" name="addAppointmentDaySelector" id="addAppointmentDaySelector" style="width: 95%;">
                                                    <option v-if="displayWeeklyTableBool('Monday') == true">{{this.selectedWeek}}</option>
                                                    <option v-if="displayWeeklyTableBool('Tuesday') == true">{{this.selectedWeekDays.tuesday}}</option>
                                                    <option v-if="displayWeeklyTableBool('Thursday') == true">{{this.selectedWeekDays.thursday}}</option>
                                                    <option v-if="displayWeeklyTableBool('Friday') == true">{{this.selectedWeekDays.friday}}</option>
                                                    <option v-if="displayWeeklyTableBool('Saturday') == true">{{this.selectedWeekDays.saturday}}</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row p-2">
                                        <div class="col-2">
                                            <label class="px-1" for="addAppointmentDaySelector" style="margin-top: 95%;">
                                                Time:
                                            </label>
                                        </div>
                                        <div class="col">
                                            <input  v-model="addAppointmentTime" class="form-control mx-1 mt-4 mb-4" type="time" style="width: 95%;">
                                        </div>
                                    </div>
                                    <button @click="addAppointment()" class="btn btn-dark mb-5" style="margin-left: 21%; width: 74%;">Add</button>
                                </form>
                            </div>
                            <div class="col mx-5 p-0 bg-light" style="border-radius: 10px; box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);">
                                <div class="text-center fw-bold" id="addAppointment" style="height: 60px; border-top-left-radius: 10px; border-top-right-radius: 10px; border-bottom: solid;">
                                    <div class="pt-3">Copy A Day</div>
                                </div>
                                <div class="row p-2 mt-2">
                                    <div class="col-2">
                                        <label class="px-1" for="addAppointmentDaySelector" style="margin-top: 90%;">
                                            From:
                                        </label>
                                    </div>
                                    <div class="col">
                                        <div @click="selectWeekDays()">
                                            <select v-model="this.copyDayFrom" class="form-select mx-1 mt-4" name="addAppointmentDaySelector" id="addAppointmentDaySelector" style="width: 95%;">
                                                <option>{{this.selectedWeek}}</option>
                                                <option>{{this.selectedWeekDays.tuesday}}</option>
                                                <option>{{this.selectedWeekDays.thursday}}</option>
                                                <option>{{this.selectedWeekDays.friday}}</option>
                                                <option>{{this.selectedWeekDays.saturday}}</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <div class="row p-2">
                                    <div class="col-2">
                                        <label class="px-1" for="addAppointmentDaySelector" style="margin-top: 95%;">
                                            To:
                                        </label>
                                    </div>
                                    <div class="col">
                                        <div @click="selectWeekDays()">
                                            <select v-model="this.copyDayTo" class="form-select mx-1 mt-4 mb-4" name="addAppointmentDaySelector" id="addAppointmentDaySelector" style="width: 95%;">
                                                <option v-if="this.selectedWeek != this.copyDayFrom && this.displayWeeklyTableBool('Monday') == true">{{this.selectedWeek}}</option>
                                                <option v-if="this.selectedWeekDays.tuesday != this.copyDayFrom && this.displayWeeklyTableBool('Tuesday') == true">{{this.selectedWeekDays.tuesday}}</option>
                                                <option v-if="this.selectedWeekDays.thursday != this.copyDayFrom && this.displayWeeklyTableBool('Thursday') == true">{{this.selectedWeekDays.thursday}}</option>
                                                <option v-if="this.selectedWeekDays.friday != this.copyDayFrom && this.displayWeeklyTableBool('Friday') == true">{{this.selectedWeekDays.friday}}</option>
                                                <option v-if="this.selectedWeekDays.saturday != this.copyDayFrom && this.displayWeeklyTableBool('Saturday') == true">{{this.selectedWeekDays.saturday}}</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <button @click="copyAppointmentsByDay()" class="btn btn-dark mb-5" style="margin-left: 21%; width: 74%;">Copy</button>
                            </div>
                            <div class="col mx-5 p-0 bg-light" style="border-radius: 10px; box-shadow: 0 1px 4px rgb(0 0 0 / 0.4);">
                                <div class="text-center fw-bold" id="addAppointment" style="height: 60px; border-top-left-radius: 10px; border-top-right-radius: 10px; border-bottom: solid;">
                                    <div class="pt-3">Copy A Week</div>
                                </div>
                                <div class="row p-2 mt-2">
                                    <div class="col-2">
                                        <label class="px-1" for="addAppointmentDaySelector" style="margin-top: 90%;">
                                            From:
                                        </label>
                                    </div>
                                    <div class="col">
                                        <div>
                                            <select v-model="copyWeekFrom" class="form-select mx-1 mt-4" name="addAppointmentDaySelector" id="addAppointmentDaySelector" style="width: 95%;">
                                                <option> Week of {{this.selectedWeek}}</option>
                                                <option> Week of {{this.weeksToCopy.week1}}</option>
                                                <option> Week of {{this.weeksToCopy.week2}}</option>
                                                <option> Week of {{this.weeksToCopy.week3}}</option>
                                                <option> Week of {{this.weeksToCopy.week4}}</option>
                                                <option> Week of {{this.weeksToCopy.week5}}</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <div class="row p-2">
                                    <div class="col-2">
                                        <label class="px-1" for="addAppointmentDaySelector" style="margin-top: 95%;">
                                            To:
                                        </label>
                                    </div>
                                    <div class="col">
                                        <select v-model="copyWeekTo" class="form-select mx-1 mt-4 mb-4" name="addAppointmentDaySelector" id="addAppointmentDaySelector" style="width: 95%;">
                                                <option v-if="'Week of ' + this.selectedWeek != this.copyWeekFrom && this.copyWeekDisplayBool(this.selectedWeek) == true"> Week of {{this.selectedWeek}}</option>
                                                <option v-if="'Week of ' + this.weeksToCopy.week1 != this.copyWeekFrom && this.copyWeekDisplayBool(this.weeksToCopy.week1) == true"> Week of {{this.weeksToCopy.week1}}</option>
                                                <option v-if="'Week of ' + this.weeksToCopy.week2 != this.copyWeekFrom && this.copyWeekDisplayBool(this.weeksToCopy.week2) == true"> Week of {{this.weeksToCopy.week2}}</option>
                                                <option v-if="'Week of ' + this.weeksToCopy.week3 != this.copyWeekFrom && this.copyWeekDisplayBool(this.weeksToCopy.week3) == true"> Week of {{this.weeksToCopy.week3}}</option>
                                                <option v-if="'Week of ' + this.weeksToCopy.week4 != this.copyWeekFrom && this.copyWeekDisplayBool(this.weeksToCopy.week4) == true"> Week of {{this.weeksToCopy.week4}}</option>
                                                <option v-if="'Week of ' + this.weeksToCopy.week5 != this.copyWeekFrom && this.copyWeekDisplayBool(this.weeksToCopy.week5) == true"> Week of {{this.weeksToCopy.week5}}</option>
                                        </select>
                                    </div>
                                </div>
                                <button @click="copyAppointmentsByWeek()" class="btn btn-dark mb-5" style="margin-left: 21%; width: 74%;">Copy</button>
                            </div>
                        </div>
                        
                    </div>
                </div>
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
    name: 'schedule_component',
    data() {
            return {
                adminPrivilege: window.sessionStorage.getItem('adminPrivileges'),
                privilege: window.sessionStorage.getItem('privilege'),
                selectedWeek:  dayjs().day(1).format('dddd MMMM Do, YYYY'),
                selectedWeekFormatter: dayjs().day(1).format('YYYY-MM-DD'),
                selectedWeekDays: {
                    monday: dayjs().day(1).format('dddd MMMM Do, YYYY'),
                    tuesday: '',
                    thursday: '',
                    friday: '',
                    saturday: '',
                },
                weeksToCopy: {
                    week1: dayjs().day(1 + 7).format('dddd MMMM Do, YYYY'),
                    week2: dayjs().day(1 + 14).format('dddd MMMM Do, YYYY'),
                    week3: dayjs().day(1 + 21).format('dddd MMMM Do, YYYY'),
                    week4: dayjs().day(1 + 28).format('dddd MMMM Do, YYYY'),
                    week5: dayjs().day(1 + 35).format('dddd MMMM Do, YYYY')
                },
                addAppointmentDay: null,
                addAppointmentTime: null,
                copyWeekFrom: null,
                copyWeekTo: null,
                copyDayFrom: null,
                copyDayTo: null,
                selectedWeekIncrementer: 0,
                selectedDay: dayjs().day(1).format('dddd MMMM Do, YYYY'),
                selectedDayFormatter: dayjs(dayjs().day(1).format('YYYY MM DD')).format('dddd'),
                selectedDayIncrementer: 0,
                maxDay: 40,
                calendarMinSelector: dayjs().day(1).format('YYYY-MM-DD'),
                calendarMaxSelector: dayjs().day(41).format('YYYY-MM-DD'),
                calendarSelection: dayjs().day(1).format('YYYY-MM-DD'),
                selectedWeekAppointments: {
                    monday: [],
                    tuesday: [],
                    thursday: [],
                    friday: [],
                    saturday: [] 
                },
                selectedDayAppointments: null,
                visibility: null,
                patientInformation: {
                    appointmentDate: '',
                    appointmentTime: '',
                    patientDOB: '',
                    patientEmail: '',
                    patientPhone: '',
                    patientZip: '',
                    insuranceProvider: '',
                    groupNumber: '',
                    memberID: '',
                    phFirstName: '',
                    phLastName: '',
                    phDOB: '',
                    signUpID: '',
                    showCancel: false,
                    appointmentID: null
                }
            }
        },
    methods: {
        cancelAppointment() {
            if (confirm(`This operation will cancel the appointment at ${this.patientInformation.appointmentTime} on ${this.patientInformation.appointmentDate}. Are you sure you wish to perform this operation?`) == true) {
                let apiURL = 'http://localhost:3000/dashboard/scheduleByDay/cancelAppointment'
                axios.put(apiURL, [this.patientInformation.appointmentID]).then(res => {
                    if (res.data == 'canceled appointment') {
                        this.patientInformation.appointmentDate = ''
                        this.patientInformation.appointmentTime = ''
                        this.patientInformation.patientDOB = ''
                        this.patientInformation.patientEmail = ''
                        this.patientInformation.patientPhone = ''
                        this.patientInformation.patientZip = ''
                        this.patientInformation.insuranceProvider = ''
                        this.patientInformation.groupNumber = ''
                        this.patientInformation.memberID = ''
                        this.patientInformation.phFirstName = ''
                        this.patientInformation.phLastName = ''
                        this.patientInformation.phDOB = ''
                        this.patientInformation.signUpID = ''
                        this.patientInformation.showCancel = false
                        this.patientInformation.appointmentID = null
                    }
                    this.grabAppointmentsByDayFromDB()
                    this.grabAppointmentsByWeekFromDB()
                })
            }
        },
        viewAppointmentDetails(appointment) {
            this.patientInformation.appointmentDate = dayjs(appointment.appt_date).format('MMMM Do, YYYY')
            this.patientInformation.appointmentTime = dayjs('1/1/1 ' + appointment.appt_time).format('h:mm a')
            this.patientInformation.patientDOB = dayjs(appointment.patient_dob).format('MMMM Do, YYYY')
            this.patientInformation.patientEmail = appointment.patient_email
            this.patientInformation.patientPhone = appointment.patient_phone
            this.patientInformation.patientZip = appointment.patient_zip
            this.patientInformation.insuranceProvider = appointment.insurance_name
            this.patientInformation.groupNumber = appointment.group_number
            this.patientInformation.memberID = appointment.member_id
            this.patientInformation.phFirstName = appointment.ph_first_name
            this.patientInformation.phLastName = appointment.ph_last_name
            if (dayjs(appointment.ph_dob).isAfter('1/1/1900')) {
                this.patientInformation.phDOB = dayjs(appointment.ph_dob).format('MMMM Do, YYYY')
            }
            if (dayjs(appointment.ph_dob).isBefore('1/1/1900')) {
                this.patientInformation.phDOB = ''
            }
            this.patientInformation.signUpID = appointment.sign_up_id
            this.patientInformation.showCancel = dayjs(dayjs(appointment.appt_date).format('YYYY-MM-DD') + 'T' + appointment.appt_time).isAfter(dayjs())
            this.patientInformation.appointmentID = appointment.appt_id
        },
        toggleVisibility() {
            let selectedWeekStart = dayjs((this.selectedWeek.substring(this.selectedWeek.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
            let selectedWeekEnd = dayjs(selectedWeekStart).day(6).format('YYYY-MM-DD')
            let apiURL = 'http://localhost:3000/dashboard/scheduleByWeek/setVisibility'
            if (this.visibility == 'not visible') {
                if (confirm(`This operation will set appointments for the week of ${this.selectedWeek} to VISIBLE`) == true) {
                    axios.put(apiURL, [selectedWeekStart, selectedWeekEnd, 1]).then(res => { 
                        this.visibility = res.data
                        this.checkVisibility()
                        return
                    })
                }
            }
            if (this.visibility == 'visible') {
                if (confirm(`This operation will set appointments for the week of ${this.selectedWeek} to NOT VISIBLE`) == true) {
                    axios.put(apiURL, [selectedWeekStart, selectedWeekEnd, 0]).then(res => { 
                        this.visibility = res.data
                        this.checkVisibility()
                        return
                    })
                }
            }
        },
        checkVisibility() {
            let selectedWeekStart = dayjs((this.selectedWeek.substring(this.selectedWeek.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
            let selectedWeekEnd = dayjs(selectedWeekStart).day(6).format('YYYY-MM-DD')
            let apiURL = `http://localhost:3000/dashboard/scheduleByWeek/checkVisibility/${selectedWeekStart}/${selectedWeekEnd}`
            axios.get(apiURL).then(res => {
                console.log(res.data)
                this.visibility = res.data
            })
        },
        copyWeekDisplayBool(week) {
            let formattedWeek = dayjs((week.substring(week.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
            let currentWeekStart = dayjs().day(1).format('YYYY-MM-DD')
            if (formattedWeek != currentWeekStart) {
                return true
            }
            if (formattedWeek == currentWeekStart) {
                return false
            }
        },
        displayWeeklyTableBool(weekday) {
            let selectedWeek = dayjs((this.selectedWeek.substring(this.selectedWeek.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
            if (weekday == 'Monday') {
                if ((dayjs(selectedWeek).day(1)).isAfter(dayjs())) {
                    return true
                }
                else {
                    return false
                }
            }
            if (weekday == 'Tuesday') {
                if ((dayjs(selectedWeek).day(2)).isAfter(dayjs())) {
                    return true
                }
                else {
                    return false
                }
            }
            if (weekday == 'Thursday') {
                if ((dayjs(selectedWeek).day(4)).isAfter(dayjs())) {
                    return true
                }
                else {
                    return false
                }
            }   
            if (weekday == 'Friday') {
                if ((dayjs(selectedWeek).day(5)).isAfter(dayjs())) {
                    return true
                }
                else {
                    return false
                }
            }
            if (weekday == 'Saturday') {
                if ((dayjs(selectedWeek).day(6)).isAfter(dayjs())) {
                    return true
                }
                else {
                    return false
                }
            }         
        },
        addAppointment() {
            if (this.addAppointmentTime != null && this.addAppointmentDay != null) {
                let apiURL = `http://localhost:3000/dashboard/scheduleByWeek/addAppointment`
                let time = this.addAppointmentTime + ':00'
                let day = dayjs((this.addAppointmentDay.substring(this.addAppointmentDay.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
                let currentDaySelected = dayjs((this.selectedDay.substring(this.selectedDay.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
                axios.post(apiURL, [time, day]).then(res => {
                    console.log(res.data)
                    this.grabAppointmentsByWeekFromDB()
                    if (day == currentDaySelected) {
                        this.grabAppointmentsByDayFromDB()
                    }
                    this.checkVisibility()
                })
            }
            if (this.addAppointmentTime == null) {
                alert('Please enter a valid day and time.')
            }
        },
        deleteAppointment(appt_time, appt_date) {
            let apiURL = `http://localhost:3000/dashboard/scheduleByWeek/deleteAppointment/${appt_time}/${dayjs(appt_date).format('YYYY-MM-DD')}`
            let day = dayjs(appt_date).format('YYYY-MM-DD')
            let currentDaySelected = dayjs((this.selectedDay.substring(this.selectedDay.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
            console.log(day)
            console.log(currentDaySelected)
            axios.delete(apiURL).then(res => {
                console.log(res.data)
                this.grabAppointmentsByWeekFromDB()
                if (day == currentDaySelected) {
                    this.grabAppointmentsByDayFromDB()
                }
            })
        },
        deleteDayAppointments(day) {
            let weekStart = dayjs(((this.selectedWeek).replace('Monday ', '')).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
            let currentDaySelected = dayjs((this.selectedDay.substring(this.selectedDay.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
            if (day == 'Monday') {
                day = dayjs(weekStart).day(1).format('YYYY-MM-DD')
            }
            if (day == 'Tuesday') {
                day = dayjs(weekStart).day(2).format('YYYY-MM-DD')
            }
            if (day == 'Thursday') {
                day = dayjs(weekStart).day(4).format('YYYY-MM-DD')
            }
            if (day == 'Friday') {
                day = dayjs(weekStart).day(5).format('YYYY-MM-DD')
            }
            if (day == 'Saturday') {
                day = dayjs(weekStart).day(6).format('YYYY-MM-DD')
            }
            if (dayjs(day).diff(dayjs(), 'day') >= 0) {
                if (confirm(`This operation will delete all patientless appointments on ${dayjs(day).format('dddd MMMM Do, YYYY')} Are you sure you wish to perform this operation?`) == true) {
                    let apiURL = `http://localhost:3000/dashboard/scheduleByWeek/deleteDayAppointments/${dayjs(day).format('YYYY-MM-DD')}`
                    axios.delete(apiURL).then(res => {
                        console.log(res.data)
                        this.grabAppointmentsByWeekFromDB()
                        if (day == currentDaySelected) {
                            this.grabAppointmentsByDayFromDB()
                        }
                    })
                }
            }
        },
        copyAppointmentsByWeek() {
            if(confirm(`This operation will add the appointments from ${this.copyWeekFrom} to ${this.copyWeekTo} if they don't already exist. Are you sure you wish to perform this operation?`) == true) {
                if (this.copyWeekFrom != null && this.copyWeekTo != null) {
                    let fromWeekStart = dayjs(((this.copyWeekFrom).replace('Week of Monday ', '')).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
                    let fromWeekEnd = dayjs(fromWeekStart).day(6).format('YYYY-MM-DD')
                    let toWeekStart = dayjs(((this.copyWeekTo).replace('Week of Monday ', '')).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
                    let toWeekEnd = dayjs(toWeekStart).day(6).format('YYYY-MM-DD')
                    let apiURL = `http://localhost:3000/dashboard/scheduleByWeek/copyWeek`
                    axios.post(apiURL, [fromWeekStart, fromWeekEnd, toWeekStart, toWeekEnd]).then(res => {
                        console.log(res.data)
                        this.grabAppointmentsByWeekFromDB()
                        let currentDaySelected = dayjs((this.selectedDay.substring(this.selectedDay.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
                        if (dayjs(toWeekStart).isSame(currentDaySelected, 'week')) {
                            this.grabAppointmentsByDayFromDB()
                        }
                        this.checkVisibility()
                    })
                }
                else {
                    alert('Please select a FROM date and a TO date to copy the schedule of a week')
                }
            }
        },
        copyAppointmentsByDay() {
                if (this.copyDayFrom != null && this.copyDayTo != null) {
                    let fromDayChecker = dayjs((this.copyDayFrom.substring(this.copyDayFrom.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('dddd')
                    let toDay = dayjs((this.copyDayTo.substring(this.copyDayTo.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
                    let appointments = null
                    if (fromDayChecker == 'Monday') {
                        appointments = this.selectedWeekAppointments.monday
                    }
                    if (fromDayChecker == 'Tuesday') {
                        appointments = this.selectedWeekAppointments.tuesday
                    }
                    if (fromDayChecker == 'Thursday') {
                        appointments = this.selectedWeekAppointments.thursday
                    }
                    if (fromDayChecker == 'Friday') {
                        appointments = this.selectedWeekAppointments.friday
                    }
                    if (fromDayChecker == 'Saturday') {
                        appointments = this.selectedWeekAppointments.saturday
                    }
                    for (let i = 0; i < appointments.length; i++) {
                        appointments[i].appt_date = dayjs(appointments[i].appt_date).format('YYYY-MM-DD')
                    }
                    if(confirm(`This operation will add the appointments from ${this.copyDayFrom} to ${this.copyDayTo} if they don't already exist. Are you sure you wish to perform this operation?`) == true) {
                        let apiURL = `http://localhost:3000/dashboard/scheduleByWeek/copyDay`
                        axios.post(apiURL, [toDay, appointments]).then(res => {
                            console.log(res.data)
                            this.grabAppointmentsByWeekFromDB()
                            let currentDaySelected = dayjs((this.selectedDay.substring(this.selectedDay.indexOf(' ') + 1)).replace(',', ''), 'MMMM Do YYYY').format('YYYY-MM-DD')
                            if (toDay == currentDaySelected) {
                                this.grabAppointmentsByDayFromDB()
                            }
                        })
                    }
                }
                else {
                    alert('Please select a FROM date and a TO date to copy the schedule of a day')
                }
            
        },
        copyWeeks() {
            if (this.selectedWeekIncrementer == 0) {
                this.weeksToCopy.week1 = dayjs().day(1 + 7).format('dddd MMMM Do, YYYY')
                this.weeksToCopy.week2 = dayjs().day(1 + 14).format('dddd MMMM Do, YYYY')
                this.weeksToCopy.week3 = dayjs().day(1 + 21).format('dddd MMMM Do, YYYY')
                this.weeksToCopy.week4 = dayjs().day(1 + 28).format('dddd MMMM Do, YYYY')
                this.weeksToCopy.week5 = dayjs().day(1 + 35).format('dddd MMMM Do, YYYY')
            }
            if (this.selectedWeekIncrementer != 0) {
                var incrementers = [0, 7, 14, 21, 28, 35]
                const index = incrementers.indexOf(this.selectedWeekIncrementer)
                incrementers.splice(index, 1)
                this.weeksToCopy.week1 = dayjs().day(1 + incrementers[0]).format('dddd MMMM Do, YYYY')
                this.weeksToCopy.week2 = dayjs().day(1 + incrementers[1]).format('dddd MMMM Do, YYYY')
                this.weeksToCopy.week3 = dayjs().day(1 + incrementers[2]).format('dddd MMMM Do, YYYY')
                this.weeksToCopy.week4 = dayjs().day(1 + incrementers[3]).format('dddd MMMM Do, YYYY')
                this.weeksToCopy.week5 = dayjs().day(1 + incrementers[4]).format('dddd MMMM Do, YYYY')
            }
        },
        selectWeekDays() {
            this.selectedWeekDays.tuesday = dayjs().day(2 + this.selectedWeekIncrementer).format('dddd MMMM Do, YYYY')
            this.selectedWeekDays.thursday = dayjs().day(4 + this.selectedWeekIncrementer).format('dddd MMMM Do, YYYY')
            this.selectedWeekDays.friday = dayjs().day(5 + this.selectedWeekIncrementer).format('dddd MMMM Do, YYYY')
            this.selectedWeekDays.saturday = dayjs().day(6 + this.selectedWeekIncrementer).format('dddd MMMM Do, YYYY')
        },
        selectWeek(option) {
            if (option == 'increment' && this.selectedWeekIncrementer != 35) {
                this.selectedWeekIncrementer += 7
                this.selectedWeek = dayjs().day(1 + this.selectedWeekIncrementer).format('dddd MMMM Do, YYYY')
                this.selectedWeekFormatter = dayjs().day(1 + this.selectedWeekIncrementer).format('YYYY-MM-DD')
                this.addAppointmentDay = this.selectedWeek
                this.copyWeekFrom = null
                this.copyWeekTo = null
                this.copyDayFrom = null
                this.copyDayTo = null
                this.grabAppointmentsByWeekFromDB()
                this.checkVisibility()
            }
            if (option == 'decrement' && this.selectedWeekIncrementer != 0) {
                this.selectedWeekIncrementer -= 7
                this.selectedWeek = dayjs().day(1 + this.selectedWeekIncrementer).format('dddd MMMM Do, YYYY')
                this.selectedWeekFormatter = dayjs().day(1 + this.selectedWeekIncrementer).format('YYYY-MM-DD')
                this.addAppointmentDay = this.selectedWeek
                this.copyWeekFrom = null
                this.copyWeekTo = null
                this.copyDayFrom = null
                this.copyDayTo = null
                this.grabAppointmentsByWeekFromDB()
                this.checkVisibility()
            }
        },
        formatTheTimeForDisplay(appt_time) {
            appt_time = dayjs('1/1/1 ' + appt_time).format('h:mm a')
            return appt_time
        },
        grabAppointmentsByWeekFromDB() {
            let apiURL = `http://localhost:3000/dashboard/scheduleByWeek/${this.selectedWeekFormatter}/${dayjs(this.selectedWeekFormatter).day(6).format('YYYY-MM-DD')}`;
            axios.get(apiURL).then(res => {
                res.data.sort((a, b) => (a.appt_time < b.appt_time) ? 1: - 1)
                this.selectedWeekAppointments.monday = []
                this.selectedWeekAppointments.tuesday = []
                this.selectedWeekAppointments.thursday = []
                this.selectedWeekAppointments.friday = []
                this.selectedWeekAppointments.saturday = []
                for (let i = 0; i < res.data.length; i++) {
                    if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer).format('YYYY-MM-DD')) {
                        res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                        this.selectedWeekAppointments.monday.push(res.data[i])
                    }
                    if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer + 1).format('YYYY-MM-DD')) {
                        res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                        this.selectedWeekAppointments.tuesday.push(res.data[i])
                    }
                    if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer + 3).format('YYYY-MM-DD')) {
                        res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                        this.selectedWeekAppointments.thursday.push(res.data[i])
                    }
                    if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer + 4).format('YYYY-MM-DD')) {
                        res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                        this.selectedWeekAppointments.friday.push(res.data[i])
                    }
                    if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer + 5).format('YYYY-MM-DD')) {
                        res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                        this.selectedWeekAppointments.saturday.push(res.data[i])
                    }
                }
                }).catch(error => {
                console.log(error)
            })
        },
        calendarSelector() {
            if (dayjs(this.calendarSelection).format('dddd') != 'Wednesday' && dayjs(this.calendarSelection).format('dddd') != 'Sunday') {
                if (dayjs().day(1).format('YYYY-MM-DD') == dayjs(this.calendarSelection).format('YYYY-MM-DD')) {
                    this.selectedDayIncrementer = 0
                    this.selectedDay =  dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.grabAppointmentsByDayFromDB() 
                }
                else {
                    this.selectedDayIncrementer = dayjs(this.calendarSelection).diff(dayjs().day(1), 'day') + 1
                    this.selectedDay =  dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.grabAppointmentsByDayFromDB() 
                }
            }
        },
        grabAppointmentsByDayFromDB() {
            let apiURL = `http://localhost:3000/dashboard/scheduleByDay/${dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')}`;
            axios.get(apiURL).then(res => {
                res.data.sort((a, b) => (a.appt_time > b.appt_time) ? 1: - 1)
                for (let i = 0; i < res.data.length; i++) {
                    res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                }
                this.selectedDayAppointments = res.data
                }).catch(error => {
                console.log(error)
            })
        },
        selectDay(option) {
            if (option == 'increment' && this.selectedDayIncrementer < this.maxDay) {
                if (this.selectedDayFormatter == 'Monday') {
                    this.selectedDayIncrementer += 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
                if (this.selectedDayFormatter == 'Tuesday') {
                    this.selectedDayIncrementer += 2
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
                if (this.selectedDayFormatter == 'Thursday') {
                    this.selectedDayIncrementer += 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
                if (this.selectedDayFormatter == 'Friday') {
                    this.selectedDayIncrementer += 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
                if (this.selectedDayFormatter == 'Saturday') {
                    this.selectedDayIncrementer += 2
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
            }
            if (option == 'decrement' && this.selectedDayIncrementer != 0) {
                if (this.selectedDayFormatter == 'Monday') {
                    this.selectedDayIncrementer -= 2
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
                if (this.selectedDayFormatter == 'Tuesday') {
                    this.selectedDayIncrementer -= 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
                if (this.selectedDayFormatter == 'Thursday') {
                    this.selectedDayIncrementer -= 2
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
                if (this.selectedDayFormatter == 'Friday') {
                    this.selectedDayIncrementer -= 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
                if (this.selectedDayFormatter == 'Saturday') {
                    this.selectedDayIncrementer -= 1
                    this.selectedDay = dayjs().day(1 + this.selectedDayIncrementer).format('dddd MMMM Do, YYYY')
                    this.selectedDayFormatter = dayjs(dayjs().day(1 + this.selectedDayIncrementer).format('YYYY MM DD')).format('dddd')
                    this.calendarSelection = dayjs().day(1 + this.selectedDayIncrementer).format('YYYY-MM-DD')
                    this.grabAppointmentsByDayFromDB() 
                    return
                }
            }
        }
    },
    created() {
        if (dayjs().format('dddd') == 'Wednesday') {
            this.selectedDay = dayjs().day(4).format('dddd MMMM Do, YYYY')
            this.selectedDayIncrementer = 3
            this.selectedDayFormatter = dayjs(dayjs().day(4).format('YYYY MM DD')).format('dddd')
            this.calendarSelection = dayjs().day(4).format('YYYY-MM-DD')
        }
        if (dayjs().format('dddd') == 'Sunday') {
            this.selectedDay = dayjs().day(1).format('dddd MMMM Do, YYYY')
            this.selectedDayIncrementer = 0
            this.selectedDayFormatter = dayjs(dayjs().day(1).format('YYYY MM DD')).format('dddd')
            this.calendarSelection = dayjs().day(1).format('YYYY-MM-DD')
        }
        if (dayjs().format('dddd') == 'Tuesday') {
            this.selectedDay = dayjs().day(2).format('dddd MMMM Do, YYYY')
            this.selectedDayIncrementer = 1
            this.selectedDayFormatter = dayjs(dayjs().day(2).format('YYYY MM DD')).format('dddd')
            this.calendarSelection = dayjs().day(2).format('YYYY-MM-DD')
        }
        if (dayjs().format('dddd') == 'Thursday') {
            this.selectedDay = dayjs().day(4).format('dddd MMMM Do, YYYY')
            this.selectedDayIncrementer = 3
            this.selectedDayFormatter = dayjs(dayjs().day(4).format('YYYY MM DD')).format('dddd')
            this.calendarSelection = dayjs().day(4).format('YYYY-MM-DD')
        }
        if (dayjs().format('dddd') == 'Friday') {
            this.selectedDay = dayjs().day(5).format('dddd MMMM Do, YYYY')
            this.selectedDayIncrementer = 4
            this.selectedDayFormatter = dayjs(dayjs().day(5).format('YYYY MM DD')).format('dddd')
            this.calendarSelection = dayjs().day(5).format('YYYY-MM-DD')
        }
        if (dayjs().format('dddd') == 'Saturday') {
            this.selectedDay = dayjs().day(6).format('dddd MMMM Do, YYYY')
            this.selectedDayIncrementer = 5
            this.selectedDayFormatter = dayjs(dayjs().day(6).format('YYYY MM DD')).format('dddd')
            this.calendarSelection = dayjs().day(6).format('YYYY-MM-DD')
        }
        let apiURL = `http://localhost:3000/dashboard/scheduleByWeek/${this.selectedWeekFormatter}/${dayjs(this.selectedWeekFormatter).day(6).format('YYYY-MM-DD')}`;
        axios.get(apiURL).then(res => {
            res.data.sort((a, b) => (a.appt_time < b.appt_time) ? 1: - 1)
            for (let i = 0; i < res.data.length; i++) {
                if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer).format('YYYY-MM-DD')) {
                    res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                    this.selectedWeekAppointments.monday.push(res.data[i])
                }
                if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer + 1).format('YYYY-MM-DD')) {
                    res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                    this.selectedWeekAppointments.tuesday.push(res.data[i])
                }
                if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer + 3).format('YYYY-MM-DD')) {
                    res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                    this.selectedWeekAppointments.thursday.push(res.data[i])
                }
                if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer + 4).format('YYYY-MM-DD')) {
                    res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                    this.selectedWeekAppointments.friday.push(res.data[i])
                }
                if (dayjs(res.data[i].appt_date).format('YYYY-MM-DD') == dayjs().day(1 + this.selectedWeekIncrementer + 5).format('YYYY-MM-DD')) {
                    res.data[i].formattedTime = dayjs('1/1/1 ' + res.data[i].appt_time).format('h:mm a')
                    this.selectedWeekAppointments.saturday.push(res.data[i])
                }
            }
            }).catch(error => {
            console.log(error)
        })
        this.grabAppointmentsByDayFromDB() 
        this.checkVisibility()
    }
} 
//console.log(dayjs().day(1).format('dddd MMMM YYYY'))
// var test = dayjs('2022-03-30').day(1).$d
// var formatted = test.toISOString().split('T')[0]
// console.log(formatted)
//console.log(dayjs('2022-03-27', 'week').isSame('2022-03-26', 'week'))
</script>

<style scoped>
::-webkit-scrollbar {
    display: none;
}

#decWeekSelectorDiv:hover #decWeekSelectorArrow {
    opacity: 50%; 
}

#incWeekSelectorDiv:hover #incWeekSelectorArrow {
    opacity: 50%;
}

#incDaySelectorDiv:hover #incDaySelectorArrow {
    opacity: 50%;   
}

#calendarSelector:hover {
    opacity: 60%;
}

#decDaySelectorDiv:hover #decDaySelectorArrow {
    opacity: 50%; 
}

#dateWindow {
    border-radius: 10px; 
    box-shadow: 0 1px 8px rgb(0 0 0 / 0.4);
}

#deleteScheduleBuilderButton:hover {
    opacity: 60%;
}

#deleteDayButton:hover {
    opacity: 60%;
}

::-webkit-calendar-picker-indicator{
    margin-left: 0px;
    margin-right: 3px;
}

#test {
    background-image: url("../assets/patientInformationBackground.png");
    background-repeat: no-repeat;
    background-size: cover;
}

#scheduleBuilderBackground {
    background-image: url("../assets/scheduleBuilderBackground.png");
    background-repeat: no-repeat;
    background-size: cover;
}
</style>