var runButton = document.getElementById("run")

runButton.addEventListener('click', function() {
    //document.location.href = "../html/results.html";

    var python = require('child_process').spawn('python', ['src/python/tempSmart.py']);

    python.stdout.on('data', function(data){
        console.log("data: ",data.toString('utf8'));
       document.getElementById("print-results").innerHTML = data.toString('utf8');
    });
});