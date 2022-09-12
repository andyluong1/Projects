const express = require("express");
const mysql = require("mysql");
const cors = require("cors");
const morgan = require("morgan");
const { connect } = require("http2");
const nodemailer = require('nodemailer')
const bcrypt = require('bcrypt')
const app = express();
const port = 3000;
app.options("*", cors());
app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

const dayjs = require("dayjs")
const advancedFormat = require("dayjs/plugin/advancedFormat")
var localizedFormat = require('dayjs/plugin/localizedFormat')
var customParseFormat = require('dayjs/plugin/customParseFormat');
const { resolveSoa } = require("dns");
const { response } = require("express");
dayjs.extend(advancedFormat)
dayjs.extend(localizedFormat)
dayjs.extend(customParseFormat)


const connection = mysql.createConnection({
    host: 'cis4375-techsoftsystemsdb.cfj7rtjvoqjp.us-east-2.rds.amazonaws.com',
    user: 'TSSDB_admin',
    password: 't3%ch#!S0*f$t051222',
    database: "SmileArchitectsDB",
    multipleStatements: true
});

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'smilearchitectsnoreply@gmail.com',
        pass: 'Tss4375cIS#1653931@uh'
    }
})

connection.connect((err) => {
    if (err) throw err;
    console.log('Connected!');
})

app.get('/login/:username/:password', (req, res) => {
    console.log(req.params)
    connection.query(`SELECT emp_first_name, emp_last_name, username, password, emp_type_id, active_emp from employees inner join system_users on employees.emp_id = system_users.emp_id
    where BINARY username = '${req.params.username}'`, (err, data) => {
        if (data.length == 1 && data[0]['active_emp'] == 1) {  
            bcrypt.compare(req.params.password, data[0].password, (error, hash1check) => {
                if (hash1check == true) {
                    res.send([true, data[0]['emp_type_id'],data[0]['emp_first_name'][0] + data[0]['emp_last_name'][0], data[0]['emp_first_name'] + ' ' + data[0]['emp_last_name']])
                }
                if (hash1check == false) {
                    res.send(false)
                }
            })
        }
        else {
            res.send(false)
        }
    })
})


// app.get('/login/:username/:password', (req, res) => {
//     console.log(req.params)
//     connection.query(`SELECT emp_first_name, emp_last_name, username, password, emp_type_id, active_emp from employees inner join system_users on employees.emp_id = system_users.emp_id
//     where BINARY username = '${req.params.username}' and BINARY password = '${req.params.password}'`, (err, data) => {
//         if (data.length == 1 && data[0]['active_emp'] == 1) {
//             res.send([true, data[0]['emp_type_id'],data[0]['emp_first_name'][0] + data[0]['emp_last_name'][0], data[0]['emp_first_name'] + ' ' + data[0]['emp_last_name']])
//         }
//         else {
//             res.send(false)
//         }
//     })
// })


app.put('/login/passwordReset', (req, res) => {
    bcrypt.hash(req.body.currentPassword, 10, (err, hash) => {
        connection.query(`SELECT * from system_users where username = '${req.body.username}'`, (err, data) => {
            if (err) {
                res.send(err)
            }
            if (data.length != 1) {
                res.send('no user found')
            }
            if (data.length == 1) {
                bcrypt.compare(req.body.currentPassword, data[0].password, (error, hash1check) => {
                    console.log(hash1check)
                    if (hash1check == true) {
                        bcrypt.hash(req.body.newPassword, 10, (err1, hash1) => {
                            connection.query(`UPDATE system_users SET password = '${hash1}' WHERE username = '${req.body.username}' AND password = '${data[0].password}' AND user_id > -1`, (error, result) => {
                                if (error) {
                                    res.send(error)
                                }
                                else {
                                    res.send('reset success')
                                }
                            })
                        })
                    }
                    if (hash1check == false) {
                        res.send('no user found')
                    }
                })
            }
        })
    })
})


