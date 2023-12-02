"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var express = require("express");
var fs = require("fs");
var app = express();
var port = 3000;
var fileContents = fs.readFileSync('src/day-2/input.txt').toString().split(/\r?\n/);
var MAX_RED = 12;
var MAX_GREEN = 13;
var MAX_BLUE = 14;
var total = 0;
function isPossibleGame(game) {
    return game.red <= MAX_RED && game.green <= MAX_GREEN && game.blue <= MAX_BLUE;
}
fileContents.forEach(function (game, i) {
    //Get the actual game data
    game = game.split(':')[1].trim();
    //Split the games into individual sets
    var sets = game.split(';').map(function (set) { return set.trim(); });
    var isPossible = true;
    var minRed = 0;
    var minBlue = 0;
    var minGreen = 0;
    //Determine if each set would be possible
    for (var _i = 0, sets_1 = sets; _i < sets_1.length; _i++) {
        var set = sets_1[_i];
        var pulls = set.split(',').map(function (pull) { return pull.trim(); });
        var red = 0;
        var blue = 0;
        var green = 0;
        for (var _a = 0, pulls_1 = pulls; _a < pulls_1.length; _a++) {
            var pull = pulls_1[_a];
            var _b = pull.split(' ').map(function (property) { return property.trim(); }), number = _b[0], color = _b[1];
            if (color === 'red') {
                red = Number(number);
                //Part 2
                minRed = red > minRed ? red : minRed;
            }
            else if (color === 'blue') {
                blue = Number(number);
                //Part 2
                minBlue = blue > minBlue ? blue : minBlue;
            }
            else if (color === 'green') {
                green = Number(number);
                //Part 2
                minGreen = green > minGreen ? green : minGreen;
            }
        }
        /* Part one code
        const balls = {
          red,
          blue,
          green
        }
        
        isPossible = isPossibleGame(balls);
        if(!isPossible) {
          break;
        }
        */
    }
    total += (minRed * minBlue * minGreen);
    /* Part one code
    if(isPossible) {
      total += (i + 1);
    }
    */
});
app.get('/', function (req, res) {
    res.sendStatus(200);
});
app.listen(port, function () {
    console.log("Total: ".concat(total));
});
