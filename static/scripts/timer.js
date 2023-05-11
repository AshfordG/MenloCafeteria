//MOSTLY FROM CHAT GPT
//
//
//
const stopwatch = document.querySelector('.stopwatch');
const startBtn = document.querySelector('.start-btn');
const stopBtn = document.querySelector('.stop-btn');
const resetBtn = document.querySelector('.reset-btn');

let startTime;
let elapsedTime = 0;
let intervalId;

function startTimer() {
  startTime = Date.now() - elapsedTime;
  intervalId = setInterval(updateTimer, 10);
}

function updateTimer() {
  elapsedTime = Date.now() - startTime;
  stopwatch.textContent = formatTime(elapsedTime);
}

function formatTime(time) {
  const hours = Math.floor(time / 3600000);
  const minutes = Math.floor((time % 3600000) / 60000);
  const seconds = Math.floor((time % 60000) / 1000);
  return `${pad(hours, 2)}:${pad(minutes, 2)}:${pad(seconds, 2)}`;
}

function pad(number, length) {
  let str = `${number}`;
  while (str.length < length) {
    str = `0${str}`;
  }
  return str;
}

function stopTimer() {
  clearInterval(intervalId);
}

function resetTimer() {
  clearInterval(intervalId);
  elapsedTime = 0;
  stopwatch.textContent = '00:00:00';
}

startBtn.addEventListener('click', startTimer);
stopBtn.addEventListener('click', stopTimer);
resetBtn.addEventListener('click', resetTimer);

