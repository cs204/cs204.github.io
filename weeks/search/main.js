import {actions, successor, goalTest} from "./game.js"
import search from "./search.js"

search('a', goalTest, actions, successor)

