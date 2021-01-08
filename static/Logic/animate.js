let typeArray = ["Disease Dictionary", "Search By Category", "Search By Name"];
const typedIndex = document.querySelector(".text");
const typeDelay = 200;
const eraseDelay = 100;
const nextText = 1000;
let charIndex = 0;
let arrayIndex = 0;

function type() {
  if (charIndex < typeArray[arrayIndex].length) {
    typedIndex.textContent += typeArray[arrayIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, typeDelay);
  } else {
    setTimeout(erase, nextText);
  }
}

function erase() {
  if (charIndex > 0) {
    typedIndex.textContent = typeArray[arrayIndex].substring(0,charIndex - 1);
    charIndex--;
    setTimeout(erase, eraseDelay);
  } else {
    arrayIndex++;
    if (arrayIndex >= typeArray.length) {
      arrayIndex = 0;
    }
    setTimeout(type, typeDelay + 1100);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  // On DOM Load initiate the effect
   setTimeout(type, nextText + 250);
});
