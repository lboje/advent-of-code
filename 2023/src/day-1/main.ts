import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-1/input.txt').toString().split(/\r?\n/);

const valMap = {
  "one" : '1',
  "two": '2',
  "three": '3',
  "four": '4',
  "five": '5',
  "six": '6',
  "seven": '7',
  "eight": '8',
  "nine": '9'
}

let total = 0;

for(let line of fileContents) {
  //Part two: this
  //Replace all values to be equal to numberic value
  let regex = new RegExp(Object.keys(valMap).join('|'), "gi");
  line = line.replace(regex, function(numWord) {
    return valMap[numWord];
  });

  
  //Filter string such that we have only the numbers within it
  line = line.replace(/\D/g,'');

  const first = line.charAt(0);
  const last = line.charAt(line.length - 1);

  const number = Number(first + last);
  total += number;
}

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Total: ${total}`)
});