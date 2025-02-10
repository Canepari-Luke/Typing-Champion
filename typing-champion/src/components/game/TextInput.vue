<template>
    <input type="text" v-model="currentInput" @keyup.enter="handleEnter">
  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue';
  
  const emit = defineEmits(['textInput', 'enterPressed']);
  
  const currentInput = ref('');
  
  const handleInput = () => {
    emit('textInput', currentInput.value);
  };
  
  const handleEnter = () => {
    emit('enterPressed', currentInput.value);
    currentInput.value = ''; // Clear input field
  };
  </script>
  
  <style scoped>
  /* Style your input field here */
  </style>