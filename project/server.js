const express = require('express');
const cors = require('cors');
const app = express();
const connection = require('./config/connection');
const logger = require('morgan');
const axios = require('axios');
app.use(cors());
app.use(express.json());
app.use(logger("dev"))

const session=require("express-session");


app.use(session({
  secret: 'fixedbugs2',
  cookie: { maxAge: 60000 }
}));


app.post("/", (req, res) => {
  const { email, password } = req.body;
  console.log(email,password);
  connection.query(
      "SELECT * from users  where users.email = ? and users.password = ?", [email, password],
      function(error, results) {
          if (error) console.log(error);
          if (results[0]) {
              const success = true;
              req.session.email = results[0].email;
              res.status(200).json({ success});
          } else {
              const success = false;
              res.status(404).json({ success });
          }
          console.log(results);
      }
  );
});

app.post('/control', (req, res)=>{
  if(req.session.email){
   res.status(200).json({success:true})
  }
})

app.post('/nodepredict', (req, res)=>{
  console.log(req.body.predict)
  axios.post('http://localhost:5000/predict', {predict: req.body.predict}).then(data=>{
    res.send(data.data)
    console.log(data)
  }).catch(err=>{
    console.log(err)
  })
})


app.post('/register', (req, res) => {
  const { name, surname, password,email,role } = req.body;
  console.log(req.body)
  const sql = "insert into users(name, surname,email ,password, role)values(?,?,?,?,?)";
  connection.query(
      sql, [name, surname, email, password, role],
      (err, result) => {
          if (err) {
              const success = false;
              res.status(503).json({ success, err });
          } else {
              const success = true;
              res.status(200).json({ success });
          }
      }
  )
})

app.listen(4500, () => { console.log("server is up and runing") })