#!/usr/bin/node
let x = Number(process.argv[2]);
if (isNaN(x) || x === undefined) {
	console.log('Missing size');
} else {
	for (let i = 0; i < x; i++) {
		console.log('X'.repeeat(x));
	}
}
