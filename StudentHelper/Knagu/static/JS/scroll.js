document.addEventListener('DOMContentLoaded', function () {
  const scrollContainer = document.getElementById('content');
  let isMouseDown = false;
  let startX;
  let scrollLeft;

  scrollContainer.addEventListener('mousedown', (e) => {
    isMouseDown = true;
    startX = e.pageX - scrollContainer.offsetLeft;
    scrollLeft = scrollContainer.scrollLeft;
  });

  scrollContainer.addEventListener('mouseleave', () => {
    isMouseDown = false;
  });

  scrollContainer.addEventListener('mouseup', () => {
    isMouseDown = false;
  });

  scrollContainer.addEventListener('mousemove', (e) => {
    if (!isMouseDown) return;


    if (Math.abs(e.pageX - startX) > 5) {
      e.preventDefault();
      const x = e.pageX - scrollContainer.offsetLeft;
      const walk = (x - startX) * 1.4;
      scrollContainer.scrollLeft = scrollLeft - walk;
    }
  });


});
