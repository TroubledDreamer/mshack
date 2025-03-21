


<script setup>

let multipleChoiceOptions = {
    type: 'multipleChoiceOptions',
    question: 'What is the capital of France?',
    options: ['Paris', 'London', 'Berlin', 'Madrid'],
    answer: 'Paris'
}

let trueOrFalse = {
    type: 'trueOrFalse',
    question: 'Paris is the capital of France',
    answer: 'true'
}


let shortAnswer = {
    type: 'shortAnswer',
    question: 'What is the capital of France?',
    answer: 'Paris'
}


let speach = {
    type: 'speach',
    question: 'What is the capital of France?',
    answer: 'Paris'
}



let speakRespond = {
    type: 'speakRespond',
    question: 'What is the capital of France?',
    answer: 'Paris'
}



function renderMultipleChoiceOptions(question) {
    document.getElementById('question').innerHTML = question.question;
    document.getElementById('option1').innerHTML = question.options[0];
    document.getElementById('option2').innerHTML = question.options[1];
    document.getElementById('option3').innerHTML = question.options[2];
    document.getElementById('option4').innerHTML = question.options[3];
}

function rendertrueOrFalse(question) {
    document.getElementById('question').innerHTML = question.question;
    document.getElementById('true').innerHTML = 'True';
    document.getElementById('false').innerHTML = 'False';
}


function renderShortAnswer(question) {
    document.getElementById('question').innerHTML = question.question;
}


function renderSpeach(question) {
    document.getElementById('question').innerHTML = question.question;
}

function renderSpeakRespond(question) {
    document.getElementById('question').innerHTML = question.question;
}


function renderQuestion(question) {
    if (question.type === 'multipleChoiceOptions') {
        renderMultipleChoiceOptions(question);

    }

    if (question.type === 'trueOrFalse') {
        rendertrueOrFalse(question);
    }

    if (question.type === 'shortAnswer') {
        renderShortAnswer(question);
    }

    if (question.type === 'speach') {
        renderSpeach(question)
    }

    if (question.type === 'speakRespond') {
        renderSpeakRespond(question);
    }
}



renderQuestion(multipleChoiceOptions);


</script>



<template>

    <div>
        <h1>questions</h1>
        <div id="question"></div>

        <div id="answers">
            <div id="mqc">
                <div id="4options">
                    <div id="option1"></div>
                    <div id="option2"></div>
                    <div id="option3"></div>
                    <div id="option4"></div>
                </div>

                <div id="trueOrFalse">
                    <div id="true"></div>
                    <div id="false"></div>
                </div>
            </div>


            <div id="shortAnswer">

            </div>


            <div id="speach">


            </div>



            <div id="speakRespond">

            </div>





        </div>



    </div>



</template>

