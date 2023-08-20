function hideElementByClass(className) {
  var element = document.querySelector("." + className);
  if (element) {
    element.style.opacity = "0";
  }
}


document.getElementById('load').addEventListener('submit', function() {
    var loaderOverlay = document.getElementById('loader-overlay');
    var element = document.querySelector(".content");
    element.style.background = "rgba( 255, 255, 255, 0.8)"; // Пример изменения цвета текста
    loaderOverlay.style.display = 'flex';

    hideElementByClass("form-control");
    hideElementByClass("btn");
    hideElementByClass("img_gpt");
    hideElementByClass("text_gen");


});

