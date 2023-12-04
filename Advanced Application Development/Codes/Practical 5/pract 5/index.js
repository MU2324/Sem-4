var express=require('express');
var app=express();

app.get('/',function(req,res){
        res.send("Welcome to express framework");
});

app.listen(3030);
console.log("Express server is started and it is waiting for client connections on port no. 3030");