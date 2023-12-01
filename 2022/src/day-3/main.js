"use strict";
exports.__esModule = true;
var express = require("express");
var fs = require("fs");
var app = express();
var port = 3000;
var fileContents = fs.readFileSync('src/day-3/input.txt').toString().split(/\r?\n/);
var priorityString = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
var prioritySum = 0;
for (var _i = 0, fileContents_1 = fileContents; _i < fileContents_1.length; _i++) {
    var rucksack = fileContents_1[_i];
    var compartment_a = rucksack.substring(0, (rucksack.length / 2));
    var compartment_b = rucksack.substring(rucksack.length / 2);
    for (var i = 0; i < rucksack.length / 2; i++) {
        if (compartment_b.includes(compartment_a[i])) {
            prioritySum += priorityString.indexOf(compartment_a[i]);
            break;
        }
    }
}
app.get('/', function (req, res) {
    res.sendStatus(200);
});
app.listen(port, function () {
    return console.log("Pt 1: ".concat(prioritySum));
});
