#!/usr/bin/node
if (parseInt(process.argv[2]) === NaN) {
	console.log('Not a number');
} else {
	console.log('My number:', parseInt(process.argv[2]));
}
