<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

// Reactive variable to store leaderboard data
const topUsers = ref([]);

// Helper function to process the backend data
const processData = (data) => {
    // Create an object to store the best score for each player
    const players = {};

    // Loop through the data and select the best score for each player
    data.forEach(entry => {
        const { Name, WordPerMinute, Accuracy, Level } = entry;

        // Use a unique key by combining Name and Level
        const playerKey = `${Name}-${Level}`;  // You can adjust this to use other unique fields if needed

        if (!players[playerKey] || players[playerKey].WordPerMinute < WordPerMinute) {
            players[playerKey] = { Name, WordPerMinute, Accuracy, Level };
        }
    });

    // Convert the players object to an array and sort by WordPerMinute (WPM)
    const topPlayers = Object.values(players).sort((a, b) => b.WordPerMinute - a.WordPerMinute);

    console.log("Processed Players:", topPlayers);  // Debugging line to check data

    return topPlayers;
};

// Function to fetch top 10 users from the backend
const fetchLeaderboard = async () => {
    try {
        const response = await axios.get("http://localhost:8000/api/scores/");
        
        // Log raw data to see what we are getting from the backend
        console.log("Raw Data:", response.data);

        // Process the fetched data to get the top players
        const processedData = processData(response.data);
        
        // Take the top 10 players (or fewer if there are less than 10)
        topUsers.value = processedData.slice(0, 10); 
        
        console.log("Top Users:", topUsers.value);  // Debugging line to check top players
        
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
      <li v-for="(user, index) in topUsers" :key="user.Name + '-' + user.Level">
        <span>#{{ index + 1 }} - {{ user.Name }}</span>
        <span>Speed: {{ user.WordPerMinute }} WPM | Accuracy: {{ user.Accuracy }}%</span>
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
