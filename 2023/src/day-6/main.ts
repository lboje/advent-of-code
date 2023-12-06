import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-6/input.txt').toString().split(/\r?\n/);

/**
 * Find and return the range in button presses that will surpass the given distance
 * within the given amount of time
 * 
 * We can express the total amount of time (t) in the race as as 
 * the amount of time holding the button (h) + the amount of time the boat moves (m).
 * 
 * As we all know, distance (d) = velocity (v) * time (t)
 * Since the speed increases at a rate of 1 millimeter per millisecond we hold the button,
 * the velocity is equal to h. 
 * 
 * And for calculating our distance traveled, we only need to be concerned 
 * with the amount of time the boat moves, so time is equal to b.
 * 
 * As such, we can use d = h * m to calculate the distance our boat will travel.
 * 
 * From t = h + m, we can solve that m = t - h and substitute that into the formula above
 * 
 * Now we have d = th - h^2 to calculate our distance. 
 * Since we want to know when we surpass the distance, we just need to find the first value for which
 * d < th - h^2
 * 
 * Technically, this can also be shown as 
 * h^2 - th + d = 0, and then solved appropriately.
 * The lower value would be the minimum value, and the higher would be the maximum. 
 * But I was too lazy to do that. 
 */
function findHoldingRange(time, distance) {
  //h is never going to be 0 - if we don't hold the button, the boat doesn't move. 
  let h = 1;

  //It's quadratic, it'll have an axis of symmetry at the time/2
  //So we don't need to even try past that
  for(h; h <= time/2; h++) {
    const d = (time * h) - Math.pow(h, 2);
    if(d > distance) {
      break;
    }
  }

  //For reasons I don't know, the minimum and maximum added together are equal to the time
  //I just observed it as I was solving by hand
  //If I figure it out later, I'll come back and edit this
  const max = time - h;
  //Get the inclusive distance between the min and max
  const range = max - h + 1;

  return range;
}


const partOneTotal = (function (){
  let total = 1;

  //The first line is structured as follows
  //Time:    1    2     7
  //So we can do the following to get a number array of the times
  const times = (fileContents[0].split(':'))[1].trim().split(/[ ,]+/).map(time => Number(time));
  //Distances are pretty much the same
  const distances = (fileContents[1].split(':'))[1].trim().split(/[ ,]+/).map(distance => Number(distance));

  for(let i = 0; i < times.length; i++) {
    const range = findHoldingRange(times[i], distances[i]);
    total *= range;
  }

  return total
})();


const partTwoTotal = (function (){
  //This time we want it all as one number
  const time = Number(fileContents[0].replace(/\D/g,''));
  //Ditto
  const distance = Number(fileContents[1].replace(/\D/g,''));
  const range = findHoldingRange(time, distance);
  return range;
})();


app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Part one: ${partOneTotal}\nPart two: ${partTwoTotal}`);
});