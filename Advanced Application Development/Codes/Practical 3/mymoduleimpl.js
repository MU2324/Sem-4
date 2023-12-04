var http=require('http')
var md=require('./mymodule');

http.createServer(function(req,res){
     res.writeHead(200,{'Content-Type':'text/html'});
     res.write("Current Date and Time is "+md.mydate());
     res.write(" Message returned is "+md.message());
}).listen(8040);