const fs = require('fs')
const http = require('http')

const server = http.createServer()
server.on("request", handler)
server.listen(8080)

function handler(req, res)
{
	fs.readFile("./file.html",
		function(err, data)
		{
			if(err){
				res.writeHead(500)
				res.write(err.message)
				res.end()
			}
			else{
				res.writeHead(200, {"Content-Type":"text/html"})
				res.write(data)
				res.end()
			}
		})
}
