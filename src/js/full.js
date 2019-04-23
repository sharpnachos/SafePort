// declaring JSON variables
var fs = require('fs');
var readData = fs.readFileSync('src/js/results.json');
var results = JSON.parse(readData);

console.log(results);

var runFull = document.getElementById("runFull")

runFull.addEventListener('click', function() {

    var python = require('child_process').spawn('python', ['src/python/tempFull.py']);

    python.stdout.on('data', function(data){

        console.log("data: ",data.toString('utf8'));
        //document.getElementById("print-results").innerHTML = data.toString('utf8');

        // store results in JSON
        results = data.toString('utf8');
        var writeData = JSON.stringify(results);
        fs.writeFile('src/js/results.json', writeData, (err) => {
            if (err)
                throw err;
            else
                document.location.href = "../html/results.html";
            //console.log('The file has been saved!');
        });
    });

    //alert("test");
    //document.location.href = "../html/results.html";
});