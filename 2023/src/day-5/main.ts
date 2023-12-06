import express = require('express');
import fs = require('fs');

const app = express();
const port = 3000;

const fileContents = fs.readFileSync('src/day-5/input.txt').toString().split(/\r?\n/);

let partOneTotal = 0;
let partTwoTotal = 0;

//The first line is structured as follows
//seeds: 79 14 55 13
//So we can do the following to get an array of the seed values
const seeds = (fileContents[0].split(':'))[1].trim().split(/[ ,]+/);

//This is how we set which mapping to follow 
enum MapMode {
  SeedToSoil = 0,
  SoilToFertilizer = 1,
  FertilizerToWater = 2,
  WaterToLight = 3,
  LightToTemperature = 4,
  TemperatureToHumidity = 5,
  HumidityToLocation = 6
}

let mode = MapMode.SeedToSoil;

fileContents.shift();

fileContents.forEach(function (line, i) {
  console.log(line);  
});

app.get('/', (req, res) => {
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Part one: ${partOneTotal}\nPart two: ${partTwoTotal}`);
});