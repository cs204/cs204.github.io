async function termo()
{
	const url = "http://termopogoda.ru/data_tomsk.json"

	const response = await fetch(url, {method: 'GET', mode: 'no-cors'})
	return  await response.json()
}
			


document.addEventListener("DOMContentLoaded", function () 
	{
		termo().then(data =>
			{
				let msg = document.getElementById("msg")
				msg.innerHTML = data.current_temp
			})
	}
)