// app.put('/login/passwordReset', (req, res) => {
//     connection.query(`SELECT * from system_users where username = '${req.body.username}' and password = '${req.body.currentPassword}'`, (err, data) => {
//         if (err) {
//             res.send(err)
//         }
//         if (data.length != 1) {
//             res.send('no user found')
//         }
//         if (data.length == 1) {
//             connection.query(`UPDATE system_users SET password = '${req.body.newPassword}' WHERE username = '${req.body.username}' AND password = '${req.body.currentPassword}' AND user_id > -1`, (error, result) => {
//                 if (error) {
//                     res.send(error)
//                 }
//                 else {
//                     res.send('reset success')
//                 }
//             })
//         }
//     })
// })


// employees dashboard tab endpoints

app.get('/dashboard/employees', (req, res) => {
    connection.query(`SELECT * from employees`, (err, data) => {
        for (let i = 0; i < data.length; i++) {
            if (data[i].active_emp == 1) {
                data[i].active = 'Yes'
            }
            if (data[i].active_emp == 0) {
                data[i].active = 'No'
            }
            if (data[i].emp_type_id == 1) {
                data[i].permissions = 'Administrator'
            }
            if (data[i].emp_type_id == 2) {
                data[i].permissions = 'Read-only'
            }
            if (data[i].emp_type_id == 3) {
                data[i].permissions = 'Read-write'
            }
            data[i].firstName = data[i].emp_first_name
            data[i].lastName = data[i].emp_last_name
            data[i].email = data[i].emp_email
            data[i].phoneNumber = data[i].emp_phone
        }
        res.send(data)
    })
})

app.post('/dashboard/employees', (req, res) => {
    emp_first_name = req.body.firstName.toLowerCase()
    emp_first_name = emp_first_name[0].toUpperCase() + emp_first_name.slice(1)
    emp_last_name = req.body.lastName.toLowerCase()
    emp_last_name = emp_last_name[0].toUpperCase() + emp_last_name.slice(1)
    emp_email = req.body.email.toLowerCase()
    emp_phone = req.body.phoneNumber
    emp_type_id = req.body.permissions
    username = req.body.username
    password = req.body.password
    connection.query(
        `SELECT * from employees where emp_email = '${emp_email}'; 
         SELECT * from system_users where BINARY username = '${username}';
         SELECT * from employees where emp_phone = '${emp_phone}'`, (err, data) => {
        console.log(data)
        if (data[0].length >= 1 && data[1].length >= 1 && data[2].length == 0) {
            res.send('email and username already exist.')
        }
        if (data[0].length >= 1 && data[2].length >= 1 && data[1].length == 0) {
            res.send('email and phone number already exist.')
        }
        if (data[1].length >= 1 && data[2].length >= 1 && data[0].length == 0) {
            res.send('username and phone number already exist.')
        }
        if (data[0].length >= 1 && data[1].length == 0 && data[2].length == 0) {
            res.send('email already exists.')
        }
        if (data[1].length >= 1 && data[2].length == 0 && data[0].length == 0) {
            res.send('username already exists.')
        }
        if (data[2].length >= 1 && data[1].length == 0 && data[0].length == 0) {
            res.send('phone number already exists.')
        }
        if (data[0].length >= 1 && data[1].length >= 1 && data[2].length >= 1) {
            res.send('email, phone number, and username already exist.')
        }
        if (data[0].length == 0 && data[1].length == 0 && data[2].length == 0) {
            connection.query(`INSERT INTO employees (emp_first_name, emp_last_name, emp_email, emp_phone, emp_type_id, active_emp)
            values ('${emp_first_name}','${emp_last_name}','${emp_email}','${emp_phone}',${emp_type_id}, 1)`, (err, result) => {
                if (err) {
                    res.send('Error occured. Please try again.')
                }
                else {
                    bcrypt.hash(password, 10, (err, hash) => {
                        connection.query(`INSERT INTO system_users (username, password, emp_id) values ('${username}','${hash}', ${result.insertId})`, (err, result) => {
                            if (err) {
                                res.send('Error occured. Please try again.')
                            }
                            else {
                                res.send('Successfully added.')
                            }
                        })
                    })
                }      
            })
        }
    })
})

