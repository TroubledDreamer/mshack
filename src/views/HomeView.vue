<script setup> 
import Stats from '../components/Stats.vue'
import { ref } from 'vue';

import { useRouter } from 'vue-router';

let language = ref('English');

const router = useRouter();

function StartLearning() {
    router.push({ name: 'Learn' });
    console.log('Start Learning');
}


function Support() {
    router.push({ name: 'Support' });
    console.log('Support');
}

function Profile() {
    router.push({ name: 'Profile' });
    console.log('Profile');
}
</script>

<template>

  <div class="home">
    
    <!-- <div  class="homeContainer"> -->

    <div class="homeButtonsContainer">

      <button class="homeButtons" @click="StartLearning()">Start Learning</button>

      <button class="homeButtons" @click="Support()">Support</button>

      <button class="homeButtons" @click="Profile()">Profile</button>

    </div>


    <Stats class="statss" />

    <div class="langauge">
      <div class="langaugeTitle">Language
      

      </div>  <hr>
      <div class="languageText">{{ language }}</div>
    </div>



  <!-- </div> -->
</div>

</template>


<style scoped>

.homeButtons {
    background-color: #40b0a700;
    border: solid 1px black;
    color: black;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: block;
    font-size: 25px;
    cursor: pointer;
    width: 100%;
    height: 100px;
    border-radius: 2px;
    border-top: none;
    border-right: none;
    border-bottom: none;
    border: none;
    font-weight: bold;

}

.homeButtons:hover {
    background-color: #40b0a7;
    border-left: solid 3px black;
}

.homeButtonsContainer {
  width: 380px;
  background-color: white;
  display: inline;
  margin-right: 150px;
  margin-left: 100px;
  margin-top: 100px;
  height: 300px;
  padding: 30px;
  border-radius: 25px;
  border: solid 1.5px black;
}


/* .stats {
  width: 300px;
  display: block;
} */

.home {
  display: flex;
  height: 80vh;
  background-color: #e2cfa4;

}

.homeContainer {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #E1BE6A;
  border: none;
  padding: 20px;
  width: 90%;
}

.statss {
  margin-top: 100px;
  margin-right: 50px;
}

.langauge {
  margin-top: 100px;
  background-color: white;
  padding: 15px;
  padding-right: 150px;
  height: 90px;
  border-radius: 25px;
  border: solid 1.5px black;
  

  

}

.langaugeTitle {
  font-size: 24px;
  font-weight: bold;
  width: 100px;




}


.languageText {
  font-size: 18px;
  font-weight: bold;
  padding-top: 7px;


}

.langauge hr {
  width: 100px;
}

</style>