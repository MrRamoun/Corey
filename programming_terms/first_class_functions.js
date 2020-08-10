function sq(num) {
	return num*num
}

function cu(num) {
	return num*num*num
}

var value = sq(5) // using the '()' for execution

var square = sq

console.log(value)
console.log(square)
console.log(sq)
console.log(square(6))

/* building our own map function */
function my_map(func, array) {
	var result = []
	for(var i = 0; i < array.length; i++){
		result.push(func(array[i]))
	}
	return result
}

var squares = my_map(square, [1,2,3,4,5,6])
console.log(squares)

