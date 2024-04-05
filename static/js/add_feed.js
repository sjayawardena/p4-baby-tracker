/** Defining global variables */

const dropdown = document.querySelector("#id_feed_type"); //variable for dropdown feedtype selector
const breast = document.querySelector("#div_id_breast_feed_time_minutes"); //variable for breast feed duration input
const formula = document.querySelector("#div_id_formula_amount_ml"); //variable for formula feed amount input

dropdown.addEventListener("change", event => {
  if (event.target.value === 'breast') {
    breast.style.display = 'block'
    formula.style.display = 'none'
  }
  else if (event.target.value === 'formula') {
    breast.style.display = 'none'
    formula.style.display = 'block'
  }
  else {
    breast.style.display = 'none'
    formula.style.display = 'none'
  }
})
