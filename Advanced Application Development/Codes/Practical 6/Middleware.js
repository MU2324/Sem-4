var express=require('express');
var app=express();

app.get('/',function(req,res,ne){
res.send("Working with express Middleware");
ne(logout());
});

function logout(req,res){
console.log("LOGOUT");
}

app.listen(3030);
console.log("Server Started...")
