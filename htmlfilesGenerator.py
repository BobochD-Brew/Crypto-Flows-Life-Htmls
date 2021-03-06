for k in range(512):
    f = open(str(k)+".html", "w")
    f.write(""" 
    <!DOCTYPE html><html lang="en"><head>
        <script src="https://bobochd-brew.github.io/Crypto-Flows-Life-Htmls/p5.js"></script>
        <link rel="stylesheet" type="text/css" href="https://bobochd-brew.github.io/Crypto-Flows-Life-Htmls/style.css">
        <meta charset="utf-8">

    </head>
    <body>
        <main>
        </main>
        <script>
            let sizex = Math.min(innerWidth,innerHeight);
            let sizey = Math.min(innerWidth,innerHeight);
            let rows = 11;

            let id = """+str(k)+""";
            let state = [];
            let cleanState = [];
            let interval;
            let playing = true;
            let stateList = []
            let updateF = ()=>{
                if(!check(state,nextState(state)))  {
                    stateList.push(copyState(state))
                    state = nextState(state)
                    drawState(state)
                }else{
                    stateList.push(copyState(state))
                    state = [];
                    for(let i = 0; i < rows ; i++){
                        state.push([])
                        for(let j = 0; j < rows ; j++){
                        state[i].push(0)
                        }
                    }
                    let idString = id.toString(2)
                    for(let i = 0; i < (9-id.toString(2).length);i++){
                        idString = "0"+idString;
                    }
                    for(let i = 0; i < idString.length;i++){
                        if(idString[i] == '1'){
                        squarex = i % 3;
                        squarey = int(i/3)
                        state[(rows-3)/2 + squarex][(rows-3)/2 + squarey] = 1
                        }
                    }
                    drawState(state)
                }
            }

            function setup() {
            
            createCanvas(sizex, sizey);
            state = [];
            for(let i = 0; i < rows ; i++){
                state.push([])
                for(let j = 0; j < rows ; j++){
                state[i].push(0)
                }
            }
            for(let i = 0; i < rows ; i++){
                cleanState.push([])
                for(let j = 0; j < rows ; j++){
                cleanState[i].push(0)
                }
            }
            let idString = id.toString(2)
            for(let i = 0; i < (9-id.toString(2).length);i++){
                idString = "0"+idString;
            }
            for(let i = 0; i < idString.length;i++){
                if(idString[i] == '1'){
                squarex = i % 3;
                squarey = int(i/3)
                state[(rows-3)/2 + squarex][(rows-3)/2 + squarey] = 1
                }
            }
            drawState(state)
            interval = setInterval(updateF,1000)
            } 
            function check(state1,state2){
            for(let i = 0; i < rows ; i++){
                for(let j = 0; j < rows ; j++){
                if(state1[i][j] != state2[i][j]) return false
                }
            }
            return true;
            }
            function keyPressed() {
            if (keyCode === DOWN_ARROW && stateList.length != 0) {
                state = stateList.pop();
                drawState(state)
            } else if (keyCode === UP_ARROW && !check(state,nextState(state))) {
                updateF()
            }else if (keyCode === 80) {
                if(playing){
                clearInterval(interval)
                playing = false
                }else{
                interval = setInterval(updateF,1000)
                playing = true
                }
            }
            
            }
            function copyState(stateToCopy){
                let newState = [];
            for(let i = 0; i < rows ; i++){
                newState.push([])
                for(let j = 0; j < rows ; j++){
                newState[i].push(0)
                }
            }
            for(let i = 0; i < rows ; i++){
                for(let j = 0; j < rows ; j++){
                newState[i][j] = stateToCopy[i][j];
                }
            }
            return newState;
            }
            function drawState(stateToDraw) {
            background(10);
            stroke(255)
            for(let i = 0; i<rows+1;i++){
                line(i*(sizex)/rows,0,i*(sizex/rows),sizey)
            }
            for(let i = 0; i<rows+1;i++){
                line(0,i*(sizey)/rows,sizex,i*(sizey/rows))
            }
            for(let i = 0; i < rows ; i++){
                for(let j = 0; j < rows ; j++){
                if(state[i][j] == '1'){
                    rect((i)*(sizex/rows),(j)*(sizey/rows),(sizex/rows),(sizey/rows))
                }
                }
            }

            }
            function windowResized() {
                sizex = Math.min(innerWidth,innerHeight);
                sizey = Math.min(innerWidth,innerHeight);
                resizeCanvas(sizex, sizey);
            }
            function nextState(stateToUpdate){
            let newState = [];
            for(let i = 0; i < rows ; i++){
                newState.push([])
                for(let j = 0; j < rows ; j++){
                newState[i].push(0)
                }
            }
            for(let i = 0; i < rows ; i++){
                for(let j = 0; j < rows ; j++){
                let s = 0;
                for(let k = 0; k < 9 ; k++){
                    let x = i-1+(k%3)
                    let y = j-1+int(k/3)
                    if(k != 4 && x >= 0 && x < rows && y >= 0 && y < rows){
                    if(stateToUpdate[x][y] == 1) s+= 1;
                    }
                }
                if(stateToUpdate[i][j] == 0 && s == 3){
                    newState[i][j] = 1
                }else if(stateToUpdate[i][j] == 1 && (s > 3 || s < 2)){
                    newState[i][j] = 0
                }else{
                    newState[i][j] = stateToUpdate[i][j];
                }
                }
            }
            return newState;
            }
        </script>
    </body></html>
    """)
    f.close()
