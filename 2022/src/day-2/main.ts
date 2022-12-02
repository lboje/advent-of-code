import e = require('express');
import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-2/input.txt').toString().split(/\r?\n/);

const bestChoice = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X'
};

const worstChoice = {
    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y'
};

enum endState {
    LOSE = 'X',
    TIE = 'Y',
    WIN = 'Z'
}

const map = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
}

const points = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
};

const winPoints = 6;
const tiePoints = 3;

let pt1Score = 0;

//Part 1
for(let round of fileContents){
    const [opponentChoice, myChoice] = round.split(' ');
    pt1Score += points[myChoice]; 
    //I win
    if (bestChoice[opponentChoice] === myChoice) {
        pt1Score += winPoints;
    }
    //Tie
    else if(map[opponentChoice] === myChoice) {
        pt1Score += tiePoints; 
    }
}

let pt2Score = 0;

//Part 2
for(let round of fileContents){
    const [opponentChoice, endResult] = round.split(' ');

    //I win
    if (endResult === endState.WIN) {
        pt2Score += winPoints + points[bestChoice[opponentChoice]];
        
    }
    //Tie
    else if(endResult === endState.TIE) {
        pt2Score += tiePoints + points[map[opponentChoice]]; 
    }
    //Lose :(
    else {
        pt2Score += points[worstChoice[opponentChoice]];
    }
}

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  return console.log(`Pt 1: ${pt1Score}\nPt2: ${pt2Score}`);
});