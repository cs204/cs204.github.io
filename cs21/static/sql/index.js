import express from "express";
import bodyParser from "body-parser"
import {controlGradebook} from "./gradebook.js"

const app = express();
app.use(bodyParser.urlencoded({ extendes: true}));
app.use(express.static('public'));

app.get("/", (req, res)=>
	{
		res.render("index.ejs");
	}
)

app.post("/gradebook", controlGradebook);

const port = process.env.PORT || 8080;
app.listen(port, ()=>console.log(`Listen port: ${port}`));


