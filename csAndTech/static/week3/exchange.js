const msg = document.querySelector("#msg")
const url = "https://api.exchangeratesapi.io/latest?base=USD"
fetch(url)
.then(function(response)
	{
		return response.json()
	}
)
.then(function (data)
	{
		msg.innerText = `1 USD = ${data.rates.RUB} RUB`
	}
)

