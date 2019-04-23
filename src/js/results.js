
function showResults() {
    var fs = require('fs');
    var readData = fs.readFileSync('src/js/results.json');
    var results = JSON.parse(readData);

    document.getElementById("print-results").innerHTML = results;
}