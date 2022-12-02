"use strict";
exports.__esModule = true;
var express = require("express");
var fs = require("fs");
var app = express();
var port = 3000;
var fileContents = fs.readFileSync('src/day-2/input.txt').toString().split(/\r?\n/);
var bestChoice = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
};
var worstChoice = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
};
var endState;
(function (endState) {
    endState["LOSE"] = "X";
    endState["TIE"] = "Y";
    endState["WIN"] = "Z";
})(endState || (endState = {}));
var map = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
};
var points = {
    'X': 1,
    'Y': 2,
    'Z': 3
};
var winPoints = 6;
var tiePoints = 3;
var pt1Score = 0;
//Part 1
for (var _i = 0, fileContents_1 = fileContents; _i < fileContents_1.length; _i++) {
    var round = fileContents_1[_i];
    var _a = round.split(' '), opponentChoice = _a[0], myChoice = _a[1];
    pt1Score += points[myChoice];
    //I win
    if (bestChoice[opponentChoice] === myChoice) {
        pt1Score += winPoints;
    }
    //Tie
    else if (map[opponentChoice] === myChoice) {
        pt1Score += tiePoints;
    }
}
var pt2Score = 0;
//Part 2
for (var _b = 0, fileContents_2 = fileContents; _b < fileContents_2.length; _b++) {
    var round = fileContents_2[_b];
    var _c = round.split(' '), opponentChoice = _c[0], endResult = _c[1];
    //I win
    if (endResult === endState.WIN) {
        pt2Score += winPoints + points[bestChoice[opponentChoice]];
    }
    //Tie
    else if (endResult === endState.TIE) {
        pt2Score += tiePoints + points[map[opponentChoice]];
    }
    //Lose :(
    else {
        pt2Score += points[worstChoice[opponentChoice]];
    }
}
app.get('/', function (req, res) {
    res.sendStatus(200);
});
app.listen(port, function () {
    return console.log("Pt 1: ".concat(pt1Score, "\nPt2: ").concat(pt2Score));
});
