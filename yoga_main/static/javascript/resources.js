

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

