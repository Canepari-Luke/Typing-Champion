<template>
    <div class="life-display">
      Lives: {{ lives }}
      <span v-for="n in lives" :key="n" class="heart">❤</span>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    lives: {
      type: Number,
      required: true,
    },
  });
  </script>
  
  <style scoped>
  .life-display {
    /* Style your life display */
    color: red;
  }
  .heart {
      font-size: 1.2em;
  }
  </style>
  