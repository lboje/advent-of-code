"use strict";
exports.__esModule = true;
var express = require("express");
var fs = require("fs");
var app = express();
var port = 3000;
var fileContents = fs.readFileSync('src/day-1/input.txt').toString().split(/\n\s*\n/);
var maxCalories = Number.MIN_SAFE_INTEGER;
var secondBest = null;
var bronzeMedal = null;
for (var _i = 0, fileContents_1 = fileContents; _i < fileContents_1.length; _i++) {
    var elf = fileContents_1[_i];
    var totalCalories = 0;
    for (var _a = 0, _b = elf.split('\n'); _a < _b.length; _a++) {
        var calories = _b[_a];
        totalCalories += +calories;
    }
    if (totalCalories > maxCalories) {
        bronzeMedal = secondBest;
        secondBest = maxCalories;
        maxCalories = totalCalories;
    }
    else if (totalCalories > secondBest) {
        bronzeMedal = secondBest;
        secondBest = totalCalories;
    }
    else if (totalCalories > bronzeMedal) {
        bronzeMedal = totalCalories;
    }
}
app.get('/', function (req, res) {
    res.sendStatus(200);
});
app.listen(port, function () {
    return console.log("Max: ".concat(maxCalories, "\nTop three: ").concat(maxCalories + secondBest + bronzeMedal));
});
