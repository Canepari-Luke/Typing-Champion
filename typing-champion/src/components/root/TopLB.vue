<script setup>
import { ref, onMounted } from 'vue';

// Reactive variable to store leaderboard data
const topUsers = ref([]);

// Function to fetch top 10 users from the backend
const fetchLeaderboard = async () => {
    try {
        const response = await fetch("http://localhost:8000/api/users/");
        if (!response.ok) throw new Error("Failed to fetch leaderboard data");

        const data = await response.json();
        
        // Assuming the backend returns a full list of users, we slice the top 10
        topUsers.value = data.slice(0, 10); 
    } catch (error) {
        console.error("Error fetching leaderboard:", error);
    }
};

// Fetch data when the component mounts
onMounted(fetchLeaderboard);
</script>

<template>
  <div class="leaderboard">
    <h2>🏆 Top 10 Players</h2>
    <ul>
      <li v-for="(user, index) in topUsers" :key="user.id">
        <span>#{{ index + 1 }} - {{ user.username }}</span>
        <span>Speed: {{ user.speed }} WPM | Accuracy: {{ user.accuracy }}%</span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.leaderboard {
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

li:last-child {
  border-bottom: none;
}
</style>
