async function grades_rows()
{
	let rowCount = gradesTable.rows.length
	for(let i = 0; i < rowCount; ++i)
		gradesTable.deleteRow(0)

	const url = 'http://90.188.117.161:8080/results/api_grades'
	const data = {id_house: houseSelect.value}
	const response = await fetch(url, 
		{
			method:'POST',
			headers:{'Content-Type':'application/json'},
			body: JSON.stringify(data)
		})
	const result = await response.json()
							
	const grades = result.gradebook
	const pset = result.pset
	rowCount = grades.length
	for(let i = 0; i < rowCount; ++i)
	{
		let row = gradesTable.insertRow()
		let cellLastName = row.insertCell()
		let cellFirstName = row.insertCell() 
		let cellSurname = row.insertCell() 
		cellLastName.innerHTML = grades[i].lastname
		cellFirstName.innerHTML = grades[i].firstname 
		cellSurname.innerHTML = grades[i].surname
		for(let problem of pset)
		{
			let cellGrade = row.insertCell()
			if(problem['id_problemset'] == 1)
			{ 
				cellGrade.innerHTML = `<input size=1 value='${grades[i].grades[problem['id_problemset']].grade}' disabled>`;
			}
			else
			{ 
				cellGrade.innerHTML = `<div title=${problem['name']}><a href=${grades[i].grades[problem['id_problemset']].url}>${grades[i].grades[problem['id_problemset']].grade}</a></div>`;
			}
		}
		
		let cellRemove = row.insertCell() 
		cellRemove.innerHTML = `<input class=messageCheckbox type=checkbox name='remove_list[]' value='${grades[i].id}'/>`
	}

	rowCount = psetTable.rows.length
	for(let i = 0; i < rowCount; ++i)
		psetTable.deleteRow(0)

	rowCount = pset.length
	for(let i = 0; i < rowCount; ++i)
	{
		let row = psetTable.insertRow()
		let cellId = row.insertCell()
		let cellName = row.insertCell()
		cellId.innerHTML = pset[i]['id_problemset']
		cellName.innerHTML =`<a href=${pset[i]['description']}> ${pset[i]['name']}</a>`
	}
}

document.addEventListener('DOMContentLoaded', ()=>
	{
		var gradesTable = document.querySelector('#gradesTable')
		var houseSelect = document.querySelector('#houseSelect')
		var psetTable = document.querySelector('#psetTable')
		houseSelect.addEventListener('input', grades_rows)
	}
)


