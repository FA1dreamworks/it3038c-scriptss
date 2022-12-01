const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    myServerUp=os.uptime();
    myTotalMem=os.totalmem()/10000000 + " MB";
    myFreeMem=os.freemem()/10000000 + " MB";
    myCPU=os.cpus().length;
    numDay=(os.uptime(24 *3600)) + " Days,";
    numHr= ((os.uptime %(24 *3600)/3600)) +" Hours,";
    numMin= ((os.uptime % (24 *3600 * 3600))/60) +" Mins,";
    numSec= ((os.uptime % (24 * 3600 *3600 *60))/60) +" Sec";
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${Math.round(os.uptime()/86400) + " Days, " + Math.round(os.uptime()* 24) + " Hours, " + Math.round(os.uptime(5184000)) + " Minutes, " + Math.round(os.uptime((24 * 3600 *3600 *60)/60)) + " Seconds."} </p>
        <p>Total Memory: ${myTotalMem} </p>
        <p>Free Memory: ${myFreeMem} </p>
        <p>Number of CPUs: ${myCPU} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");