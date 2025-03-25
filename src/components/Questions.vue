<script setup>
import { ref, onMounted } from 'vue';

// Reactive data properties
const type = ref('');
const option1 = ref('');
const option2 = ref('');
const option3 = ref('');
const option4 = ref('');
const truer = ref('True');
const falser = ref('False');
const questionText = ref('');
const selectedOption = ref('');
const userInput = ref('');
const transcript = ref('');
const isRecognizing = ref(false);
const recognition = ref(null);
const currentQuestionIndex = ref(0);
const isCorrect = ref('');
const score = ref(0);

// Questions data
const questions = ref({
  teaching: "As a zookeeper, it's important to be able to communicate with visitors and colleagues in Spanish to ensure the safety and well-being of the animals under your care. One key phrase you can learn is '¿Dónde está el elefante?' which means 'Where is the elephant?' This phrase can help you locate animals and provide information to visitors.",
  assessment: {
    questions: [
      {
        question: "¿Dónde está el elefante? translates to:",
        choices: [
          "How are you?",
          "Where is the elephant?",
          "What time is it?",
          "Who is that?"
        ],
        answer: "Where is the elephant?",
        type: "multipleChoiceOptions"
      },
      {
        question: "Tigre is the Spanish word for 'lion'.",
        answer: false,
        type: "trueOrFalse"
      },
      {
        question: "Monkeys are commonly found in zoos around the world.",
        answer: true,
        type: "trueOrFalse"
      },
      {
        question: "What is the Spanish word for 'giraffe'?",
        answer: "jirafa",
        type: "shortAnswer"
      },
      {
        question: "Which animal is 'el oso' in Spanish?",
        choices: [
          "Elephant",
          "Bear",
          "Zebra",
          "Lion"
        ],
        answer: "Bear",
        type: "speach"
      }
    ],
    answers_explanation: {
      "question_1": "The correct translation of '¿Dónde está el elefante?' is 'Where is the elephant?' This phrase can help you locate specific animals.",
      "question_2": "The statement is false. 'Tigre' in Spanish translates to 'tiger', not 'lion'.",
      "question_3": "The statement is true. Monkeys are commonly found in zoos around the world as part of the animal exhibits.",
      "question_4": "The Spanish word for 'giraffe' is 'jirafa'.",
      "question_5": "'El oso' in Spanish refers to a 'bear'."
    }
  }
});

console.log(questions.value);

function getQuestion() {
    fetch('http://localhost:8000/createassessment', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            speak: "English",
            learn: "Spanish",
            job: "Painter",
            score: score.value
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error("Error fetching questions:", data.error);
            return;
        }
        questions.value = JSON.parse(data);
        console.log(questions.value);
        console.log(typeof questions.value);
        renderQuestion(questions.value.assessment.questions[currentQuestionIndex.value]);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

// Get initial questions
onMounted(() => {
    getQuestion();
});

// Speech synthesis function
function speak(text) {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = 'en-US';
    speech.rate = 1;
    speech.pitch = 1;
    speech.volume = 1;
    window.speechSynthesis.speak(speech);
}

// Speech recognition functions
function toggleRecognition() {
    if (isRecognizing.value) {
        stopRecognition();
    } else {
        startRecognition();
    }
}

function startRecognition() {
    recognition.value = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.value.lang = 'en-US';
    recognition.value.interimResults = false;
    recognition.value.maxAlternatives = 1;

    recognition.value.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        transcript.value = transcript;
    };

    recognition.value.onerror = (event) => {
        console.error("Error: ", event.error);
    };

    recognition.value.start();
    isRecognizing.value = true;
}

function stopRecognition() {
    if (recognition.value) {
        recognition.value.stop();
        isRecognizing.value = false;
    }
}

// Render functions
function renderMultipleChoiceOptions(question) {
    type.value = 'multipleChoiceOptions';
    questionText.value = question.question;
    [option1.value, option2.value, option3.value, option4.value] = question.choices;
}

function renderTrueOrFalse(question) {
    type.value = 'trueOrFalse';
    questionText.value = question.question;
}

function renderShortAnswer(question) {
    type.value = 'shortAnswer';
    questionText.value = question.question;
}

function renderSpeach(question) {
    type.value = 'speach';
    questionText.value = question.question;
    speak(question.question);
}

// Main function to render questions
function renderQuestion(question) {
    resetInputs();
    if (question.type === 'multiple choice') {
        renderMultipleChoiceOptions(question);
    } else if (question.type === 'true or false') {
        renderTrueOrFalse(question);
    } else if (question.type === 'short answer') {
        renderShortAnswer(question);
    } else if (question.type === 'speach') {
        renderSpeach(question);
    }
}

// Function to check if the answer is correct
function checkAnswer() {
    const currentQuestion = questions.value.assessment.questions[currentQuestionIndex.value];
    let correct = false;

    if (currentQuestion.type === 'multipleChoiceOptions') {
        const selectedText = [option1.value, option2.value, option3.value, option4.value][parseInt(selectedOption.value.replace('option', '')) - 1];
        correct = selectedText === currentQuestion.answer;
    } else if (currentQuestion.type === 'trueOrFalse') {
        correct = (selectedOption.value === 'truer' && currentQuestion.answer === true) ||
                  (selectedOption.value === 'falser' && currentQuestion.answer === false);
    } else if (currentQuestion.type === 'shortAnswer') {
        correct = userInput.value.toLowerCase() === currentQuestion.answer.toLowerCase();
    } else if (currentQuestion.type === 'speach') {
        correct = transcript.value.toLowerCase().includes(currentQuestion.answer.toLowerCase());
    }

    if (correct) {
        isCorrect.value = "Correct";
        score.value++;
    } else {
        isCorrect.value = "Incorrect: " + questions.value.assessment.answers_explanation["question_" + (currentQuestionIndex.value + 1)];
        if (score.value > 0) {
            score.value--;
        }
    }
}

