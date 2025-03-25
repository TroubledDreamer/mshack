
<script setup>
import { ref } from 'vue';
let vocabulary = ref(100);
let pronunciation = ref(0);
let grammar = ref(8);
let writing = ref(5);


</script>


<template>
    <div class="stats">
        <div class="skillTitle">Skill Levels
            <hr>
        </div>

        <div id="statsBlockContainer">
            <div class="statsBlock">
                <div>Vocabulary:</div> 
                <div class="loader">
                    <div class="progress" :style="{ width: vocabulary + '%' }"></div>
                </div>
                <div>{{ vocabulary }}%</div>
            </div>

            <div class="statsBlock">
                <div>Pronunciation:</div> 
                <div class="loader">
                    <div class="progress" :style="{ width: pronunciation + '%' }"></div>
                </div>
                <div>{{ pronunciation }}%</div>
            </div>

            <div class="statsBlock">
                <div>Grammar:</div> 
                <div class="loader">
                    <div class="progress" :style="{ width: grammar + '%' }"></div>
                </div>
                <div>{{ grammar }}%</div>
            </div>

            <div class="statsBlock">
                <div>Writing:</div> 
                <div class="loader">
                    <div class="progress" :style="{ width: writing + '%' }"></div>
                </div>
                <div>{{ writing }}%</div>
            </div>
        </div>
    </div>
</template>


<style scoped>

#statsBlockContainer {
    background-color: whitesmoke;
    width: 400px;
    padding: 10px;
    border-radius: 10px;
}

.statsBlock {
    display: flex;
    align-items: center;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}

.statsBlock div {
    margin-right: 10px;
}

.loader {
    flex: 1;
    height: 15px;
    background: #ddd;
    border-radius: 5px;
    overflow: hidden;
    position: relative;
}

.progress {
    height: 100%;
    background: linear-gradient(90deg, gold, gold);
    transition: width 0.5s ease-in-out;
}

.stats {
    background-color: rgb(255, 255, 255);
    padding: 15px;
    border-radius: 25px;
    height: 200px;
    border: solid 1.5px black;
  
}


.skillTitle {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}
</style>
