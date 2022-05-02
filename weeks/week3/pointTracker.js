class Point
{
	constructor(x, y)
	{
		this.x = x;
		this.y = y;
		if (Point.count == undefined)
		{
			Point.count = 1;
		}
		else if (Point.count == 1)
		{
			Point.count = 2;
		}
	}

	value()
	{
		return "(" + this.x + ", " + this.y + ")"
	}

	static getCount()
	{
		return (Point.count == undefined) ? 0: Point.count;
	}

	static distance(pt1, pt2)
	{
		var xDist, yDist, distance;
		xDist = pt1.x - pt2.x;
		yDist = pt1.y - pt2.y;
		distance = Math.sqrt(xDist**2 + yDist**2);
		return distance;
	}

};

var point1, point2;

function captureClick(e)
{
	if (Point.getCount() == 0)
	{
		point1 = new Point(e.clientX, e.clientY);
		document.getElementById("pt1").innerHTML = point1.value();
	}
	else if (Point.getCount() == 1)
	{
		point2 = new Point(e.clientX, e.clientY);
		document.getElementById("pt2").innerHTML=point2.value();
	}
	else
	{
		point1 = point2;
		point2 = new Point(e.clientX, e.clientY);
		document.getElementById("pt1").innerHTML=point1.value();
		document.getElementById("pt2").innerHTML=point2.value();
	}
}

function displayDistance(e)
{
	var distance;
	e.stopPropagation();
	distance = Point.distance(point1, point2);
	document.getElementById("distance").innerHTML = distance;
}

