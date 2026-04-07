const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const db = require('./db');

const app = express();
app.use(express.json())

app.use(bodyParser.urlencoded({ extended: false }));

app.use(session({
    secret: 'secret-key',
    resave: false,
    saveUninitialized: true
}));
app.use(express.static('views'));

app.post('/search', (req, res) => {
    const query = req.body.query;
    const sql = `SELECT username, email FROM users WHERE username LIKE '%${query}%'`;

    if (query = "") {
        return [];
    } 
    db.all(sql, (err, rows) => {
        if (err) {
            return res.send({"error" : `Database error: + ${err.message}`});
        }
        console.log(rows);
        res.json(rows);
    });
});

app.get('/admin', (req, res) => {
    res.sendFile(__dirname + '/views/admin.html');
});

app.post('/admin', (req, res) => {
    console.log("Request: ", req.body)
    const { user, password } = req.body;

    if (user === 'flag' && password === 'dmVyeV93ZWFrX3Bhc3N3ZAo=') {
        return res.send({message: 'Congrats! Here is your flag: b24be7019235141704e656ad29c9c8013237708d'});
    }

    res.send({message: 'Invalid credentials'});
});

app.listen(3001, () => {
    console.log('[Server] Running on port 3001');
});