var runButton = document.getElementById("run")

runButton.addEventListener('click', function() {

    var python = require('child_process').spawn('python', ['src/python/tempSmart.py']);

    python.stdout.on('data', function(data){
        console.log("data: ",data.toString('utf8'));
       document.getElementById("print-results").innerHTML = data.toString('utf8');
    });

    //document.location.href = "../html/results.html";
});