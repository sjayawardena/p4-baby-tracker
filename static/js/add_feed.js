/** Defining global variables to be used in functions */

const feedTypeSelector = document.getElementById("id_feed_type") //variable for dropdown menu on feed form to select feed type - breast or formula

/** Function to show Formula Amount (ml) input if formula feed type is selected */

function showFormulaAmountInput() {
    document.getElementById("div_id_formula_amount_ml").style.display="block";
}

/** Function to show Breast Feed Duration (Minutes) input if breast feed type is selected */

function showBreastFeedDurationInput() {
    document.getElementById("div_id_breast_feed_time_minutes").style.display="block";
}

function showFeedAmountInputs() {
    if (feedTypeSelector.value == "Formula") {
        showFormulaAmountInput();
    }
    else if (feedTypeSelector.value == "Breast") {
        showBreastFeedDurationInput();
    }
}

showFeedAmountInputs();