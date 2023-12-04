import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-3/input.txt').toString().split(/\r?\n/).map(line => line.split(''));


let total = 0;


function findNeighbors(fileContents, rowNum, colNum) {

}


fileContents.forEach(function (row, x) {
  row.forEach(function (char, y) {
    if(!`0123456789.`.includes(char))
      console.log(`${x}, ${y} : ${char}`);

  })
});

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Total: ${total}`)
});