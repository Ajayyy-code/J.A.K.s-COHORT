window.onload = function(){

    let orderp = document.getElementById("orderp").firstChild.nodeValue;    //Grabs the time the order was placed
    let eta = document.getElementById("eta").firstChild.nodeValue;      //Grabs the estimated time of the order
    let timestuff; //AM or PM value
    let totaletaH; //New estimated time hours
    let totaletaM; //New estimated time Minutes
    let totaleta; // New estimated time in Seconds

    

    
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

}