app.put('/dashboard/employees', (req, res) => {
    connection.query(`UPDATE employees SET emp_first_name = '${req.body.emp_first_name}', emp_last_name = '${req.body.emp_last_name}', emp_email = '${req.body.emp_email}',
    emp_phone = '${req.body.emp_phone}', emp_type_id = ${req.body.emp_type_id}, active_emp = ${req.body.emp_active} 
    WHERE emp_email = '${req.body.current_employee_email}';`, (err, result) => {
        if (err) {
            res.send('update failed')
        }
        else {
            res.send(['update successful', req.body.emp_email])
        }
    })
})

app.delete('/dashboard/employees/:email/:phoneNumber', (req, res) => {
    connection.query(`DELETE from employees WHERE emp_email = '${req.params.email}' AND emp_phone = '${req.params.phoneNumber}';`, (err, result) => {
        if (err) {
            res.send('Not deleted')
        }
        else {
            res.send('Deleted')
        }
    })
})


// Schedule dashboard endpoints

app.get('/dashboard/scheduleByWeek/:selectedWeekStart/:selectedWeekEnd', (req, res) => {
    connection.query(`SELECT * from appointments WHERE appt_date BETWEEN '${req.params.selectedWeekStart}' AND '${req.params.selectedWeekEnd}';`, (err, result) => {
        if (err) {
            res.send('Error')
        }
        else {
            res.send(result)
        }
    })
})

app.post('/dashboard/scheduleByWeek/addAppointment', (req, res) => {
    let weekStart = dayjs(req.body[1]).day(1).format('YYYY-MM-DD')
    let weekEnd = dayjs(req.body[1]).day(6).format('YYYY-MM-DD')
    connection.query(`SELECT * from appointments WHERE appt_date BETWEEN '${weekStart}' AND '${weekEnd}'`, (err, data) => {
        if (data.length == 0) {
            connection.query(`INSERT INTO appointments (appt_time, appt_date, isVisible) values ('${req.body[0]}', '${req.body[1]}', 0)`, (err, result) => {
                if (err) {
                    res.send('Error')
                }
                else {
                    res.send('appointment added')
                }
            })
        }
        if (data.length >= 1 && data[0].isVisible == 0) {
            connection.query(`INSERT INTO appointments (appt_time, appt_date, isVisible) values ('${req.body[0]}', '${req.body[1]}', 0)`, (err, result) => {
                if (err) {
                    res.send('Error')
                }
                else {
                    res.send('appointment added')
                }
            })
        }
        if (data.length >= 1 && data[0].isVisible == 1) {
            connection.query(`INSERT INTO appointments (appt_time, appt_date, isVisible) values ('${req.body[0]}', '${req.body[1]}', 1)`, (err, result) => {
                if (err) {
                    res.send('Error')
                }
                else {
                    res.send('appointment added')
                }
            })
        }
    })
})

app.post('/dashboard/scheduleByWeek/copyDay', (req, res) => {
    let weekStart = dayjs(req.body[0]).day(1).format('YYYY-MM-DD')
    let weekEnd = dayjs(req.body[0]).day(6).format('YYYY-MM-DD')
    connection.query(`SELECT * from appointments WHERE appt_date BETWEEN '${weekStart}' AND '${weekEnd}'`, (err, data) => {
        if (data.length == 0) {
            let bulkInsert = ''
            for (let i = 0; i < req.body[1].length; i++) {
                bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${req.body[1][i].appt_time}', '${req.body[0]}', 0); `
            }
            connection.query(bulkInsert, (err, result) => {
                if (err) {
                    res.send('Error')
                }
                else {
                    res.send('appointment added')
                }
            })
        }
        if (data.length >= 1 && data[0].isVisible == 0) {
            let bulkInsert = ''
            for (let i = 0; i < req.body[1].length; i++) {
                bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${req.body[1][i].appt_time}', '${req.body[0]}', 0); `
            }
            connection.query(bulkInsert, (err, result) => {
                if (err) {
                    res.send('Error')
                }
                else {
                    res.send('appointment added')
                }
            })
        }
        if (data.length >= 1 && data[0].isVisible == 1) {
            let bulkInsert = ''
            for (let i = 0; i < req.body[1].length; i++) {
                bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${req.body[1][i].appt_time}', '${req.body[0]}', 1); `
            }
            connection.query(bulkInsert, (err, result) => {
                if (err) {
                    res.send('Error')
                }
                else {
                    res.send('appointment added')
                }
            })
        }
    })
})

