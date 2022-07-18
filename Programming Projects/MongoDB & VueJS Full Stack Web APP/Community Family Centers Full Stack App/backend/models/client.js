const uuid = require('uuid');
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//Client schema made from Intake Form
let clientSchema = new Schema({
    _id: { type: String, default: uuid.v1 },
    familyNo: { type: Number },
    clientNo: { type: Number },
    startDate: {type: Date },
    closeDate: {type: Date },

    firstName: { type: String, required: true },
    lastName: { type: String, required: true },
    middleName: { type: String },
    birthDate: { type: Date, required: true },
    socialNumber: { type: String, required: true },
    otherDocument: { type: String },
    gender: { type: String },
    txIDorLicense: { type: Number, required: true },

    address: { type: String },
    city: { type: String },
    state: { type: String },
    zip: { type: Number },
    county: { type: String },
    residencyLengthYears: { type: Number },
    livingArrangements: { type: String },
    includedUtilities: { type: String },
    subsidizedRent: { type: String },
    singleParent: { type: String },
    
    homePhone: { type: String },
    workPhone: { type: String },
    cellPhone: { type: String },
    otherPhone: { type: String },
    personalEmail: { type: String },
    otherEmail: { type: String },
    maritalStatus: { type: String },
    language: { type: String },
    ethnicity: { type: String },
    priorityPopulation: { type: String },
    pregnancy: { type: String },
    teenParent: { type: String },
    deliveryDateMonths: { type: String },


    yearsEmployed: { type: Number },
    employer: { type: String },
    occupation: { type: String },
    yearsUnemployed: { type: Number },
    yearsRetired: { type: Number },
    housewife: { type: String },

    attendedSchool: { type: String },
    nameofSchool: { type: String },
    lastCompletedGrade: { type: String },
    graduated: { type: String },
    levelGraduated: { type: String },
    certification: { type: String },


    headOfHousehold: { type: String },
    monthlyIncome: { type: String },
    otherIncome: { type: String },
    spousalSupport: { type: String },
    workersComp: { type: String },
    childSupport: { type: String },
    TANF: { type: String },
    SSI: { type: String },
    unemployment: { type: String },
    socialSecurity: { type: String },
    other: { type: String },

    healthInsurance: { type: String },
    insuranceType: { type: String },
    foodStamps: {
        haveStamps: { type: String },
        stampsAmt:  { type: Number },
        noStamps: { type: String }
    
    },
 
    name: { type: String },
    sex: { type: String },
    DOB: { type: Date },
    age: { type: String },
    relation: { type: String },
    race: { type: String },
    pregnant: { type: String },
    workStudy: { type: String },
    occupationGrade: { type: String },
    notes: { type: String },


},{
    collection: 'client'
});

module.exports = mongoose.model('client', clientSchema)