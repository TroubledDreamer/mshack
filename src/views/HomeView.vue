<script setup> 
import Stats from '../components/Stats.vue'

import { useRouter } from 'vue-router';

const router = useRouter();

function StartLearning() {
    router.push({ name: 'Learn' });
    console.log('Start Learning');
}


function Support() {
    router.push({ name: 'Support' });
    console.log('Support');
}
</script>

<template>

  <div class="homeContainer">

    <button class="homeButtons" @click="StartLearning()">Start Learning</button>

    <Stats />


    <button class="homeButtons" @click="Support()">Support</button>

  </div>


</template>


<style scoped>

.homeButtons {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}






</style>