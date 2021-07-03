/* MODAL */
function onClick(element) {
    modal = document.getElementById("myModal");
    modalImg = document.getElementById("img01");
    captionText = document.getElementById("caption");
    modal.style.display = "block";
    modalImg.src = element.src;  
    //captionText.innerHTML = element.alt;
  
}