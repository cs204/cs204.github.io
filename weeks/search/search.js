import Agenda from "./agenda.js"
import Explored from "./explored.js"
import Node from "./node.js"

export default function search(initialState, goalTest, actions, successor, print = true)
{
	const agenda = new Agenda()
	const explored = new Explored()
	const initialNode = new Node(null, initialState, null)
	agenda.add(initialNode)
	while(agenda.notEmpty())
	{
		const parent = agenda.getNode()
		if(goalTest(parent.state))
		{
			if(print)
				console.log("Solution:", parent.strPath())
			return parent.path()
		}
		explored.add(parent.state)
		for(const action of actions(parent.state))
		{
			const newS = successor(parent.state, action)
			const newN = new Node(action, newS, parent)
			if(!explored.hasState(newS))
			{
				agenda.add(newN)
				if(print)
					console.log(newN.strPath())
			}
		}
	}
	return null
}
