// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Use querySelector to store the div in a variable.
let colorSelected = 'white';

let redButton = document.querySelector('#red');
let greenButton = document.querySelector('#green');
let blueButton = document.querySelector('#blue');
let clearButton = document.querySelector('#clear');

let box = document.getElementById('responseBox');

function changeColor(color){
  console.log("You clicked the " + color + " button!");
  box.style.backgroundColor = color;
  box.innerHTML = color.charAt(0) + color.substr(1);
  box.innerHTML.fontcolor = 'white';
}

clearButton.addEventListener('click', e =>{
  box.style.backgroundColor = 'white';
});

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', e => {
  changeColor('red');
});

greenButton.addEventListener('click',e => {
  changeColor('green');
})

blueButton.addEventListener('click', e => {
  changeColor('blue');
});