var express=require('express');
var app=express();

app.get('/home',function(req,res){
      res.send("Welcome from route home...");
})

app.get('/login',function(req,res){
      res.send("Welcome from route login...");
})

app.listen(3030);
console.log("Express server is started...");