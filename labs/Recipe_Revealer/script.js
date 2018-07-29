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

let recipe = [];
let publishTxt = document.querySelector('#publishTxt');
let publishBtn = document.querySelector('#publishBtn');

console.log(publishBtn);
console.log(publishTxt);

function addInstructions(recipeArray){
// add all of the instructions into the recipeArray variable
    console.log("recipe added");
    recipeArray.push("Heat oven to 425ºF. Prepare Double-Crust Pastry.",
                    "Mix sugar, flour, cinnamon, nutmeg and salt in large bowl.",
                    "Stir in apples.",
                    "Turn into pastry-lined pie plate. Dot with butter. Trim overhanging edge of pastry 1/2 inch from rim of plate.",
                    "Roll other round of pastry. Fold into fourths and cut slits so steam can escape.",
                    "Unfold top pastry over filling; trim overhanging edge 1 inch from rim of plate.",
                    "Fold and roll top edge under lower edge, pressing on rim to seal; flute as desired.",
                    "Cover edge with 3-inch strip of aluminum foil to prevent excessive browning. Remove foil during last 15 minutes of baking.",
                    "Bake 40 to 50 minutes or until crust is brown and juice begins to bubble through slits in crust. Serve warm if desired.");
// return the array
}

function checkStep(recipeArray, step){
// return the correct step in the given array
    let stepNumber = parseInt(recipeArray.findIndex(step)) + 1;
}

// Write a function publishRecipe
function publishRecipeToPage(recipeArray){
    console.log("published");
    let publish = "";
    publish = recipeArray.join("\n");
    publishTxt.innerHTML = publish;
}

publishBtn.addEventListener("click",()=>{
    console.log("button clicked");
    addInstructions(recipe);
    console.log(recipe);
    publishRecipeToPage(recipe);
});
