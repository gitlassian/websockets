
document.addEventListener("DOMContentLoaded", () => {
    const log = document.getElementById("log");
    const button = document.querySelector('[name=button]')
    const input = document.querySelector('[name=message_input]')

    let websocket = new WebSocket("ws://localhost:8765");

    websocket.onopen = () => {
        button.onclick = () => {
            websocket.send(input.value)
            input.value = ""
        }
    }

    websocket.onmessage = (message) => {
        log.innerHTML = log.innerHTML + "<pre>" + message.data + "</pre>";
    }
    websocket.onclose = (event) => {
        console.log("WebSocket connection closed: ", event);
    };
}, false)