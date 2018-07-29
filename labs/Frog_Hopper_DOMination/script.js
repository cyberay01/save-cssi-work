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
const reset = 6;
let currentlily = 1;
let frogger = document.querySelector("#frog")/*use a querySelector to grab your frog from your HTML*/;

frogger.addEventListener('click', function(){
// Insert what should happen when you click on the frog!
    document.querySelector("#lilypad" + currentlily).classList.remove("active");
    currentlily++;
    if(currentlily == reset){
        currentlily = 1;
    }
    frogger.style.left = window.getComputedStyle(document.querySelector("#lilypad" + currentlily)).left;
    frogger.style.top = window.getComputedStyle(document.querySelector("#lilypad" + currentlily)).top;
    console.log(currentlily);
    document.querySelector("#lilypad" + currentlily).classList.add("active");
});

function changeSize(element,sizeChange){

    element.style.height = element.offsetHeight + sizeChange + "px";
    element.style.width = element.offsetWidth + sizeChange + "px";

frogger.addEventListener('mouseover',()=>{
    changeSize(frogger, 10);
});

frogger.addEventListener('mouseout',()=>{
    changeSize(frogger, -10);
});