//document.getElementById("message").innerHTML="Fuccumean"
const randomNumber = Math.floor(Math.random() * 100 ) +1;
//console.log(randomNumber)
let attempt = 0;

function checkGuess(){
    const guess = parseInt(document.getElementById("guessField").value)
    attempt++;
    if(isNaN(guess) || guess < 1 || guess > 100){
        setMessage("Please enter a valid number between 1 and 100")
        return;
    }
    if(guess === randomNumber){
        setMessage("Congratulations!!")
        document.getElementById("guessField").disabled = true;
    }else if(guess < randomNumber){
        setMessage("Too low, try again")
    }else{
        setMessage("Too high, try again")
    }
}
function setMessage(message){
    document.getElementById("message").textContent = message
}
