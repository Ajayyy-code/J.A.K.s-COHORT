window.onload = function(){


    let orderp = document.getElementById("orderp").firstChild.nodeValue;    //Grabs the time the order was placed
    let eta = document.getElementById("eta").firstChild.nodeValue;      //Grabs the estimated time of the order
    let timestuff; //AM or PM value
    let totaletaH; //New estimated time hours
    let totaletaM; //New estimated time Minutes
    let totaleta; // New estimated time in Seconds
    let hr24; //Hours in 24 Hours


    

    
    //Changes estimated time to integer
    inteta = parseInt(eta);

    let orderptime = orderp;

    if (orderptime.includes("p.m.")){

        orderptime = orderp.replace('p.m.',"");
        orderptime = orderptime.split(":");
        timestuff = ("p.m.");


    } 

    else if(orderptime.includes("a.m.")){


        orderptime = orderp.replace('a.m.',"");
        orderptime = orderptime.split(":");
        timestuff = ("a.m.");

    }
    //If the time has no minutes 
    if (orderptime.length == 1) {
        
        orderptime.push('0');
        
    }
    //If the time goes from AM to PM
    if (orderptime[0] == 11 && orderptime[1] + (inteta / 60) > 60 && timestuff.includes("a.m.")){

        
        timestuff = ("p.m.");




    }
    //If the time goes from PM to AM
    else if (orderptime[0] == 11 && orderptime[1] + (inteta / 60) > 60 && timestuff.includes("p.m.")){

        timestuff = ("a.m.");
        
    }


  

    //Changes the time the order was placed into seconds
    secorderp = (((orderptime[0] * 60) * 60) + (orderptime[1] * 60));
    //The new time in seconds
    totaleta = secorderp + inteta;

   

    
    if (totaleta % 60 == 0){

        totaleta = totaleta / 60;
        //If time goes from 12 to 1
        if ((Math.trunc(totaleta / 60)) > 12) {
            totaeltaH = (Math.trunc(totaleta / 60) - 12);
        }

        else {
            totaletaH = (Math.trunc(totaleta / 60));
        }
        totaletaM = totaleta % 60;
        

    }

    else {

        totaleta = Math.trunc(totaleta / 60);
        //If time goes from 12 to 1
        if ((Math.trunc(totaleta / 60)) > 12 ){
            totaletaH = (Math.trunc(totaleta / 60) - 12);
        }
        else{
            totaletaH = (Math.trunc(totaleta / 60));
        }
        totaletaM = totaleta % 60;


    }

    


    let strtotalH = totaletaH.toString(); 
    let strtotalM = totaletaM.toString();

    if (strtotalM.length < 2 ){

        strtotalM = "0" + strtotalM; 
    }
    //Creates the new time in Hours and minutes
    let neweta = (strtotalH + ":" + strtotalM + " " + timestuff);
    //Appends the new time to the landing page
    document.getElementById("eta").innerHTML = (neweta);

    if (timestuff.includes('p.m')){
        hr24 = parseInt(orderptime[0]) + 12; //Turn the hours into 24 hour time
    }

    
    if (timestuff.includes('a.m')){
        hr24 = parseInt(orderptime[0]);
    }


    let Day = new Date().getDate();
    let Month = new Date().getMonth();
    let Year = new Date().getFullYear();
    
    // Set the date order was made

    let downdate = new Date(Year,Month,Day,hr24,orderptime[1]).getTime();

    // Set the date we're counting down to 
    let countDownDate;


    countDownDate = (downdate + inteta*1000);

    // Update the count down every 1 second
    let x = setInterval(function() {

    // Get today's date and time
    let now = new Date().getTime();
        
    // Find the distance between now and the count down date
    let distance = countDownDate - now;
        
    // Time calculations for minutes and seconds
    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
    // Shows the timer in an element with id="timer"
    if(seconds<10){
        document.getElementById("timer").innerHTML = minutes + " : 0" + seconds;
    } else {
        document.getElementById("timer").innerHTML = minutes + " : " + seconds;
    }
        
    // When the timer has ran out displays a message 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("timer").innerHTML = "Your Order is Arriving Late";
    }
    }, 1000);
    
}