

function modalclick1() {
  var x = document.getElementById("element1");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function modalclick2() {
  var x = document.getElementById("element2");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function modalclick3() {
  var x = document.getElementById("element3");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}


function modalclick4() {
  var x = document.getElementById("element4");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function modalclick5() {
  var x = document.getElementById("element5");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

// Above r scripts for the intro content

function basicsButton() {
  var title = document.getElementById("titletext");
  title.innerHTML = "Yoga Basics"; 
  // change styling
  document.getElementById("yogabasics").className = "flex p-3 items-center font-medium bg-green-50 rounded text-green-500";
  document.getElementById("introductiontext").className = "flex p-3 items-center font-medium hover:bg-green-50 rounded text-gray-500 hover:text-green-500";


}


window.onload = function() {
      document.getElementById('first').className = 'show';
      document.getElementById('firsta').className = 'current';
    };
    let previous = document.getElementById("first");
    function toggle(e){
      
      let elems = document.getElementsByClassName("current");
      if (previous === document.getElementById("first")){
        console.log("hello");
        previous.classList.remove("show");
        previous.classList.add("right");
      } else {
        let previousElem = document.querySelectorAll('[aria-label="'+previous+'"]')[1];
        previousElem.classList.remove("show");
      }
      
      let aria = document.querySelectorAll('[aria-label="'+e.target.getAttribute('aria-label')+'"]');
      aria[1].classList.add("show");
      
      for (i=0;i<elems.length; i++){
      
          elems[i].classList.remove("current");

        }
        e.target.classList.add("current"); 
        console.log(e.target.getAttribute('aria-label'));
      previous=e.target.getAttribute('aria-label');
};