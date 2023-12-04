import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-4/input.txt').toString().split(/\r?\n/);

let partOneTotal = 1;


//List of how many times each card has appeared
const cardCount = Array<number>(fileContents.length).fill(1);

fileContents.forEach(function (card, cardNum) {
 //Get the actual card data
 card = card.split(':')[1].trim();
 //Split the card from its winnings
 //We then convert these into arrays containing each number
 const [winNums, cardNums] = card.split('|').map(nums => nums.trim().split(/[ ,]+/));

 //Wins is just the amount of winning numbers we had on our card
 const wins = (cardNums.filter(num => winNums.includes(num))).length;

 if(wins) {
  partOneTotal += (Math.pow(2, wins - 1));
  //For each of the next cards equal to the amount of wins
  //We want to add the number of cards that this card has
  for(let i = cardNum + 1; i <= cardNum + wins; i++) {
    cardCount[i] += cardCount[cardNum];
  }
 }
});

//Part two answer is equal to the sum of card counts
let partTwoTotal = cardCount.reduce((a, b) => a + b, 0)

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Part one: ${partOneTotal}\nPart two: ${partTwoTotal}`);
});