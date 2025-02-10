<template>
    <div v-if="challengeActive">
      <h2>Final Challenge!</h2>
      <p>{{ currentLine }}</p>
      <input type="text" @keyup.enter="handleEnter" v-model="typedLine">
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps, defineEmits, watch } from 'vue';
  
  const emit = defineEmits(['lineTyped']);
  
  const props = defineProps({
    challengeText: {
      type: Array, // Or String if it's one long string
      required: true,
    },
  });
  
  const challengeActive = ref(false);
  const currentLineIndex = ref(0);
  const currentLine = ref('');
  const typedLine = ref('');
  
  watch(() => props.challengeText, (newVal) => {
    if (newVal && newVal.length > 0) {
      challengeActive.value = true;
      currentLine.value = newVal[currentLineIndex.value];
    }
  });
  
  const handleEnter = () => {
    emit('lineTyped', typedLine.value);
    typedLine.value = '';
    currentLineIndex.value++;
    if (currentLineIndex.value < props.challengeText.length) {
      currentLine.value = props.challengeText[currentLineIndex.value];
    } else {
      challengeActive.value = false; // Challenge finished
    }
  };
  </script>
  
  <style scoped>
  /* Style the challenge display */
  </style>