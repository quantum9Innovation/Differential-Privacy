var flip = function (dataArray) {
	var a = dataArray
	for(var i = 0; i < a.length; i++) {
		var b = Math.random(0,1)
		var c = Math.round(b)
		if(c === 1) {
				var b1 = Math.random(0,1)
				var c1 = Math.round(b1)
				if(c1 === 0) {

				}
				if(c1 === 1) {
				a[i] = false
				}
		}
	}
		dataArray = a
}