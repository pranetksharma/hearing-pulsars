/*
var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

function changeHandler({
  target
}) {
  // Make sure we have files to use
  if (!target.files.length) return;

  // Create a blob that we can use as an src for our audio element
  const urlObj = URL.createObjectURL(target.files[0]);

  // Create an audio element
  const audio = document.createElement("audio");

  // Clean up the URL Object after we are done with it
  audio.addEventListener("load", () => {
    URL.revokeObjectURL(urlObj);
  });

  // Append the audio element
  document.body.appendChild(audio);

  // Allow us to control the audio
  audio.controls = "true";

  // Set the src and start loading the audio from the file
  audio.src = urlObj;
}

document
  .getElementById("audio-upload")
  .addEventListener("change", changeHandler);

  function getUserName() {
    var nameField = document.getElementById('nameField').value;
    var result = document.getElementById('result');
    
    if (nameField.length > 3) {
        result.textContent = 'Username must contain at least 3 characters';
        //alert('Username must contain at least 3 characters');
    } 
    else {
        result.textContent = 'You selected: ' + nameField;
        alert(nameField);

        /*const fs = require('fs');

        console.log("\nFile Contents of file before append:",
          fs.readFileSync("example_file.txt", "utf8"));
          
        fs.appendFile("example_file.txt", nameField, (err) => {
          if (err) {
            console.log(err);
          }
          else {
            // Get the file contents after the append operation
            console.log("\nFile Contents of file after append:",
              fs.readFileSync("example_file.txt", "utf8"));
          }
        });*/

        
const out1 = document.getElementById('output1');
const prof1 = document.getElementById('profile1');
const profsubmit1 = document.getElementById('profsubmit1');
const dm1 = document.getElementById('dm1');
const dmsubmit1 = document.getElementById('dmsubmit1');
const tp1 = document.getElementById('tp1');
const tpsubmit1 = document.getElementById('tpsubmit1');
const fp1 = document.getElementById('fp1');
const fpsubmit1 = document.getElementById('fpsubmit1');
const final1 = document.getElementById('final1');
const finalsubmit1 = document.getElementById('finalsubmit1');

function profile_galadriel(){
  out1.innerHTML += prof1.value;
}
function dm_jakub(){
  out1.innerHTML += dm1.value;
}
function tp_gandalf(){
  out1.innerHTML += tp1.value;
}
function fp_hobbit(){
  out1.innerHTML += fp1.value;
}

profsubmit1.addEventListener("click", profile_galadriel)
dmsubmit1.addEventListener("click", dm_jakub)
tpsubmit1.addEventListener("click", tp_gandalf)
fpsubmit1.addEventListener("click", fp_hobbit)

var dialog = document.querySelector('dialog'); 
document.querySelector('#show').onclick = function() { 
    dialog.show(); 
    }; 
document.querySelector('#close').onclick = function() { 
    dialog.close(); 
    }; 



/*function performClick(elemId) {
    var elem = document.getElementById(elemId);
    if(elem && document.createEvent) {
       var evt = document.createEvent("MouseEvents");
       evt.initEvent("click", true, false);
       elem.dispatchEvent(evt);
    }
 }*/