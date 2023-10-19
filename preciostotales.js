// Import required modules
const https = require('https');
const fs = require('fs');
const csv = require('csv-stringify');

// Define the API URL for electricity prices
const apiUrl = 'https://api.preciodelaluz.org/v1/prices/all?zone=PCB';

// Define an array of time intervals (hours)
const horas = [
  '00-01', '01-02', '02-03', '03-04', '04-05', '05-06', '06-07', '07-08',
  '08-09', '09-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16',
  '16-17', '18-19', '19-20', '20-21', '21-22', '22-23', '23-24'
];

// Create an empty array to store electricity prices
const precios = [];

// Initialize variables to calculate the average price
var long = 0;

// Send an HTTP GET request to the API URL
https.get(apiUrl, res => {
  let data = '';
  const headerDate = res.headers && res.headers.date ? res.headers.date : 'no response date';
  console.log('Status Code:', res.statusCode);
  console.log('Date in Response header:', headerDate);

  // Listen for incoming data from the API
  res.on('data', chunk => {
    data += chunk;
  });

  // When the response ends
  res.on('end', () => {
    console.log('Response ended: ');

    try {
      // Parse the received JSON data
      const jsonData = JSON.parse(data);

      // Create a CSV file with headers and write it
      csv.stringify([['hora', 'precio [€/MWh]']], (e, o) => fs.writeFileSync('data.csv', o));

      // Iterate over the specified time intervals
      for (let i = 0; i < horas.length; i++) {
        // Get data for the current hour interval
        var horaDato = jsonData[horas[i]];
        console.log(`Prize of the electricity today, ${horaDato.date} :`);
        console.log(`Between ${horaDato.hour} hours the prize will be: ${horaDato.price} ${horaDato.units}`);

        // Prepare data for writing to the CSV file
        dato = [[i + 1, horaDato.price]];

        // Push the price into the 'precios' array
        precios.push(horaDato.price);

        // Append the data to the CSV file
        csv.stringify(dato, (e, o) => fs.appendFileSync('data.csv', o));
      }

      // Calculate the average price
      long = precios.length;
      avg = precios.reduce((a, b) => a + b, 0) / long;
      console.log('Maximum Price:', Math.max(...precios));
      console.log('The average is: ', avg);
    } catch (error) {
      console.error('Error parsing JSON:', error.message);
    }
  });
}).on('error', err => {
  console.error('Error: ', err.message);
});
