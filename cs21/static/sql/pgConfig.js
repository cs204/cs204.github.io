import dotenv from 'dotenv'
import pg from "pg";

dotenv.config()

export const pool = new pg.Pool({connectionString: process.env.DB_URL,
	    ssl: { rejectUnauthorized: false}
})

