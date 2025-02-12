<script setup>
import Header from '@/components/Header.vue';
import Play from '@/components/Play.vue';
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
