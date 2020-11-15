var searchIcon = document.getElementsByClassName("search-box__icon")[0];
var searchBox = document.getElementsByClassName("search-box")[0];

searchIcon.addEventListener("click", activateSearch);

function activateSearch() {
  searchBox.classList.toggle("active");
}

var modal = document.getElementById("myModal");

var img = document.getElementById("myImg");
var modalImg = document.getElementById("photo");
var captionText = document.getElementById("caption");
img.onclick = function () {
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

var span = document.getElementsByClassName("close")[0];

span.onclick = function () {
  modal.style.display = "none";
}
