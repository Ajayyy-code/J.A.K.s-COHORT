window.onload = function(){

    let orderp = document.getElementById("orderp").firstChild.nodeValue;
    console.log(orderp);
    let eta = document.getElementById("eta").firstChild.nodeValue;
    let timestuff;
    let totaletaH;
    let totaletaM;
    let totaleta;

    console.log(eta);

    

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
    //If time goes from AM to PM
    if (orderptime[0] == 11 && orderptime[1] + (inteta / 60) > 60 && timestuff.includes("a.m.")){

        
        timestuff = ("p.m.");




    }
    //If time goes from PM to AM
    else if (orderptime[0] == 11 && orderptime[1] + (inteta / 60) > 60 && timestuff.includes("p.m.")){

        timestuff = ("a.m.");
        
    }



    if (orderptime[0] == 11 && orderptime[1] + (inteta / 60) > 60 && timestuff.includes("a.m.")){


        timestuff = ("p.m.");




    }

    else if (orderptime[0] == 11 && orderptime[1] + (inteta / 60) > 60 && timestuff.includes("p.m.")){

        timestuff = ("a.m.");
        
    }

    console.log(orderptime,inteta);


    secorderp = (((orderptime[0] * 60) * 60) + (orderptime[1] * 60));

    totaleta = secorderp + inteta;

    console.log(totaleta);

    
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

        if ((Math.trunc(totaleta / 60)) > 12 ){
            totaletaH = (Math.trunc(totaleta / 60) - 12);
        }
        else{
            totaletaH = (Math.trunc(totaleta / 60));
        }
        totaletaM = totaleta % 60;


    }

    console.log(totaletaH,totaletaM);


    let strtotalH = totaletaH.toString();
    let strtotalM = totaletaM.toString();

    if (strtotalM.length < 2 ){

        strtotalM = "0" + strtotalM; 
    }

    let neweta = (strtotalH + ":" + strtotalM + " " + timestuff);

    console.log(document.getElementById("eta").innerHTML = (neweta));

}