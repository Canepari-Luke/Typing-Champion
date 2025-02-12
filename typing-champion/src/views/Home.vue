<script setup>
import Header from '@/components/Header.vue';
<<<<<<< HEAD
=======
import Play from '@/components/root/game/Play.vue';
>>>>>>> 4e7f83917fc51b0dc17e92cc62a54444171ffbc2
import TopLB from '@/components/root/TopLB.vue';
</script>

<template>

  <div class="home">
    <h1>Welcome, Typing Champion!</h1>
    <p>Click play to start or check the leaderboard.</p>

    
    <Play />
    <TopLB />
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 20px;
}
</style>
