#!/usr/bin/node

// This line specifies that the script should be run using the Node.js interpreter

const request = require('request');

// Import the request library to make HTTP requests

const movieId = process.argv[2];

// Get the movie ID from the command-line argument (second argument)

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

// Define the request options:
//  - url: The API endpoint to retrieve movie data (including the movie ID)
//  - method: The HTTP method (GET) to retrieve data

request(options, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
