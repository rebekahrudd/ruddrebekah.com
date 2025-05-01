// Get the hamburger icon and menu elements
const hamburger = document.getElementById("hamburger");
const menu = document.getElementById("menu");
const myName = document.getElementById("name");
console.log("here");

// Add a click event listener to the hamburger icon
// hamburger.addEventListener("click", function () {
//   // Toggle the 'menu' visibility by adding/removing the 'show' class
// });

const menuButton = document.getElementById("menu-button");
const navMenu = document.querySelector("header nav h1 a");

menuButton.addEventListener("click", function () {
  this.classList.toggle("active");
  // console.log("this runs")
  menu.style.display = menu.style.display === "block" ? "none" : "block";
  // navMenu.style.display = navMenu.style.display === "none" ? "block" : "none";
  myName.style.display = myName.style.display === "none" ? "block" : "none";
});
