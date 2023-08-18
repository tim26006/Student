function randomText()
{

    var text = ("абвгдеёжзиклмнопрстюяэйцушщхъь0123456789")
    letter = text[Math.floor(Math.random() * text.length)];
    return letter;
}



function rain()
{

    let cloud = document.querySelector('.cloud');
    let e = document.createElement( 'div' );
    let left = Math.floor(Math.random() * 300);
    let size = Math.random() * 2;

    e.classList.add('text');
    cloud.appendChild(e);
    e.innerText = randomText();
    e.style.left = left+"px";
    e.style.fontSize = 0.5+size+'em';


    setTimeout(function(){
     cloud.removeChild(e)

    },2000)
}

setInterval(function(){

   rain ()

}, 100);