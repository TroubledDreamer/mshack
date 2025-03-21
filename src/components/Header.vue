
<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();


function goBack() {
    router.back();
}



</script>

<template>

    <div>
        <button @click="goBack()"><-</button>
        <h1>header</h1>
    </div>
</template>