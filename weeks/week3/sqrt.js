function sqrt(e)
{
	var x = parseFloat(document.getElementById("x").value);
	var res = Math.sqrt(x);
	document.getElementById("res").value = res.toFixed(2);
}

document.addEventListener("DOMContentLoaded",
	function ()
	{
		var btn = document.getElementById("btn");
		btn.addEventListener("click", sqrt);
	}
);