// Function to move to the next question
function nextQuestion() {
    if (currentQuestionIndex.value < questions.value.assessment.questions.length - 1) {
        currentQuestionIndex.value++;
        renderQuestion(questions.value.assessment.questions[currentQuestionIndex.value]);
    } else {
        alert('You have completed all questions! Fetching new ones...');
        getQuestion();
    }
}

// Function to reset inputs
function resetInputs() {
    selectedOption.value = '';
    userInput.value = '';
    transcript.value = '';
    isCorrect.value = '';
}

// onMounted(() => {
//     renderQuestion(questions.value.assessment.questions[currentQuestionIndex.value]);
// });
</script>

<template>
    <div class="learn-view">
        <div class="teaching-section">
            <h1>Study material</h1>
            <div id="teaching-text">
                <p v-for="sentence in questions.teaching.split('. ')" :key="sentence">{{ sentence }}.</p>
            </div>
        </div>

        <div class="question-section-container">
            <div class="question-section"> 
                <h1>Questions</h1>
                <div id="questionText">{{ questionText }}</div>

                <div id="answers">
                    <!-- Multiple Choice Options -->
                    <div v-if="type === 'multipleChoiceOptions'">
                        <div 
                            class="multipleChoiceO" 
                            v-for="(option, index) in [option1, option2, option3, option4]" 
                            :key="index"
                            :class="{ selected: selectedOption === 'option' + (index + 1) }"
                            @click="selectedOption = 'option' + (index + 1)"
                        >
                            <label>{{ option }}</label>
                        </div>
                    </div>

                    <!-- True or False -->
                    <div v-if="type === 'trueOrFalse'">
                        <div 
                            class="multipleChoiceO" 
                            :class="{ selected: selectedOption === 'truer' }"
                            @click="selectedOption = 'truer'"
                        >
                            <label>{{ truer }}</label>
                        </div>
                
                        <div 
                            class="multipleChoiceO" 
                            :class="{ selected: selectedOption === 'falser' }"
                            @click="selectedOption = 'falser'"
                        >
                            <label>{{ falser }}</label>
                        </div>
                    </div>
                    
                    <!-- Short Answer -->
                    <div v-if="type === 'shortAnswer'">
                        <input class="shortAnswer" type="text" v-model="userInput" placeholder="Your answer...">
                    </div>

                    <!-- Speech Recognition -->
                    <div v-if="type === 'speach'">
                        <button id="record" @click="toggleRecognition">
                            {{ isRecognizing ? 'Stop Recognition' : 'Start Recognition' }}
                        </button>
                        <div>{{ transcript }}</div>
                    </div>

                    <div>
                        <h1>{{ isCorrect }}</h1>
                    </div>
                </div>
            </div>

            <div class="button-section">
                <button id="submitQuestion" @click="checkAnswer">Submit</button>
                <button id="nextQuestion" @click="nextQuestion">Next</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.teaching-section {
    width: 35%;
    height: 800px;
    background-color: #f2e2bd;
    border: solid 1px black;
    border-right: solid 2px black;
    padding: 15px;
}

.question-section {
    width: 97%;
    height: 765px;
    border: solid 1px black;
    padding-left: 3%;
    border-right: none;
    border-left: none;
    padding-top: 15px;
    background-color: #d8c598;
}

.question-section-container {
    width: 65%;
}

.learn-view {
    display: flex;
    justify-content: space-around;
    font-size: 20px;
}

.button-section {
    height: 50px;
    width: 100%;
    display: flex;
    background-color: #E1BE6A;
}

.button-section button {
    background-color: #363d3600;
    color: #40B0A6;
    padding: 5px 32px;
    text-decoration: none;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border: solid #40B0A6 2px;
    border-radius: 2px;
}

.button-section button:hover {
    background-color: #40B0A6;
    color: white;
}

#submitQuestion {
    margin-left: 45%;
}

#nextQuestion {
    float: left;
    margin-left: 34%;
}

#questionText {
    margin-bottom: 20px;
    word-spacing: 3px;
}

.teaching-section {
    padding: 15px;
    font-size: .9em;
}

#teaching-text {
    font-size: .95em;
}

#teaching-text p {
    white-space: pre-line;
    word-spacing: 4px;
}

.multipleChoiceO {
    margin-bottom: 10px;
    border: 1px solid black;
    width: 80%;
    padding: 3.5%;
    cursor: pointer;
}

.multipleChoiceO:hover {
    background-color: #40B0A6;
    color: white;
}

.selected {
    background-color: #40B0A6;
    color: white;
}

.shortAnswer {
    width: 80%;
    padding: 10px;
    margin-top: 10px;
    font-size: 20px;
    border: none;
    border-bottom: solid 1px black;
    background-color: #d8c59800;
}

#record {
    background-color: #40B0A6;
    color: white;
    padding: 10px 10px;
    text-decoration: none;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border: none;
    border-radius: 2px;
    margin-bottom: 15px;
}

#record:hover {
    background-color: #363d36;
}
</style>