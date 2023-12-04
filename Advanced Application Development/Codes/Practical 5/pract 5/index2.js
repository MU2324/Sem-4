var express=require('express');
var app=express();

app.get('/home/:name/:id',function(req,res){
      res.send("User name is "+req.params.name+" and id is "+req.params.id);
})

app.listen(3030);
console.log("Express server is started...");