<script setup>
import { ref } from 'vue';

// Reactive data properties
let type = ref('');
let option1 = ref('');
let option2 = ref('');
let option3 = ref('');
let option4 = ref('');
let truer = ref('True');
let falser = ref('False');
let questionText = ref('');
let selectedOption = ref(''); // For radio buttons
let userInput = ref(''); // For text input
let transcript = ref(''); // For speech recognition
let isRecognizing = ref(false); // For speech recognition
let recognition = ref(null); // Speech recognition instance
let correctAnswer = ref('');
let currentQuestionIndex = ref(0); // Track the current question index
let isCorrect = ref('');
let currentSection = ref('teaching'); // Track the current section (teaching or questions)


// Questions data
let questions = {
  "teaching": "As a zookeeper, it's important to be able to communicate with visitors and colleagues in Spanish to ensure the safety and well-being of the animals under your care. One key phrase you can learn is '¿Dónde está el elefante?' which means 'Where is the elephant?' This phrase can help you locate animals and provide information to visitors.",
  "assessment": {
    "questions": [
      {
        "question": "¿Dónde está el elefante? translates to:",
        "choices": [
          "How are you?",
          "Where is the elephant?",
          "What time is it?",
          "Who is that?"
        ],
        "answer": "Where is the elephant?",
        "type": "multipleChoiceOptions"
      },
      {
        "question": "Tigre is the Spanish word for 'lion'.",
        "answer": false,
        "type": "trueOrFalse"
      },
      {
        "question": "Monkeys are commonly found in zoos around the world.",
        "answer": true,
        "type": "trueOrFalse"
      },
      {
        "question": "What is the Spanish word for 'giraffe'?",
        "answer": "jirafa",
        "type": "shortAnswer"
      },
      {
        "question": "Which animal is 'el oso' in Spanish?",
        "choices": [
          "Elephant",
          "Bear",
          "Zebra",
          "Lion"
        ],
        "answer": "Bear",
        "type": "multipleChoiceOptions"
      }
    ],
    "answers_explanation": {
      "question_1": "The correct translation of '¿Dónde está el elefante?' is 'Where is the elephant?' This phrase can help you locate specific animals.",
      "question_2": "The statement is false. 'Tigre' in Spanish translates to 'tiger', not 'lion'.",
      "question_3": "The statement is true. Monkeys are commonly found in zoos around the world as part of the animal exhibits.",
      "question_4": "The Spanish word for 'giraffe' is 'jirafa'.",
      "question_5": "'El oso' in Spanish refers to a 'bear'."
    }
  }
};

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
        const trans = event.results[0][0].transcript;
        transcript.value = trans; // Store the transcript
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
    questionText.value = question.question;
    option1.value = question.choices[0] || '';
    option2.value = question.choices[1] || '';
    option3.value = question.choices[2] || '';
    option4.value = question.choices[3] || '';
}

function renderTrueOrFalse(question) {
    questionText.value = question.question;
    truer.value = 'True';
    falser.value = 'False';
}

function renderShortAnswer(question) {
    questionText.value = question.question;
}

function renderSpeach(question) {
    questionText.value = question.question;
    speak(question.question);
}

function renderSpeakRespond(question) {
    questionText.value = question.question;
    speak(question.question);
}

// Main function to render questions
function renderQuestion(question) {
    type.value = question.type;
    if (question.type === 'multipleChoiceOptions') {
        renderMultipleChoiceOptions(question);
    } else if (question.type === 'trueOrFalse') {
        renderTrueOrFalse(question);
    } else if (question.type === 'shortAnswer') {
        renderShortAnswer(question);
    } else if (question.type === 'speach') {
        renderSpeach(question);
    } else if (question.type === 'speakRespond') {
        renderSpeakRespond(question);
    }
}

