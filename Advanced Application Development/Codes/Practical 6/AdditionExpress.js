var express=require('express');
var app=express();

app.get('/addition',function(req,res){
               var num1=parseInt(req.query.number1);
               var num2=parseInt(req.query.number2);
               res.send("addition= "+(num1+num2));
});

app.listen(3030);
console.log("server started")
