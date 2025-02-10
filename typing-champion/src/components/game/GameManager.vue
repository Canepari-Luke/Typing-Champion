<template>
    <div class="game-manager">
      <WordDisplay :word="currentWord" />
      <TextInput @textInput="handleTextInput" @enterPressed="handleEnterPressed" />
      <LifeDisplay :lives="lives" />
      <LevelDisplay :level="level" />
      <ScoreDisplay :speed="speed" :accuracy="accuracy" />
      <ChallengeDisplay :challengeText="challengeText" :challengeActive="inChallengeMode" @lineTyped="handleLineTyped"/>
      <div v-if="gameOver">
          <h1>Game Over!</h1>
          <p>Your final score: Level {{ level -1 }}, Speed {{ speed }} WPM, Accuracy {{ accuracy }}%</p>
          <button @click="restartGame">Restart</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, defineProps, defineEmits, computed } from 'vue';
  import WordDisplay from './WordDisplay.vue';
  import TextInput from './TextInput.vue';
  import LifeDisplay from './LifeDisplay.vue';
  import LevelDisplay from './LevelDisplay.vue';
  import ScoreDisplay from './ScoreDisplay.vue';
  import ChallengeDisplay from './ChallengeDisplay.vue';
  
  const emit = defineEmits(['gameOver', 'levelComplete']);
  
  const props = defineProps({
    initialLevel: {
      type: Number,
      required: true,
    },
  });
  
  const level = ref(props.initialLevel);
  const lives = ref(3); // Starting lives, adjust per level
  const currentWord = ref('');
  const currentWordIndex = ref(0);
  const words = ref([]); // Store words for current level
  const speed = ref(0);
  const accuracy = ref(0);
  const startTime = ref(null);
  const correctChars = ref(0);
  const totalChars = ref(0);
  const challengeText = ref([]);
  const inChallengeMode = ref(false);
  const wordsPerLevel = ref(5);
  const gameOver = ref(false);
  
  const wordLists = {
  1: ["cat", "dog", "run", "fun", "sun", "hat", "bat", "rat", "fat", "mat", "sit", "hit", "bit", "kit", "lit", "wit", "zip", "tip", "rip", "dip"],
  2: ["typing", "champion", "keyboard", "mouse", "screen", "monitor", "laptop", "desktop", "internet", "browser", "website", "application", "programming", "coding", "software", "hardware", "network", "server", "database", "algorithm"],
  3: ["algorithm", "database", "programming", "javascript", "python", "vuejs", "react", "angular", "html", "css", "developer", "engineer", "software", "hardware", "network", "security", "cloud", "computing", "artificial", "intelligence"],
  // ... more levels
};
  
const challengeTexts = {
    1: ["Challenge Line 1", "Challenge Line 2"],
    2: ["Longer Challenge Line 1", "Longer Challenge Line 2"],
    3: ["Even Longer Challenge Line 1", "Even Longer Challenge Line 2", "Even Longer Challenge Line 3"],
    // ... more levels
}
  
function getWordsForLevel(level) {
  const levelWords = wordLists[level] || [];
  const minLength = level * 2;
  const maxLength = level * 4;

  const filteredWords = levelWords.filter(word => word.length >= minLength && word.length <= maxLength);
  const shuffledWords = filteredWords.sort(() => 0.5 - Math.random());

  return shuffledWords.slice(0, wordsPerLevel.value); // Limit words per level
}
  
function getChallengeText(level) {
    return challengeTexts[level] || [];
}
  
  onMounted(() => {
    loadLevelData();
  });
  
  const loadLevelData = () => {
      currentChallengeText.value = getChallengeText(level.value);
      words.value = getWordsForLevel(level.value);
      startLevel();
  }
  
  const startLevel = () => {
    currentWordIndex.value = 0;
    currentWord.value = words.value[currentWordIndex.value];
    startTime.value = Date.now();
    correctChars.value = 0;
    totalChars.value = 0;
    inChallengeMode.value = false;
  };
  
  const handleTextInput = (input) => {
    totalChars.value = input.length;
  };
  
  const handleEnterPressed = (typedWord) => {
    if (typedWord === currentWord.value) {
      correctChars.value += typedWord.length;
      currentWordIndex.value++;
  
      if (currentWordIndex.value < words.value.length) {
        currentWord.value = words.value[currentWordIndex.value];
      } else {
        inChallengeMode.value = true;
      }
  
      const endTime = Date.now();
      const timeTaken = (endTime - startTime.value) / 60000; // in minutes
      speed.value = Math.round((correctChars.value / 5) / timeTaken); // WPM
      accuracy.value = Math.round((correctChars.value / totalChars.value) * 100);
    } else {
      lives.value--;
      if (lives.value === 0) {
        gameOver.value = true;
        emit('gameOver');
      }
    }
  };
  
  const handleLineTyped = (typedLine) => {
    if (typedLine === challengeText.value[currentWordIndex.value]) {
      currentWordIndex.value++;
      if (currentWordIndex.value >= challengeText.value.length) {
        level.value++;
        loadLevelData(); // Load data for the next level
        emit('levelComplete', level.value);
      }
    } else {
      lives.value--;
      currentWordIndex.value = 0; // Restart challenge
      if (lives.value === 0) {
        gameOver.value = true;
        emit('gameOver');
      }
    }
  };
  
  const restartGame = () => {
      level.value = props.initialLevel;
      lives.value = 3;
      gameOver.value = false;
      loadLevelData();
  }
  </script>
  
  <style scoped>
  /* ... your styles */
  </style>