app.post('/dashboard/scheduleByWeek/copyWeek', (req, res) => {
    let weekStart = dayjs(req.body[2]).day(1).format('YYYY-MM-DD')
    let weekEnd = dayjs(req.body[3]).day(6).format('YYYY-MM-DD')
    connection.query(`SELECT * from appointments WHERE appt_date BETWEEN '${weekStart}' AND '${weekEnd}'`, (err, data) => {
        if (data.length == 0) {
            connection.query(`SELECT * from appointments where appt_date BETWEEN '${req.body[0]}' AND '${req.body[1]}';`, (err, results) => {
                let bulkInsert = ''
                for (let i = 0; i < results.length; i++) {
                    if (dayjs(results[i].appt_date).format('dddd') == 'Monday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(1).format('YYYY-MM-DD')}', 0); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Tuesday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(2).format('YYYY-MM-DD')}', 0); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Thursday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(4).format('YYYY-MM-DD')}', 0); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Friday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(5).format('YYYY-MM-DD')}', 0); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Saturday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(6).format('YYYY-MM-DD')}', 0); `
                    }
                }
                connection.query(bulkInsert, (err, result) => {
                    if (err) {
                        res.send('Error')
                    }
                    else {
                        res.send('appointments added')
                    }
                })
            })
        }
        if (data.length >= 1 && data[0].isVisible == 0) {
            connection.query(`SELECT * from appointments where appt_date BETWEEN '${req.body[0]}' AND '${req.body[1]}';`, (err, results) => {
                let bulkInsert = ''
                for (let i = 0; i < results.length; i++) {
                    if (dayjs(results[i].appt_date).format('dddd') == 'Monday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(1).format('YYYY-MM-DD')}', 0); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Tuesday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(2).format('YYYY-MM-DD')}', 0); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Thursday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(4).format('YYYY-MM-DD')}', 0); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Friday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(5).format('YYYY-MM-DD')}', 0); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Saturday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(6).format('YYYY-MM-DD')}', 0); `
                    }
                }
                connection.query(bulkInsert, (err, result) => {
                    if (err) {
                        res.send('Error')
                    }
                    else {
                        res.send('appointments added')
                    }
                })
            })
        }
        if (data.length >= 1 && data[0].isVisible == 1) {
            connection.query(`SELECT * from appointments where appt_date BETWEEN '${req.body[0]}' AND '${req.body[1]}';`, (err, results) => {
                let bulkInsert = ''
                for (let i = 0; i < results.length; i++) {
                    if (dayjs(results[i].appt_date).format('dddd') == 'Monday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(1).format('YYYY-MM-DD')}', 1); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Tuesday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(2).format('YYYY-MM-DD')}', 1); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Thursday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(4).format('YYYY-MM-DD')}', 1); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Friday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(5).format('YYYY-MM-DD')}', 1); `
                    }
                    if (dayjs(results[i].appt_date).format('dddd') == 'Saturday') {
                        bulkInsert = bulkInsert + `INSERT IGNORE INTO appointments (appt_time, appt_date, isVisible) values ('${results[i].appt_time}', '${dayjs(req.body[2]).day(6).format('YYYY-MM-DD')}', 1); `
                    }
                }
                connection.query(bulkInsert, (err, result) => {
                    if (err) {
                        res.send('Error')
                    }
                    else {
                        res.send('appointments added')
                    }
                })
            })
        }
    })
    
})

app.delete('/dashboard/scheduleByWeek/deleteAppointment/:appt_time/:appt_date', (req, res) => {
    connection.query(`DELETE from appointments WHERE appt_time = '${req.params.appt_time}' AND appt_date = '${req.params.appt_date}' AND sign_up_id is NULL;`, (err, result) => {
        if (err) {
            res.send('Not deleted')
        }
        else {
            res.send('Deleted')
        }
    })
})

