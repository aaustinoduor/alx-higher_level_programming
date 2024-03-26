#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

//  the 'request' module to perform HTTP GET request to Star Wars API URL.
request(apiUrl, function (error, response, body) {
  // check if there was no error during HTTP request
  if (!error && response.statusCode === 200) {
    // parse JSON response bod
    const movieData = JSON.parse(body);
    // Create an array of promises that fetch data for each individual character.
    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        // use another 'request' to fetch data for individual character.
        request(characterUrl, function (charError, charResponse, charBody) {
          // check if there was no error during HTTP request
          if (!charError && charResponse.statusCode === 200) {
            // parse JSON response body
            const characterData = JSON.parse(charBody);
            // resolve promise with name of character.
            resolve(characterData.name);
          } else {
            // reject promise with error message if  there was an error during HTTP request
            reject(new Error(`Error fetching character data: ${charError}`));
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        console.log(characterNames.join('\n'));
      })
      .catch((error) => {
        console.error(error.message);
      });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
}
