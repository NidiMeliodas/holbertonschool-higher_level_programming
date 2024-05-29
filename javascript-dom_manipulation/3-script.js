document.getElementById("toggle_header").addEventListener("click", toggleColour)

function toggleColour() {
  const header = document.querySelector("header");
  header.classList.toggle("red");
  header.classList.toggle("green");
}