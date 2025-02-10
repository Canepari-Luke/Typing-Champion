<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'; // Import useRouter

const router = useRouter(); // Get the router instance

const selectedLevel = ref(1);
const levels = ref([1, 2, 3, 4, 5]);

const startGame = () => {
  const gameUrl = `/game?level=${selectedLevel.value}`; // Construct game URL (still needed)
  router.push(gameUrl); // Use router.push for navigation
};
</script>

<template>
  <div class="play-widget">
    <div class="instructions">
      <h2>How to Play</h2>
      <ul>
        <li>Type the words that appear on the screen as quickly and accurately as possible.</li>
        <li>The faster and more accurate you are, the higher your score!</li>
        <li>Challenge yourself with different levels!</li>
      </ul>
    </div>
    <div class="play-button">
      <button @click="startGame">Play</button>
    </div>
    <div class="level-selector">
      <label for="level">Level:</label>
      <select v-model="selectedLevel" id="level">
        <option v-for="level in levels" :key="level" :value="level">
          {{ level }}
        </option>
      </select>
    </div>
  </div>
</template>

<style scoped>
.play-widget {
  display: flex; /* Arrange items horizontally */
  align-items: center; /* Vertically center items */
  justify-content: center; /* Horizontally center items */
  padding: 20px;
  border: 1px solid #ccc; /* Optional border */
  border-radius: 5px; /* Optional rounded corners */
  margin-bottom: 20px; /* Space below the widget */
}

.instructions {
  text-align: left;
  margin-right: 20px; /* Space between instructions and button */
}

.play-button {
  margin-right: 20px; /* Space between button and level selector */
}

.level-selector {
  display: flex; /* Arrange label and select horizontally */
  align-items: center;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #4CAF50; /* Green */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

select {
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
</style>