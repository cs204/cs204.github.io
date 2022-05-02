const http = require("http")
const server = http.createServer()

server.on('request', requestHandler)
server.listen(8080)

function requestHandler(req, res)
	{
		if( req.url == "/")
		{
			res.writeHead(200, {"Content-Type":"text/plain"})
			res.write("Hello, World!")
			res.end()
		}
		else if( req.url == "/api")
		{
			res.writeHead(200, {"Constent-Type": "application/json"})
			let person = {name: "Bob", age: 18}
			res.write(JSON.stringify(person))
			res.end()
		}
		else
		{
			res.writeHead(400)
			res.end("Page not found")
		}
	}

