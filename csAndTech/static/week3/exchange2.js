const msg = document.querySelector("#msg")
const url = "https://api.exchangeratesapi.io/latest?base=USD"

async function myFetch()
{
	const response = await fetch(url)
	const data = await response.json()
	msg.innerText = `1 USD = ${data.rates.RUB} RUB`
}

myFetch()

