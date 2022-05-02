let l = [1, 5, "Bob", 6] //литерал массива
l.push(9)//Добавляет новый элемент в конец массива
for (let i = 0; i < l.length; i++)
{
console.log(`l[${i}]=${l[i]}`)
}
l.reverse()//меняет порядок элементов
console.log(l)

let l2 = l.slice(1, 4)//создает новый массив с элементами с первого по 3 
console.log(l2)


