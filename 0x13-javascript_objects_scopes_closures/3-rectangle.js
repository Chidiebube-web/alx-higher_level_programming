#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if(((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.height = h;
      this.width = w;
    }
  }
    
   print () {
      for (let i = 0; i<this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
}
module.exports = Rectangle;
