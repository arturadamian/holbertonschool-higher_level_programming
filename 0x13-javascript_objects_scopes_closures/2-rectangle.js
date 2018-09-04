#!/usr/bin/node

module.exports =
    class Rectangle {
	constructor (w, h) {
	    if (isNaN(w) || w < 1 || isNaN(h) || h < 1) {
		return null;
	    }
	    this.width = w;
	    this.height = h;
	}
    };
