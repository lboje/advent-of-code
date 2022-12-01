import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-1/input.txt').toString().split(/\n\s*\n/);


let maxCalories = Number.MIN_SAFE_INTEGER;
let secondBest = null;
let bronzeMedal = null;

for(let elf of fileContents) {
    let totalCalories = 0;
    for(let calories of elf.split('\n')) {
        totalCalories += +calories;
    }
    if(totalCalories > maxCalories) {
        bronzeMedal = secondBest;
        secondBest = maxCalories;
        maxCalories = totalCalories;
    }
    else if(totalCalories > secondBest) {
        bronzeMedal = secondBest;
        secondBest = totalCalories;
    }
    else if(totalCalories > bronzeMedal) {
        bronzeMedal = totalCalories;
    }
}

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  return console.log(`Max: ${maxCalories}\nTop three: ${maxCalories + secondBest + bronzeMedal}`);
});