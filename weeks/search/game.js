export function goalTest(state)
{
	return state === 'e'
}

const stateSpace = {'a':['b'], 'b': ['c', 'd'], 'c':['e'], 'd': ['f'], 'e':[], 'f':[]}

export function actions(s)
{
	const n = stateSpace[s].length
	const l = []
	for(let i = 0; i < n; i++)
		l.push(i)
	return l
}

export function successor(state, action)
{
	return stateSpace[state][action]
}
