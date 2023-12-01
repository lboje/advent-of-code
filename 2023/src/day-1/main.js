"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var express = require("express");
var fs = require("fs");
var app = express();
var port = 3000;
var fileContents = fs.readFileSync('src/day-1/input.txt').toString().split(/\r?\n/);
var valMap = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
};
var total = 0;
for (var _i = 0, fileContents_1 = fileContents; _i < fileContents_1.length; _i++) {
    var line = fileContents_1[_i];
    //Part two: this
    //Replace all values to be equal to numberic value
    var regex = new RegExp(Object.keys(valMap).join('|'), "gi");
    line = line.replace(regex, function (numWord) {
        return valMap[numWord];
    });
    //Filter string such that we have only the numbers within it
    line = line.replace(/\D/g, '');
    var first = line.charAt(0);
    var last = line.charAt(line.length - 1);
    var number = Number(first + last);
    total += number;
}
app.get('/', function (req, res) {
    res.sendStatus(200);
});
app.listen(port, function () {
    console.log("Total: ".concat(total));
});
