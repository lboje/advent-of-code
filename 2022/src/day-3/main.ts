import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-3/input.txt').toString().split(/\r?\n/);

const priorityString = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

let prioritySum1 = 0;

for(const rucksack of fileContents) {
    const compartment_a = rucksack.substring(0, (rucksack.length / 2));
    const compartment_b = rucksack.substring(rucksack.length / 2);
    for(let i = 0; i < rucksack.length / 2; i++){
        if(compartment_b.includes(compartment_a[i])) {
            prioritySum1 += priorityString.indexOf(compartment_a[i]);
            break;
        }
    }
}

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  return console.log(`Pt 1: ${prioritySum1}`);
});