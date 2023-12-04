var file=require("fs");
/*
var data=file.readFileSync('simple.txt');
console.log(data.toString());
console.log("Program ended");
*/
file.readFile('simple.txt', function(err,data){
      if(err) return console.error(err);
      console.log(data.toString());
});
console.log("Program Ended")
