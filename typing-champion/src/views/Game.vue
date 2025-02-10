// views/Game.vue
<template>
  <div class="game">
    <h1>Game View</h1> <GameManager :initial-level="level" />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import GameManager from '@/components/game/GameManager.vue';

const route = useRoute();
const level = parseInt(route.query.level || 1); // Get level from query, default to 1

</script>

<style scoped>
.game {
  text-align: center;
}
</style>