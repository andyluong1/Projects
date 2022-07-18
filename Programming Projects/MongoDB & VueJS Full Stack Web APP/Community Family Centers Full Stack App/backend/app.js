//This app starts a server and listens on port 3000 for connections
const express = require('express');
const mongoose = require("mongoose"); 
const app = express(); 
const port = 3000;
const cors = require('cors');
const morgan = require("morgan");

//const { MongoClient } = require('mongodb');

// Connection URL
const url = 'mongodb://localhost:27017/CFCDatabase';

// Database Name
//const dbName = 'CFCDatabase';

app.use(cors());
app.use(express.json()); //allows us to access request body as req.body
app.use(morgan("dev"));  //enable incoming request logging in dev mode

require('dotenv').config();


//import client and program model schema from folder 'models'
let ClientModel = require('./models/client');
let ProgramModel = require('./models/program');


//mongoose connection
mongoose
    .connect(url)   // read environment varibale from .env
    .then(() => {
        console.log("Database connection Success!");
    })
    .catch((err) => {
        console.error("Mongo Connection Error", err);
    });
app.use(express.json());

app.listen(port, () => {
  console.log(`CFC app listening at http://localhost:${port}`)
});


// == CRUD functions for IntakeForm also known as Clients ==
// NOTE: Rempved res.send because the response was sent multiple times instead of just once
// CREATE
app.post('/client', (req, res, next) => {
    ClientModel.create(req.body, (error, data) => {
        if (error) {
          return next(error)
        } else {
          res.json(data)
          //res.send('Client is added to the database');
        }
    });
});

// RETRIEVE - endpoint for clients to gather info from from api
app.get('/client', (req, res, next) => {
    ClientModel.find((error, data) => {
        if (error) {
          return next(error)
        } else {
          return res.json(data)
          //res.send('Client infomation is retrieved');
        }
      })
});

app.get('/client/:id', (req, res, next) => {
    ClientModel.findOne({ _id: req.params.id}, (error, data) => {
        if (error) {
            return next(error)
        } else if (data === null) {
        
          res.status(404).send('Client not found');
        }
        else {
          res.json(data)
        }
    });
});

//null is used to remove "options: mongoose.QueryOptions"
// UPDATE
app.put('/client/:id', (req, res, next) => {
    ClientModel.findOneAndUpdate({ _id: req.params.id }, {
        $set: req.body
      }, null, (error, data) => {
        if (error) {
          return next(error);
        } else {
          res.send('Client has been edited');
          console.log('Client successfully updated!', data)
        }
      })
});


// DELETE
app.delete('/client/:id', (req, res, next) => {
    ClientModel.findOneAndRemove({ _id: req.params.id}, null, (error, data) => {
        if (error) {
          return next(error);
        } else {
           res.status(200).json({
             msg: data
           });
        // return res.send('Client is deleted');
        }
      });
});


// == CRUD functions for Programs ==
// CREATE
app.post('/program', (req, res, next) => {
    ProgramModel.create(req.body, (error, data) => {
        if (error) {
          return next(error)
        } else {
          return res.json(data)
          // return res.send('Program is added to the database');
        }
    });
});

// RETRIEVE - endpoint for programs to gather info from api
app.get('/program', (req, res, next) => {
    ProgramModel.find((error, data) => {
        if (error) {
          return next(error)
        } else {
          return res.json(data)
          // res.send('Program infomation is retrieved');
        }
      })
});

app.get('/program/:id', (req, res, next) => {
   ProgramModel.findOne({ _id: req.params.id}, (error, data) => {
        if (error) {
            return next(error)
        } else if (data === null) {
        
          res.status(404).send('Program not found');
        }
        else {
          res.json(data)
        }
    });
});

// UPDATE
app.put('/program/:id', (req, res, next) => {
    ProgramModel.findOneAndUpdate({ _id: req.params.id }, {
        $set: req.body
      }, null, (error, data) => {
        if (error) {
          return next(error);
        } else {
          res.send('Program has been edited');
          console.log('Program successfully updated!', data)
        }
      })
});


// DELETE
app.delete('/program/:id', (req, res, next) => {
    ProgramModel.findOneAndRemove({ _id: req.params.id}, null, (error, data) => {
        if (error) {
          return next(error);
        } else {
           res.status(200).json({
             msg: data
           });
        // return res.send('Program is deleted');
        }
      });
});


// Aggregate Function
// The program information is linked with an client number from client information
// Get activity starting with date/time and client with clientNo
app.get('/program', (req, res, next) => {

  ClientModel.aggregate([
    { $match : { clientNo : req.params.id } },
    { $project : { clientNo : 1, firstName : 1, lastName : 1, programbyClient : 1 } },
    { $lookup : {
        from : 'program',
        localField : 'clientNo',
        foreignField : 'clientNo',
        as : 'programbyClient'
    } }
  ], (error, data) => {
      if (error) {
        return next(error)
      } else {
        res.json(data);
      }
  });
});

// eslint-disable-next-line no-unused-vars
app.use(function (err, req, res, next) {
  console.error(err.message);
  if (!err.statusCode) 
      err.statusCode = 500;
  res.status(err.statusCode).send(err.message);
});