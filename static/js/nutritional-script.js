const nutritionalsearchBtn = document.getElementById('nutritional-search-btn');

// event listeners
nutritionalsearchBtn.addEventListener('click', getNutritionalValue);

// get meal list that matches with the ingredients
function getNutritionalValue(){
    let item = document.getElementById('nutritional-search-input').value.trim();
    fetch(
        `https://trackapi.nutritionix.com/v2/natural/nutrients`,
        {
        method: "POST",
        headers: {
        "content-type": "application/json",
        "x-app-id": "af3b3111",
        "x-app-key": "467b792fa3b9a09a4c5d14ba98883980",
        "x-remote-user-id": "0"
        },
        body: JSON.stringify({query:item})
        })
    .then(response => response.json())
    .then(data => {
        //console.log(data.foods[0].food_name);
        let array = data.foods[0];
        let tableData="";
        let tableHeading="";
        tableHeading=`<h1>${array.food_name}</h1>`
        document.getElementById("table_heading").innerHTML=tableHeading;
        tableData=`
            <thead>
            <tr>
                <th>Nutrient</th>
                <th>Value</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td>Calories</td>
              <td>${array.nf_calories}</td>
            </tr>
            <tr>
              <td>Total Fat</td>
              <td>${array.nf_total_fat}</td>
            </tr>
            <tr>
              <td>Saturated Fat</td>
              <td>${array.nf_saturated_fat}</td>
            </tr>
            <tr>
              <td>Cholesterol</td>
              <td>${array.nf_cholesterol}</td>
            </tr>
            <tr>
              <td>Sodium</td>
              <td>${array.nf_sodium}</td>
            </tr>
            <tr>
              <td>Total Carbs</td>
              <td>${array.nf_total_carbohydrate}</td>
            </tr>
            <tr>
              <td>Dietary Fiber</td>
              <td>${array.nf_dietary_fiber}</td>
            </tr>
            <tr>
              <td>Sugars</td>
              <td>${array.nf_sugars}</td>
            </tr>
            <tr>
              <td>Proteins</td>
              <td>${array.nf_protein}</td>
            </tr>
        </tbody>
        `;
        document.getElementById("table_data").innerHTML=tableData;
    });
}
