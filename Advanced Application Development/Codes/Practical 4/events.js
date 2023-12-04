//Import Event Module
var events=require('events');

//Create EventEmitter Object
var eventemitter=new events.EventEmitter();

//Define a Handler function to handle 'connection' event
var Handler=function connected()
{
       console.log("Connection Established");
       eventemitter.emit('download');
}

//Register download event with asynchronous function
eventemitter.on('download', function(){
      console.log("File Downloaded")
});

//Bind connection event with Handler function
eventemitter.on('connection', Handler);
eventemitter.emit('connection');
console.log("Program Terminated")

