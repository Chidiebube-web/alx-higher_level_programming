#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if(((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.height = h;
      this.width = w;
    }
  }
}
module.exports = Rectangle;
