#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if(((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.height = h;
      this.width = w;
    }
    
    print () {
      console.log(('X'.repeat(this.height) + '\n').repeat(this.height - 1) + 'X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
