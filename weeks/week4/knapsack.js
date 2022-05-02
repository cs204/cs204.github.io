const items = buildItems()

let xFGen = weightFilter(20, genPowerSet(items)) 
testSolution(xFGen)


function* genBin(n)//создаёт генератор двоичных последовательностей, добавляющий 1
{
	let b = []
	for(let i = 0; i < n; i++)
		b.push(0)
	yield b
	let i = 0
	while(true)
	{
		if(i == n)
		{
			return
		}
		else if( b[i] == 1)
		{
			b[i] = 0
			i++
		}
		else
		{
			b[i] = 1
			i = 0
			yield b
		}
	}
}

function* genPowerSet(items)//создаёт генератор подмножеств
{
	for(let x of genBin(items.length))
	{
		let taken = []
		for (let i = 0; i < x.length; i++)
		{
			if (x[i] == 1) taken.push(items[i])
		}
		yield taken
	}
}

function weightTest(taken, maxWeight)// проверяет, что вес не превышает заданный
{
	totalWeight = 0
	for(let t of taken)
	{
		totalWeight += t.weight 
		if(totalWeight > maxWeight)
		{
			return false
		}
	}
	return true
}



function* weightFilter(maxWeight, genSet) // создаёт генератор, выбирающий только множества правильного веса
{
	for(let taken of genSet)
	{
		if (weightTest(taken, maxWeight))
			yield taken
	}
	return
}

function genSolution(xFGen) // использует генератор, чтобы выбрать набор решающий задачу
{
	let totalValue = 0
	let taken = []
	for (let x of xFGen)
	{
		if (value(x) > totalValue)
		{
			totalValue = value(x)
			taken = x.slice()
		}
	}
	return {totalValue: totalValue, taken: taken}
}

function testSolution(xFGen)// выводит ответ
{
	const res = genSolution(xFGen)
	console.log("Цена взятого =", res.totalValue)
	console.log("Взяли:", res.taken)
}

function value(taken)//складывает цены 
{
	let totalValue = 0
	for(let item of taken)
	{
		totalValue += item.value 
	}
	return totalValue
}

function buildItems()// создаёт массив  вещей
{
	const names = ['часы', 'картина', 'радио', 'выза', 'книга', 'компьютер']
	const values = [175, 90, 20, 50, 10, 200]
	const weights = [10, 9, 4, 2, 1, 20]
	const items = []
	for (let i = 0; i < values.length; i++)
	{
		items.push({
			name:names[i], 
			value: values[i], 
			weight: weights[i]
		})
	} 
	return items
}

