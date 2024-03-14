function changeSubmitBtnStatus() {
    var submitBtn = document.getElementById("submit-btn");
    var questionInput = document.getElementById("question-input");

    if (questionInput.value.length > 0) {
        submitBtn.disabled = false;
    } else {
        submitBtn.disabled = true;
    }
}

async function submitQuestion() {
    var questionInput = document.getElementById("question-input");
    var question = questionInput.value;

    var submitBtnIcon = document.getElementById("submit-btn-icon");
    submitBtnIcon.classList.remove("fa-paper-plane")
    submitBtnIcon.classList.add("fa-spinner")
    submitBtnIcon.classList.add("fa-spin-pulse")

    if (question.length > 0) {
        console.log("Submitting question: " + question);
    }



    showQuestion(question);

    var answerItem = document.getElementById("answer-textarea");
    answerItem.innerHTML = "Loading...";

    let answer = await fetchAnswer(question);
    answer = answer.trimStart();
    answer = answer.replace(/\n/g, "<br/>");
    // answer = answer.replace(/\\t/g, "&nbsp;&nbsp;&nbsp;&nbsp;");
    // answer = answer.replace(/\\'/g, "'");
    // answer = answer.replace(/\\"/g, '"');
    // answer = answer.replace(/\\&/g, "&");
    // answer = answer.replace(/\\r/g, "\r");

    answerItem.innerHTML = answer;
    submitBtnIcon.classList.remove("fa-spinner")
    submitBtnIcon.classList.remove("fa-spin-pulse")
    submitBtnIcon.classList.add("fa-paper-plane")

    // decrementQuestionsRemaining(); // TODO define function when ready
}

function showQuestion(question) {
    var questionInput = document.getElementById("question-input");
    var questionItem = document.getElementById("question-textarea")
    questionItem.innerHTML = question;

    questionInput.value = ""

    var submitBtn = document.getElementById("submit-btn");

    submitBtn.disabled = true;
}

async function fetchAnswer(question) {
    try {
        var userid = Clerk.user.id;
    } catch (error) {
        return "You must be logged in to ask a question."
    }
    var url = "/ai?userid=" + userid + "&question=" + question;

    var answer = ""

    try {
        let response = await fetch(url);
        let data = await response.json();
        console.log(data);
        answer = data;
    } catch (error) {
        console.log(error);
        answer = "Error...see console for details.";
    }
    return answer;
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('question-input').addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            submitQuestion();
        }
    });

    document.getElementById('submit-btn').addEventListener('click', function () {
        submitQuestion();
    });
});
