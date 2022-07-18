const uuid = require('uuid');
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//New clients being placed into programs
let programSchema = new Schema({
    _id: { type: String, default: uuid.v1 },
    activity: { type: String },
    startDate: { type: Date },
    closeDate: { type: Date },
    servicesUsed: { type: String },
    clientNo: { type: Number }
},{
    collection: 'program'
});

module.exports = mongoose.model('program', programSchema)