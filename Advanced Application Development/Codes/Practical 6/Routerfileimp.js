var express=require('express');
var app=express();
var router=require('./Routerfile.js');

app.use('/',router);
app.listen(3030);
console.log("Server Stared...");