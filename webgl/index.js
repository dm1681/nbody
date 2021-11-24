

function main() {
    // get the canvas object
    const canvas = document.querySelector('#canvas');

    // get the WebGL context
    const gl = canvas.getContext('webgl');

    // if we don't have a GL context, give up now
    if (gl === null) {
        alert('Unable to initialize WebGL. Your browser or machine may not support it.');
        return;
    }


    // set clear color to black, fully opaque
    gl.clearColor(0.0, 0.0, 0.0, 1.0);

    // clear the color buffer with specified clear color
    gl.clear(gl.COLOR_BUFFER_BIT);
}

window.onload = main;