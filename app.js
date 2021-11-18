window.onload = function (){
    
    let coll = document.getElementsByClassName("collapsible");
    let i;

    
for (i = 0; i < coll.length; i++) {

    coll[i].addEventListener("click", function(e) {
        e.preventDefault();
      console.log(this.parentElement.parentElement.nextElementSibling);
      let content = this.parentElement.parentElement.nextElementSibling;
      if (content.style.display === "block") {
        content.style.display = "none";
      } else {
        content.style.display = "block";
      }
    });
  }
}


