import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-4/input.txt').toString().split(/\r?\n/);

let total = 0;

fileContents.forEach(function (card, i) {
 //Get the actual card data
 card = card.split(':')[1].trim();
 //Split the card from its winnings
 //We then convert these into arrays containing each number
 const [winNums, cardNums] = card.split('|').map(nums => nums.trim().split(/[ ,]+/));

 const wins = (cardNums.filter(num => winNums.includes(num))).length;

 console.log(wins);
 if(wins) {
  total += (Math.pow(2, wins - 1));
 }
});

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Total: ${total}`)
});