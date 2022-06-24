//initializing array for sound level history
let queue = [0,0,0,0,0,0,0,0];
function receiveVolumeLevel(websocket) {
  var volumebar ="";
  var additionalbarstyles = `font-weight:bold; font-size:20px; margin: 0;
  padding: 0;`
  websocket.addEventListener("message", ({ data }) => {
    const event = JSON.parse(data);
    //receive value from server
    console.log(event);
    volumebar="";
    for(var i = 0; i<event;i++){
      // volumebar+="|";
      //renders bars color according to volume levels
      if(i<34)
            volumebar+=`<span style="color:green; ${additionalbarstyles}">|</span>`
        if(i>=34 && i<66)
            volumebar+=`<span style="color:orange; ${additionalbarstyles}">|</span>`
        if(i>=66)
            volumebar+=`<span style="color:red; ${additionalbarstyles}">|</span>`
    }
    //puts value in queue history
    queue.push(volumebar);
    queue.shift();
    //display queue in browser
    const render = queue.map((e)=>{
        return `<p>${e}</p>`
      }
    )
    document.getElementById('leveling').innerHTML = `${render}`;
  });
}

window.addEventListener("DOMContentLoaded", () => {
  // Open the WebSocket connection and register event handlers.
  const websocket = new WebSocket("ws://localhost:8001/");
  receiveVolumeLevel(websocket);
});