app.delete('/dashboard/scheduleByWeek/deleteDayAppointments/:appt_date', (req, res) => {
    connection.query(`DELETE from appointments WHERE appt_date = '${req.params.appt_date}' AND sign_up_id is NULL;`, (err, result) => {
        if (err) {
            res.send('Not deleted')
        }
        else {
            res.send('Deleted')
        }
    })
})

app.get('/dashboard/scheduleByDay/:selectedDay', (req, res) => {
    connection.query(`SELECT a.*, b.* from appointments as a LEFT JOIN appt_sign_up_forms as b ON a.sign_up_id = b.sign_up_id WHERE a.appt_date = '${req.params.selectedDay}';`, (err, result) => {
        if (err) {
            res.send('Error')
        }
        else {
            res.send(result)
        }
    })
})

app.get('/dashboard/scheduleByWeek/checkVisibility/:selectedWeekStart/:selectedWeekEnd', (req, res) => {
    connection.query(`SELECT * from appointments WHERE appt_date BETWEEN '${req.params.selectedWeekStart}' AND '${req.params.selectedWeekEnd}';`, (err, result) => {
        if (err) {
            res.send('Error')
        }
        else {
            if (result.length >= 1) {
                if (result[0].isVisible == 0){
                    res.send('not visible')
                }
                if (result[0].isVisible == 1) {
                    res.send('visible')
                }
            }
            if (result.length == 0) {
                res.send('not visible')
            }
        }
    })
})

app.put('/dashboard/scheduleByWeek/setVisibility', (req, res) => {
    console.log(req.body)
    if (req.body[2] == 0) {
        connection.query(`UPDATE appointments SET isVisible = '${req.body[2]}' WHERE appt_date BETWEEN '${req.body[0]}' AND '${req.body[1]}' AND appt_id > -1;`, (err, result) => {
            if (err) {
                res.send('visible')
            }
            else {
                res.send('not visible')
            }
        })
    }
    if (req.body[2] == 1) {
        connection.query(`UPDATE appointments SET isVisible = '${req.body[2]}' WHERE appt_date BETWEEN '${req.body[0]}' AND '${req.body[1]}' AND appt_id > -1;`, (err, result) => {
            if (err) {
                res.send('not visible')
            }
            else {
                res.send('visible')
            }
        })
    }    
})

app.put('/dashboard/scheduleByDay/cancelAppointment', (req, res) => {
    connection.query(`UPDATE appointments SET sign_up_id = NULL WHERE appt_id = ${req.body[0]};`, (err, result) => {
        if (err) {
            res.send('appointment cancel failed')
        }
        else {
            res.send('canceled appointment')
        }
    })
})

// book appointment endpoints


app.get('/bookAppointment/:selectedDay', (req, res) => {
    connection.query(`SELECT * from appointments WHERE appt_date = '${req.params.selectedDay}' AND sign_up_id is NULL AND isVisible = 1`, (err, result) => {
        if (err) {
            res.send('Error')
        }
        else {
            res.send(result)
        }
    })
})


