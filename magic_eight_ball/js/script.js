
function magic8ball() {
  var fortune = getafortune();
  showfortune(fortune)
}

function getafortune(){
    var fortunes = ['yes', 'no', 'maybe', '6-7']
    var random=rando(fortunes.length)
   return fortunes[random]
}
function rando(max){
    return Math.floor(Math.random() *4)
}

function showfortune(fortune) {
    document.getElementById('answer').innerHTML=fortune
}