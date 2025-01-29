const words = [
    "apple", "banana", "grape", "orange", "pear", "peach", "cherry", "melon", "plum", "mango", 
    "kiwi", "pineapple", "watermelon", "lemon", "grapefruit", "peach", "apricot", "lychee", "fig", 
    "jackfruit", "papaya", "Batman", "Bruce Wayne", "Star Wars", "Superman", "Clark Kent"
  ];
  
  const poem = [
    "The woods are lovely, dark and deep,",
    "But I have promises to keep,",
    "And miles to go before I sleep,",
    "And miles to go before I sleep."
  ];
  
  const wordDisplay = document.getElementById("word-display");
  const input = document.getElementById("input");
  const startButton = document.getElementById("start-button");
  const result = document.getElementById("result");
  
  let currentWord = "";
  let currentIndex = 0; // Tracks position in the word challenge
  let currentPoemIndex = 0; // Tracks position in the poem
  let lives = 3; // Player's lives
  let gameInProgress = false;
  let isPoemChallenge = false; // Flag to indicate if we are in the poem challenge
  
  function startGame() {
    // Reset the game state
    result.textContent = "";
    currentIndex = 0;
    currentPoemIndex = 0;
    lives = 3;
    gameInProgress = true;
    input.disabled = false;
    input.value = "";
    isPoemChallenge = false;
  
    // Start with the word challenge
    displayNextWord();
  }
  
  function displayNextWord() {
    if (currentIndex < words.length && !isPoemChallenge) {
      currentWord = words[currentIndex]; // Set the current word or phrase
      wordDisplay.textContent = currentWord; // Display the word
      input.value = ""; // Clear the input field
      input.focus(); // Focus on the input field
    } else {
      // End of the word challenge, start the poem challenge
      isPoemChallenge = true;
      displayNextPoemLine();
    }
  }
  
  function displayNextPoemLine() {
    if (currentPoemIndex < poem.length) {
      currentWord = poem[currentPoemIndex]; // Set the current line of the poem
      wordDisplay.textContent = currentWord; // Display the poem line
      input.value = ""; // Clear the input field
      input.focus(); // Focus on the input field
    } else {
      endGame(); // Player finished the poem (Boss fight complete)
    }
  }
  
  function checkInput() {
    if (!gameInProgress) return;
  
    const userInput = input.value.trim();
    if (userInput === currentWord) {
      result.textContent = "Correct!";
      result.style.color = "green";
      input.value = ""; // Clear the input for the next round
      
      if (isPoemChallenge) {
        currentPoemIndex++; // Move to the next line of the poem
        displayNextPoemLine();
      } else {
        currentIndex++; // Move to the next word in the word challenge
        displayNextWord();
      }
    } else if (userInput.length >= currentWord.length) {
      result.textContent = "Wrong! Try Again!";
      result.style.color = "red";
      input.value = ""; // Clear the input for retry
  
      // Handle life loss
      lives--;
      if (lives <= 0) {
        endGame(false); // End game if the player has lost all lives
      } else {
        result.textContent += ` Lives remaining: ${lives}`;
      }
    }
  }
  
  function endGame(success = true) {
    gameInProgress = false;
    input.disabled = true;
  
    if (success) {
      wordDisplay.textContent = "You've completed the challenge!";
      result.textContent = "Congratulations!";
      result.style.color = "blue";
    } else {
      wordDisplay.textContent = "Game Over!";
      result.textContent = "You ran out of lives!";
      result.style.color = "red";
    }
  }
  
  startButton.addEventListener("click", () => {
    startGame();
  });
  
  input.addEventListener("input", checkInput);
  