const msg = document.querySelector("#msg")
const btn = document.querySelector("#btn")
function hello()
{
	msg.innerText = "Hello, World!"
	msg.style.color = "red"
}

btn.addEventListener("click", hello)
