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
  <div>

    <button @click="StartLearning()">Start Learning</button>

    <Stats />


    <button @click="Support()">Support</button>

  </div>
</template>