app.post('/bookAppointment', (req, res) => {
    connection.query(`INSERT INTO appt_sign_up_forms (patient_first_name, patient_last_name, patient_dob, patient_email, patient_phone, patient_zip, insurance_name, group_number, member_id, ph_first_name, ph_last_name, ph_dob, service) values (
    '${req.body.patient_first_name}', '${req.body.patient_last_name}', '${req.body.patient_dob}', '${req.body.patient_email}', '${req.body.patient_phone}', '${req.body.patient_zip}', '${req.body.insurance_name}', '${req.body.group_number}', '${req.body.member_id}', '${req.body.ph_first_name}', '${req.body.ph_last_name}', '${req.body.ph_dob}', '${req.body.service}');`, (err, result) => {
        if (err) {
            res.send('Error')
        }
        else {
            connection.query(`UPDATE appointments SET sign_up_id = ${result.insertId} WHERE appt_date = '${req.body.appt_date}' AND appt_time = '${req.body.appt_time}' AND appt_id > -1;`, (err, data) => {
                if (err) {
                    res.send('Error')
                }
                else {
                    let mailOptions = {
                        from: 'smilearchitectsnoreply@gmail.com',
                        to: req.body.patient_email,
                        subject: 'Appointment Confirmation: Smile Architects of Houston',
                        text: `Thank you for choosing Smile Architects of Houston. Your appointment is scheduled for ${dayjs('1/1/1 ' + req.body.appt_time).format('h:mm a')} on ${dayjs(req.body.appt_date).format('dddd MMMM Do')}. If you wish to cancel this appointment, please contact our office.`
                    }
                    transporter.sendMail(mailOptions, (error, info) => {
                        if (error) {
                            console.log(error)
                        }
                        else {
                            res.send('success')
                        }
                    })
                }
            })
        }
    })
})


// analytics endpoints

app.get('/dashboard/analytics/BarChart', (req, res) => {
    let yesterday = dayjs().add(-1, 'day').format('YYYY-MM-DD')
    let lastMonth = dayjs().add(-31, 'day').format('YYYY-MM-DD')
    connection.query(`SELECT (appt_date) from appointments where sign_up_id is not NULL AND appt_date BETWEEN '${lastMonth}' AND '${yesterday}';`, (err, result) => {
        if (err) {
            console.log(err)
        }
        else {
            if (result.length != 0) {
                for (let i = 0; i < result.length; i++) {
                    result[i].appt_date = dayjs(result[i].appt_date).format('dddd')
                }
                let data = {
                    labels: ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday'],
                    datasets: [ { data: [0, 0, 0, 0, 0] } ]
                }
                for (let i = 0; i < result.length; i++) {
                    if (result[i].appt_date == 'Monday') {
                        data.datasets[0].data[0] += 1
                    }
                    if (result[i].appt_date == 'Tuesday') {
                        data.datasets[0].data[1] += 1
                    }
                    if (result[i].appt_date == 'Thursday') {
                        data.datasets[0].data[2] += 1
                    }
                    if (result[i].appt_date == 'Friday') {
                        data.datasets[0].data[3] += 1
                    }
                    if (result[i].appt_date == 'Saturday') {
                        data.datasets[0].data[4] += 1
                    }
                }
                res.send(data)
            }
            if (result.length == 0) {
                let data = {
                    monday: 0,
                    tuesday: 0,
                    thursday: 0,
                    friday: 0,
                    saturday: 0
                }
                res.send(data)
            }
        }
    })
})


