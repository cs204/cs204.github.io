async function exchange(e)
{
	let url = "https://api.exchangeratesapi.io/latest?base=USD";
	let response = await fetch(url);
	let parsed = await response.json();
	let rub = parsed.rates.RUB;
	let res = document.getElementById("res");
	res.innerHTML = rub.toFixed(2);
}

document.addEventListener("DOMContentLoaded", exchange);
