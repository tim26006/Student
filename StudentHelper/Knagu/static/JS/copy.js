 document.getElementById("copyButton").addEventListener("click", function() {
    var olElement = document.getElementById("myList");
    var range = document.createRange();
    range.selectNode(olElement);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);

    try {
      // Копируем выделенный текст в буфер обмена
      document.execCommand("copy");

      // Очищаем выбранные области
      selection.removeAllRanges();

      // Выводим сообщение об успешном копировании
      alert("Текст успешно скопирован!");
    } catch (err) {
      // Если копирование не удалось, выводим сообщение об ошибке
      alert("Копирование не удалось: " + err);
    }
  });