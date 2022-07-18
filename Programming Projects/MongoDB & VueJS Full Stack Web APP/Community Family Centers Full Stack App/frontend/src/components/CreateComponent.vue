<!-- This is to create a client that can be added to the database/ this is based off of the given intake form -->
<template>
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h3 class="text-center">Create Client</h3>
            <form @submit.prevent="handleSubmitForm">
                <div class="form-group">
                    <label>Family Number</label>
                    <input type="number" class="form-control" v-model="client.familyNo" required>
                </div>
                <div class="form-group">
                    <label>Client Number</label>
                    <input type="number" class="form-control" v-model="client.clientNo" required>
                </div>
                <div class="form-group">
                    <label>Start Date</label>
                    <input type="date" class="form-control" v-model="client.startDate" required>
                </div>
                <div class="form-group">
                    <label>Close Date</label>
                    <input type="date" class="form-control" v-model="client.closeDate" required>
                </div>

                <!--How do format in new sections?? -->
                <br><p>GENERAL INFORMATION</p>
                
                <div class="form-group">
                    <label>First Name</label>
                    <input type="string" class="form-control" v-model="client.firstName" required>
                </div>
                <div class="form-group">
                    <label>Last Name</label>
                    <input type="string" class="form-control" v-model="client.lastName" required>
                </div>
                <div class="form-group">
                    <label>Middle Name</label>
                    <input type="string" class="form-control" v-model="client.middleName">
                </div>
                <div class="form-group">
                    <label>Birthday</label>
                    <input type="date" class="form-control" v-model="client.birthDate" required>
                </div>
                <div class="form-group">
                    <label>Social Number</label>
                    <input type="number" class="form-control" v-model="client.socialNumber" required>
                </div>
                <div class="form-group">
                    <label>Other Document</label>
                    <input type="string" class="form-control" v-model="client.otherDocument" >
                </div>
                <div class="form-group">
                    <label>Gender</label>
                    <input type="string" class="form-control" v-model="client.gender" >
                </div>
                <div class="form-group">
                    <label>Texas ID or Driver's License Number</label>
                    <input type="number" class="form-control" v-model="client.txIDorLicense" required>
                </div>

                <br><p>RESIDENCE INFORMATION</p>

                <div class="form-group">
                    <label>Address</label>
                    <input type="string" class="form-control" v-model="client.address" >
                </div>
                <div class="form-group">
                    <label>City</label>
                    <input type="string" class="form-control" v-model="client.city" >
                </div>
                <div class="form-group">
                    <label>State</label>
                    <input type="string" class="form-control" v-model="client.state" >
                </div>
                <div class="form-group">
                    <label>Zip Code</label>
                    <input type="number" class="form-control" v-model="client.zip" >
                </div>
                <div class="form-group">
                    <label>County</label>
                    <input type="string" class="form-control" v-model="client.county" >
                </div>
                <div class="form-group">
                    <label>Residency Length in Years</label>
                    <input type="number" class="form-control" v-model="client.residencyLengthYears" >
                </div>
                <!-- Make a dropdown?? for the next 4 -->
                <div id="v-model-select" class="form-group">
                    <label>Living Arrangements</label>
                    <select v-model="client.livingArrangements">
                        <option disabled value="">Please select one</option>
                        <option>Renting</option>
                        <option>Owner of House/Trailer</option>
                        <option>Staying with Friends/Family</option>
                        <option>Staying In Shelter/ Hotel</option>
                        <option>Living in Car/Tent</option>
                        <option>Traveling Through the Area</option>
                    </select>
                    <span>Selected: {{ client.livingArrangements }}</span>
                </div>
                <div class="form-group">
                    <label>Utilities Included</label>
                    <input type="string" class="form-control" v-model="client.includedUtilities" >
                </div>
                <div class="form-group">
                    <label>Subsidized Rent</label>
                    <input type="string" class="form-control" v-model="client.subsidizedRent" >
                </div>
                <div class="form-group">
                    <label>Single Parent</label>
                    <input type="string" class="form-control" v-model="client.singleParent" >
                </div>

                <br><p>CONTACT INFORMATION</p>

                <div class="form-group">
                    <label>Home Phone</label>
                    <input type="string" class="form-control" v-model="client.homePhone" >
                </div>
                <div class="form-group">
                    <label>Work Phone</label>
                    <input type="string" class="form-control" v-model="client.workPhone" >
                </div>
                <div class="form-group">
                    <label>Cell Phone</label>
                    <input type="string" class="form-control" v-model="client.cellPhone" >
                </div>
                <div class="form-group">
                    <label>Other Phone</label>
                    <input type="string" class="form-control" v-model="client.otherPhone" >
                </div>
                <div class="form-group">
                    <label>Personal Email</label>
                    <input type="string" class="form-control" v-model="client.personalEmail" >
                </div>
                <div class="form-group">
                    <label>Other Email</label>
                    <input type="string" class="form-control" v-model="client.otherEmail" >
                </div>
                <div class="form-group">
                    <label>Marital Status</label>
                    <input type="string" class="form-control" v-model="client.maritalStatus" >
                </div>
                <div class="form-group">
                    <label>Language</label>
                    <input type="string" class="form-control" v-model="client.language" >
                </div>
                <div class="form-group">
                    <label>Ethnicity</label>
                    <input type="string" class="form-control" v-model="client.ethnicity" >
                </div>
                <div class="form-group">
                    <label>Priority Population</label>
                    <input type="string" class="form-control" v-model="client.priorityPopulation" >
                </div>
                <div class="form-group">
                    <label>Pregnancy</label>
                    <input type="string" class="form-control" v-model="client.pregnancy" >
                </div>
                <div class="form-group">
                    <label>Teen Parent</label>
                    <input type="string" class="form-control" v-model="client.teenParent" >
                </div>
                <div class="form-group">
                    <label>Months until Delivery</label>
                    <input type="string" class="form-control" v-model="client.deliveryDateMonths" >
                </div>

                <br><p>EMPLOYMENT INFORMATION</p>

                <!--Employed Section-->
                <div class="form-group">
                    <label>Years Employed</label>
                    <input type="number" class="form-control" v-model="client.yearsEmployed" >
                </div>
                <div class="form-group">
                    <label>Employer</label>
                    <input type="string" class="form-control" v-model="client.employer" >
                </div>
                <div class="form-group">
                    <label>Occupation</label>
                    <input type="string" class="form-control" v-model="client.occupation" >
                </div>
                <br><p>Unemployed Section</p>
                <div class="form-group">
                    <label>Years Unemployed</label>
                    <input type="number" class="form-control" v-model="client.yearsUnemployed" >
                </div>
                <br><p>Retired Section</p>
                <div class="form-group">
                    <label>Years Retired</label>
                    <input type="number" class="form-control" v-model="client.yearsRetired" >
                </div>
                <br><p>Housewife Section</p>
                <div class="form-group">
                    <label>Housewife</label>
                    <input type="string" class="form-control" v-model="client.housewife" >
                </div>

                <br><p>EDUCATION INFORMATION</p>

                <div class="form-group">
                    <label>Attended School</label>
                    <input type="string" class="form-control" v-model="client.attendedSchool" >
                </div>
                <div class="form-group">
                    <label>Name of School</label>
                    <input type="string" class="form-control" v-model="client.nameofSchool" >
                </div>
                <div class="form-group">
                    <label>Last Completed Grade</label>
                    <input type="string" class="form-control" v-model="client.lastCompletedGrade" >
                </div>
                <div class="form-group">
                    <label>Graduated</label>
                    <input type="string" class="form-control" v-model="client.graduated" >
                </div>
                <div class="form-group">
                    <label>Level Graduated</label>
                    <input type="string" class="form-control" v-model="client.levelGraduated" >
                </div>
                <div class="form-group">
                    <label>Certification</label>
                    <input type="string" class="form-control" v-model="client.certification" >
                </div>

                <br><p>INCOME INFORMATION</p>

                <div class="form-group">
                    <label>Head of Household</label>
                    <input type="string" class="form-control" v-model="client.headOfHousehold" >
                </div>
                <div class="form-group">
                    <label>Monthly Income</label>
                    <input type="string" class="form-control" v-model="client.monthlyIncome" >
                </div>
                <div class="form-group">
                    <label>Other Income</label>
                    <input type="string" class="form-control" v-model="client.otherIncome" >
                </div>
                <div class="form-group">
                    <label>Spousal Support</label>
                    <input type="string" class="form-control" v-model="client.spousalSupport" >
                </div>
                <div class="form-group">
                    <label>Worker's Compensation</label>
                    <input type="string" class="form-control" v-model="client.workersComp" >
                </div>
                <div class="form-group">
                    <label>Child Support</label>
                    <input type="string" class="form-control" v-model="client.childSupport" >
                </div>
                <div class="form-group">
                    <label>TANF</label>
                    <input type="string" class="form-control" v-model="client.TANF" >
                </div>
                <div class="form-group">
                    <label>SSI</label>
                    <input type="string" class="form-control" v-model="client.SSI" >
                </div>
                <div class="form-group">
                    <label>Unemployment</label>
                    <input type="string" class="form-control" v-model="client.unemployment" >
                </div>
                <div class="form-group">
                    <label>Social Security</label>
                    <input type="string" class="form-control" v-model="client.socialSecurity" >
                </div>
                <div class="form-group">
                    <label>Other</label>
                    <input type="string" class="form-control" v-model="client.other" >
                </div>

                <br><p>HEALTH INSURANCE INFORMATION</p>

                <div class="form-group">
                    <label>Health Insurance</label>
                    <input type="string" class="form-control" v-model="client.healthInsurance" >
                </div>
                <div class="form-group">
                    <label>Insurance Type</label>
                    <input type="string" class="form-control" v-model="client.insuranceType" >
                </div>
                <br><p>Food Stamps Section</p>
                <div class="form-group">
                    <label>Have Food Stamps</label>
                    <input type="string" class="form-control" v-model="client.haveStamps" >
                </div>
                <div class="form-group">
                    <label>Amount of Stamps</label>
                    <input type="string" class="form-control" v-model="client.stampsAmt" >
                </div>
                <div class="form-group">
                    <label>Have NO Food Stamps</label>
                    <input type="string" class="form-control" v-model="client.noStamps" >
                </div>

                <br><p>FAMILY HOUSEHOLD MEMBERS INFORMATION</p>

                <div class="form-group">
                    <label>Name</label>
                    <input type="string" class="form-control" v-model="client.name" >
                </div>
                <div class="form-group">
                    <label>Sex</label>
                    <input type="string" class="form-control" v-model="client.sex" >
                </div>
                <div class="form-group">
                    <label>DOB</label>
                    <input type="date" class="form-control" v-model="client.DOB" >
                </div>
                <div class="form-group">
                    <label>Age</label>
                    <input type="string" class="form-control" v-model="client.age" >
                </div>
                <div class="form-group">
                    <label>Relation</label>
                    <input type="string" class="form-control" v-model="client.relation" >
                </div>
                <div class="form-group">
                    <label>Race</label>
                    <input type="string" class="form-control" v-model="client.race" >
                </div>
                <div class="form-group">
                    <label>Pregnant</label>
                    <input type="string" class="form-control" v-model="client.pregnant" >
                </div>
                <div class="form-group">
                    <label>Work or Study</label>
                    <input type="string" class="form-control" v-model="client.workStudy" >
                </div>
                <div class="form-group">
                    <label>Occupation or Grade</label>
                    <input type="string" class="form-control" v-model="client.occupationGrade" >
                </div>
                <div class="form-group">
                    <label>Notes</label>
                    <input type="string" class="form-control" v-model="client.notes" >
                </div>
                
                <button class="btn btn-danger mt-3">Create</button>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'client',
        data() {
            return {
                client: {
                   familyNo: '',
                   clientNo: '',
                   startDate: '',
                   closeDate: '',

                   firstName: '',
                   lastName: '',
                   middleName: '',
                   birthDate: '',
                   socialNumber: '',
                   otherDocument: '',
                   gender: '',
                   txIDorLicense: '',

                   address: '',
                   city: '',
                   state: '',
                   zip: '',
                   county: '',
                   residencyLengthYears: '',
                   livingArrangements: '',
                   includedUtilities: '',
                   subsidizedRent: '',
                   singleParent: '',

                   homePhone: '',
                   workPhone: '',
                   cellPhone: '',
                   otherPhone: '',
                   personalEmail: '',
                   otherEmail: '',
                   maritalStatus: '',
                   language: '',
                   ethnicity: '',
                   priorityPopulation: '',
                   pregnancy: '',
                   teenParent:'',
                   deliveryDateMonths: '',

                   yearsEmployed: '',
                   employer: '',
                   occupation: '',
                   yearsUnemployed: '',
                   yearsRetired: '',
                   housewife: '',

                   attendedSchool: '',
                   nameofSchool: '',
                   lastCompletedGrade: '',
                   graduated: '',
                   levelGraduated: '',
                   certification: '',

                   headOfHousehold: '',
                   monthlyIncome: '',
                   otherIncome: '',
                   spousalSupport: '',
                   workersComp: '',
                   childSupport: '',
                   TANF: '',
                   SSI: '',
                   unemployment: '',
                   socialSecurity: '',
                   other: '',

                   healthInsurance: '',
                   insuranceType: '',
                   haveStamps: '',
                   stampsAmt:  '',
                   noStamps: '',

                   name: '',
                   sex: '',
                   DOB: '',
                   age: '',
                   relation: '',
                   race: '',
                   pregnant: '',
                   workStudy: '',
                   occupationGrade: '',
                   notes: ''
                }
            }
        },
        methods:{
        handleSubmitForm(){
            axios.post('http://localhost:3000/client', this.client) 
                 .then(() => {
    alert('Form was submitted successfully')
  })
                 
        }
    }
           
    }
</script>
