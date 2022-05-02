function hello(e) 
{ 
	let name = document.getElementById("name").value; 
	let msg = document.getElementById("msg");

	if(name  === "") 
	{ 
		msg.innerHTML = "Hello, World!"; 
	}
	else
	{
		msg.innerHTML = "Hello, " + name + "!";
	}

		document.body.style.backgroundColor = "aqua";
		document.getElementById("myForm").reset();
}

document.addEventListener("DOMContentLoaded", 
	function (e)  
	{ 
		const btn = document.getElementById("btn"); 
		btn.addEventListener("click", hello);
	}
);

