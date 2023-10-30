let dragged;

document.addEventListener("drag", function (event) {
  event.preventDefault();
}, false);

document.addEventListener(
  "dragstart",
  function (event) {
    dragged = event.target;
    event.target.style.opacity = 0.5;
  },
  false
);

document.addEventListener(
  "dragend",
  function (event) {
    event.target.style.opacity = "";
  },
  false
);

document.addEventListener(
  "dragover",
  function (event) {
    event.preventDefault();
  },
  false
);

document.addEventListener(
  "dragenter",
  function (event) {
    if (event.target.className == "card") {
      event.target.style.background = "#2e88cc";
    }
  },
  false
);

document.addEventListener(
  "dragleave",
  function (event) {
    if (event.target.className == "card") {
      event.target.style.background = "";
    }
  },
  false
);

document.addEventListener(
  "drop",
  function (event) {
    event.preventDefault();
    if (event.target.className == "card") {
      event.target.style.background = "";
      // Меняем местами элементы в DOM
      const parent = event.target.parentNode;
      const placeholder = document.createElement("div");
      parent.insertBefore(placeholder, dragged);
      parent.insertBefore(dragged, event.target);
      parent.replaceChild(event.target, placeholder);
    }
  },
  false
);