// Function to check if the answer is correct
function checkAnswer() {
    const currentQuestion = questions.assessment.questions[currentQuestionIndex.value];

    if (currentQuestion.type === 'multipleChoiceOptions') {
        const selectedValue = selectedOption.value;
        if (selectedValue === 'option1' && option1.value === currentQuestion.answer) {
            isCorrect.value = "Correct";
        } else if (selectedValue === 'option2' && option2.value === currentQuestion.answer) {
            isCorrect.value = "Correct";
        } else if (selectedValue === 'option3' && option3.value === currentQuestion.answer) {
            isCorrect.value = "Correct";
        } else if (selectedValue === 'option4' && option4.value === currentQuestion.answer) {
            isCorrect.value = "Correct";
        }
    } else if (currentQuestion.type === 'trueOrFalse') {
        if (selectedOption.value === 'truer' && currentQuestion.answer === true) {
            isCorrect.value = "Correct";
        } else if (selectedOption.value === 'falser' && currentQuestion.answer === false) {
            isCorrect.value = "Correct";
        }
    } else if (currentQuestion.type === 'shortAnswer') {
        if (userInput.value.toLowerCase() === currentQuestion.answer.toLowerCase()) {
            isCorrect.value = "Correct";
        }
    } else if (currentQuestion.type === 'speach' || currentQuestion.type === 'speakRespond') {
        if (transcript.value.toLowerCase().includes(currentQuestion.answer.toLowerCase())) {
            isCorrect.value = "Correct";
        }
    }

    if (isCorrect.value === "Correct") {
        isCorrect.value = "Correct";
    } else {
        isCorrect.value = "Incorrect : " + questions.assessment.answers_explanation["question_" + (currentQuestionIndex.value + 1)];
    }
}

// Function to move to the next section or question
function nextSection() {
    if (currentSection.value === 'teaching') {
        // Move to the questions section
        currentSection.value = 'questions';
        renderQuestion(questions.assessment.questions[currentQuestionIndex.value]);
    } else if (currentSection.value === 'questions') {
        // Move to the next question
        if (currentQuestionIndex.value < questions.assessment.questions.length - 1) {
            currentQuestionIndex.value++;
            resetInputs();
            renderQuestion(questions.assessment.questions[currentQuestionIndex.value]);
        } else {
            alert('You have completed all questions!');
        }
    }
}

// Function to reset inputs
function resetInputs() {
    selectedOption.value = '';
    userInput.value = '';
    transcript.value = '';
    isCorrect.value = '';
}
</script>
<template>
    <div>
        <!-- Teaching Section -->
        <div v-if="currentSection === 'teaching'">
            <h1>Teaching</h1>
            <div>{{ questions.teaching }}</div>
            <button @click="nextSection">Next</button>
        </div>

        <!-- Questions Section -->
        <div v-if="currentSection === 'questions'">
            <h1>Questions</h1>
            <div>{{ questionText }}</div>

            <div id="answers">
                <!-- Multiple Choice Options -->
                <div v-if="type === 'multipleChoiceOptions'">
                    <div v-for="(option, index) in [option1, option2, option3, option4]" :key="index">
                        <input 
                            type="radio" 
                            :id="'option' + (index + 1)" 
                            :value="'option' + (index + 1)" 
                            v-model="selectedOption" 
                            name="choices" 
                        />
                        <label :for="'option' + (index + 1)">{{ option }}</label>
                    </div>
                </div>

                <!-- True or False -->
                <div v-if="type === 'trueOrFalse'">
                    <div>
                        <input 
                            type="radio" 
                            id="truer" 
                            value="truer" 
                            v-model="selectedOption" 
                            name="choices" 
                        />
                        <label for="truer">{{ truer }}</label>
                    </div>
                    <div>
                        <input 
                            type="radio" 
                            id="falser" 
                            value="falser" 
                            v-model="selectedOption" 
                            name="choices" 
                        />
                        <label for="falser">{{ falser }}</label>
                    </div>
                </div>

                <!-- Short Answer -->
                <div v-if="type === 'shortAnswer'">
                    <input type="text" v-model="userInput" placeholder="Your answer...">
                </div>

                <!-- Speech Recognition -->
                <div v-if="type === 'speach' || type === 'speakRespond'">
                    <button @click="toggleRecognition">{{ isRecognizing ? 'Stop Recognition' : 'Start Recognition' }}</button>
                    <div>{{ transcript }}</div>
                </div>

                <!-- Feedback -->
                <div>
                    <h1>{{ isCorrect }}</h1>
                </div>

                <!-- Submit Button -->
                <button @click="checkAnswer">Submit</button>

                <!-- Next Button -->
                <button @click="nextSection">Next</button>
            </div>
        </div>
    </div>
</template>