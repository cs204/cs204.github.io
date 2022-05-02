const fetch = require("node-fetch")
fetch('http://termopogoda.ru/data_tomsk.json').then(response => response.json()).then(data => console.log("ans" + data.current_temp))
