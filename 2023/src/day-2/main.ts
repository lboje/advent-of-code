import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-2/input.txt').toString().split(/\r?\n/);

const MAX_RED = 12;
const MAX_GREEN = 13;
const MAX_BLUE = 14;


type Game = {
  red: number,
  blue: number,
  green: number
}


let total = 0;

function isPossibleGame(game: Game): boolean {
  return game.red <= MAX_RED && game.green <= MAX_GREEN && game.blue <= MAX_BLUE;
}

fileContents.forEach(function (game, i) {
  //Get the actual game data
  game = game.split(':')[1].trim();
  //Split the games into individual sets
  const sets = game.split(';').map(set => set.trim());
  let isPossible = true;

  let minRed = 0;
  let minBlue = 0;
  let minGreen = 0;

  //Determine if each set would be possible
  for(let set of sets) {
    const pulls = set.split(',').map(pull => pull.trim());

    let red = 0;
    let blue = 0;
    let green = 0;


    for(let pull of pulls) {
      const [number, color]= pull.split(' ').map(property => property.trim());
      if(color === 'red') {
        red = Number(number);
        //Part 2
        minRed = red > minRed ? red : minRed;
      }
      else if(color === 'blue') {
        blue = Number(number);
        //Part 2
        minBlue = blue > minBlue ? blue : minBlue;
      }
      else if(color === 'green') {
        green = Number(number);
        //Part 2
        minGreen = green > minGreen ? green : minGreen;
      }
    }

  
    /* Part one code
    const balls = {
      red,
      blue,
      green
    }
    
    isPossible = isPossibleGame(balls);
    if(!isPossible) {
      break;
    }
    */
  }

  total += (minRed * minBlue * minGreen);

  /* Part one code
  if(isPossible) {
    total += (i + 1);
  }
  */
});

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Total: ${total}`)
});