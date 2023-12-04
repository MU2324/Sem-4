var express=require('express');
var router=express.Router();

router.get('/home',function(req,res)
{
res.send("Welcome From Router Home....");
});

router.get('/login',function(req,res){
res.send("Welcome From Route Login...");
});

module.exports=router;