app.get('/dashboard/analytics/DoughnutChart', (req, res) => {
    let yesterday = dayjs().add(-1, 'day').format('YYYY-MM-DD')
    let lastMonth = dayjs().add(-31, 'day').format('YYYY-MM-DD')
    connection.query(`SELECT (service) from appt_sign_up_forms INNER JOIN appointments ON appt_sign_up_forms.sign_up_id = appointments.sign_up_id WHERE appt_date BETWEEN '${lastMonth}' AND '${yesterday}';`, (err, result) => {
        if (err) {
            console.log(err)
        }
        else {
            let data = {
                examination: 0,
                restoration: 0,
                implants: 0,
                prosthesis: 0,
                oralHygiene: 0,
                periodontics: 0,
                endodontics: 0,
                oralSurgery: 0,
                bondingAndMinorRestoration: 0,
                adjunctiveProcedures: 0,
                whitening: 0,
                orthodontics: 0,
                other: 0
            }
            if (result.length == 0) {
                data = {
                    labels: ['services'],
                    datasets: [ { data: [0] } ]
                }
                res.send(data)
            }
            if (result.length != 0) {
                for (let i = 0; i < result.length; i++) {
                    if (result[i].service == 'Examination') {
                        data.examination += 1
                    }
                    if (result[i].service == 'Restoration') {
                        data.restoration += 1
                    }
                    if (result[i].service == 'Implant(s)') {
                        data.implants += 1
                    }
                    if (result[i].service == 'Prosthesis') {
                        data.prosthesis += 1
                    }
                    if (result[i].service == 'Oral Hygiene') {
                        data.oralHygiene += 1
                    }
                    if (result[i].service == 'Periodontics') {
                        data.periodontics += 1
                    }
                    if (result[i].service == 'Endodontics') {
                        data.endodontics += 1
                    }
                    if (result[i].service == 'Oral Surgery') {
                        data.oralSurgery += 1
                    }
                    if (result[i].service == 'Bonding and Minor Restoration') {
                        data.bondingAndMinorRestoration += 1
                    }
                    if (result[i].service == 'Adjunctive Procedures') {
                        data.adjunctiveProcedures += 1
                    }
                    if (result[i].service == 'Whitening') {
                        data.whitening += 1
                    }
                    if (result[i].service == 'Orthodontics') {
                        data.orthodontics += 1
                    }
                    if (result[i].service == 'Other') {
                        data.other += 1
                    }
                }
                sortingArray = []
                for (service in data) { 
                    sortingArray.push(service + ' ' + data[service])
                }
                sortingArray.sort((a, b) => parseInt(a.split(" ")[1]) < parseInt(b.split(" ")[1]) ? 1 : - 1)
                data = {
                    labels: [],
                    datasets: [ { data: [] } ]
                }
                for (let i = 0; i < 5; i++) {
                    if (sortingArray.length > 0) {
                        temp = sortingArray[0].split(" ")
                        data.labels.push((temp[0].replace(/([a-z])([A-Z])/g, '$1 $2')).toLowerCase())
                        data.datasets[0].data.push(parseInt(temp[1])) 
                        sortingArray.shift()
                    }
                }
                res.send(data)
            }
        }
    })
})


app.get('/dashboard/analytics/PieChart', (req, res) => {
    let yesterday = dayjs().add(-1, 'day').format('YYYY-MM-DD')
    let lastMonth = dayjs().add(-31, 'day').format('YYYY-MM-DD')
    connection.query(`SELECT (patient_zip) from appt_sign_up_forms INNER JOIN appointments ON appt_sign_up_forms.sign_up_id = appointments.sign_up_id WHERE appt_date BETWEEN '${lastMonth}' AND '${yesterday}';`, (err, result) => {
        if (err) {
            console.log(err)
        }
        else {
            if (result.length == 0) {
                distribution = {
                    labels: [],
                    datasets: [ { data: [] } ]
                }
                res.send(distribution)
            }
            if (result.length != 0) {
                let data = []
                let distribution = {}
                for (let i = 0; i < result.length; i++) {
                    key = result[i].patient_zip
                    if (key in distribution) {
                        distribution[key] += 1
                    }
                    else {
                        distribution[key] = 1
                    }
                }
                for (zip in distribution) { 
                    data.push(zip + ' ' + distribution[zip])
                }
                count = 0
                data.sort((a, b) => parseInt(a.slice(5)) < parseInt(b.slice(5)) ? 1 : - 1)
                distribution = {
                    labels: [],
                    datasets: [ { data: [] } ]
                }
                for (let i = 0; i < 5; i++) {
                    if (data.length > 0) {
                        distribution.labels.push(data[0].slice(0, 5))
                        distribution.datasets[0].data.push(parseInt(data[0].slice(5))) 
                        data.shift()
                    }
                }
                res.send(distribution)
            }
            
        }
    })
})

app.get('/dashboard/analytics/appointmentHistory/:start/:end', (req, res) => {
    connection.query(`SELECT appt_date, appt_time, service, patient_phone, patient_email, patient_zip, patient_first_name, patient_last_name from appt_sign_up_forms INNER JOIN appointments ON appt_sign_up_forms.sign_up_id = appointments.sign_up_id WHERE appt_date BETWEEN '${req.params.start}' AND '${req.params.end}';`, (err, result) => {
        if (err) {
            console.log(err)
        }
        else {
            res.send(result)
        }
    })
})

app.listen(port, () => {
    console.log("Server started listening on port: ", port);
  });
