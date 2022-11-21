

class Sentence
{
	constructor(cells, count)
	{
		this.cells = new Set(cells);
		this.count = count;
	}

	equal(other)
	{
		if((this.count !== other.count) || (this.cells.size !== other.cells.size)) return false;
		for(var a of this.cells)
			if(!other.cells.has(a))
				return false;
		return true;
	}

	known_mines()
	{
		//Возвращает ячейки, о которых известно, что они мины.
		//--------------------------------Реализуйте самостоятельно-----------
		if(this.cells.size == this.count)
		{
			let s1 = new Set(this.cells);
			return s1; 
		}
		else 
			return new Set();
	}

	known_safes()
	{

		//Возвращает ячейки, о которых известно, что они безопасны.
		//--------------------------------Реализуйте самостоятельно-----------
		
		if(this.count == 0)
		{
			let s1 = new Set(this.cells);
			return s1;
		}
		else
			return new Set();
	}

	mark_safe(cell)
	{
		//Обновляет внутреннее представление знаний, 
		//учитывая, что ячейка известна как безопасная.
		//--------------------------------Реализуйте самостоятельно-----------
		if(this.cells.has(cell))
			this.cells.delete(cell);

	}


	mark_mine(cell)
	{
		//Обновляет внутреннее представление знаний, 
		//учитывая, что ячейка изсвестна как мина.
		//--------------------------------Реализуйте самостоятельно-----------
		if(this.cells.has(cell))
		{
			this.cells.delete(cell);
			this.count = this.count - 1;
		}
	}

	infer_from(sentence2)
	{
		if(this.equal(sentence2)){ return 0;}
		if(isSubset(this.cells, sentence2.cells))
		{
			let set1 = this.cells;
			let set2 = sentence2.cells;
			let subSet = new Set([...set2].filter(elem=>!set1.has(elem)));
			return new Sentence(subSet,sentence2.count - this.count);
		}
		if(isSubset(sentence2.cells, this.cells))
		{
			let set1 = sentence2.cells;
			let set2 = this.cells;
			let subSet = new Set([...set2].filter(elem=>!set1.has(elem)));
			return new Sentence(subSet, this.count - sentence2.count);
		}
		else
			return 0;
	}
}


