const {Pool} = require('pg')

const connectionString = 'postgresql://vadim:12345@localhost:5432/register'

const pool = new Pool(
    {
        connectionString,
    })

;(async () =>
	{
		const resalt = await pool.query('select * from students;')
		for(let res of resalt.rows)
			console.log(res.firstname,', ', res.lastname)
		await pool.end()
	}
)()
