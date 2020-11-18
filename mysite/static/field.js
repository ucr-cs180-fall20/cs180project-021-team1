const { CENTER } = require("./p5");
let button;

function setup() {
    createCanvas(windowWidth, windowHeight, WEBGL);
    //  if (window.open()){
    //      
    // }

    // rotateX(millis() / 1000);
    // rotateY(millis() / 1000);
}

function draw() {
    // shearZ(20);
    // button = createButton(<a class="button-link">Search</a>);
    // button.position(19, 19);
    // button.mousePressed(href = "{% url 'search' %}");

    background(0, 24, 4);
    stroke('rgb(169, 253, 34)');
    strokeWeight(3);
    box(3 * windowWidth / 4, 3 * windowHeight / 4, 0);
    circle(0, 0, 3 * windowHeight / 16);
    line(0, -3 * windowHeight / 8, 0, 3 * windowHeight / 8);
    //left soccer field
    //corners
    arc(-3 * windowWidth / 8, -3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, 0, HALF_PI);
    arc(-3 * windowWidth / 8, 3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, -HALF_PI, 0);
    //half circle on goal
    arc(-9 * windowWidth / 32, 0, windowHeight / 8, windowHeight / 8, -PI / 2, PI / 2);
    //.5        .25          0         -.25       -.5
    //goal
    rect(-3 * windowWidth / 8, -3 * windowHeight / 16, 3 * windowWidth / 32, 3 * windowHeight / 8);
    rect(-3 * windowWidth / 8, -3 * windowHeight / 32, 3 * windowWidth / 128, 3 * windowHeight / 16);

    //right soccer field
    //corners
    arc(3 * windowWidth / 8, 3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, PI, -HALF_PI);
    arc(3 * windowWidth / 8, -3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, HALF_PI, PI);
    //half circle on goal
    arc(9 * windowWidth / 32, 0, windowHeight / 8, windowHeight / 8, PI / 2, -PI / 2);
    //goal
    rect(9 * windowWidth / 32, -3 * windowHeight / 16, 3 * windowWidth / 32, 3 * windowHeight / 8);
    rect(45 * windowWidth / 128, -3 * windowHeight / 32, 3 * windowWidth / 128, 3 * windowHeight / 16);


    noFill();


}
