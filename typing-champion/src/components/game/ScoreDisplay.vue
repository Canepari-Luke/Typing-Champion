<template>
    <div class="score-display">
      Speed: {{ speed }} WPM, Accuracy: {{ accuracy }}%
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    speed: {
      type: Number,
      required: true,
    },
    accuracy: {
      type: Number,
      required: true,
    },
  });
  </script>
  
  <style scoped>
  /* Style your score display */
  </style>