<template>
    <div class="level-display">
      Level: {{ level }}
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    level: {
      type: Number,
      required: true,
    },
  });
  </script>
  
  <style scoped>
  /* Style your level display */
  </style>