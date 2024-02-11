import express from 'express'
import bodyParser from 'body-parser'
const app = express()
const port = process.env.PORT || 8080 

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
      res.render('index.ejs')
});

app.post('/', (req, res) =>
    {
        const username = req.body.username;
        res.render('hello.ejs', {username: username});
    });

app.listen(port, () => {
      console.log(`Example app listening on port ${port}`)
})
