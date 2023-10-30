

    var ctx = document.getElementById('myChart').getContext('2d');
    // Данные для графика (предположим, что это оценки за разные экзамены)
    var data = {
      labels: ['Семестр 1', 'Семестр 2', 'Семестр 3', 'Семестр 4', 'Семестр 5', 'Семестр 6', 'Семестр 7', 'Семестр 8'],
      datasets: [{
        backgroundColor: 'rgba(255, 255, 255, 1)', // Цвет заливки графика
        borderColor: 'rgba(255, 255, 255, 1)', // Цвет границы графика
        borderWidth: 2,
        pointBackgroundColor: 'rgba(75, 192, 192, 1)', // Цвет точек на линии
        pointBorderColor: '#fff', // Цвет обводки точек
        pointHoverBackgroundColor: '#fff', // Цвет точек при наведении
        pointHoverBorderColor: 'rgba(75, 192, 192, 1)', // Цвет обводки точек при наведении
        data: [5.0, 4.8, 5.0], // Оценки за экзамены
      }]
    };
    // Опции графика
    var options = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: false,
          ticks: {
            stepSize: 0.1, // Шаг между метками оси Y
            fontColor: 'rgba(0, 0, 0, 1)',
             font: {
            family: 'SF Pro Display',
          },
          gridLines: {
                    color: 'rgba(255, 0, 0, 1)' // устанавливаем цвет горизонтальных линий сетки
                }// Цвет меток оси Y
          },
        },
        x: {
          ticks: {
            fontColor: 'rgba(0, 0, 0, 1)',
             font: {
            family: 'SF Pro Display',
          },// Цвет меток оси X
          },
        },
      },
      plugins: {
        legend: {
          display: false,
          labels: {
            fontColor: 'rgba(255, 255, 255, 1)', // Цвет текста легенды
            fontSize: 16,
            font: {
            family: 'SF Pro Display',
          },
        },
      },
    },
    };
    // Создание графика
    var myChart = new Chart(ctx, {
      type: 'line', // Используем линейный тип графика
      data: data,
      options: options,
}
      );