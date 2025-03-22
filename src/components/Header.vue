
<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();


function goBack() {
    router.back();
}



</script>

<template>

    <div id="headerBackground">
        <button  id="backButton" @click="goBack()"><-</button>
  
    </div>
</template>


<style scoped>

#headerBackground {
    background-color: #4b4545;
    border: none;
    display: flex;
    
}


#backButton {
    background-color: #121412;
    border: none;
    color: white;
    padding: 20px 28px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
 
    cursor: pointer;
}







</style>