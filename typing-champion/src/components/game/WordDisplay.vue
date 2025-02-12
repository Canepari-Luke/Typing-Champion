<template>
    <div class="word-display">
      {{ word }}
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    word: {
      type: String,
      required: true,
    },
  });
  </script>
  
  <style scoped>
  .word-display {
    font-size: 2em; /* Adjust as needed */
    font-weight: bold;
    margin-bottom: 10px;
  }
  </style>