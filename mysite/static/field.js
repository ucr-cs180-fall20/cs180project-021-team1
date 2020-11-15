const { CENTER } = require("./p5");
let button;

function setup() {
    createCanvas(windowWidth, windowHeight, WEBGL);
}

function draw() {
    // shearZ(20);
    // button = createButton(<a class="button-link">Search</a>);
    // button.position(19, 19);
    // button.mousePressed(href = "{% url 'search' %}");

    background(0, 24, 4);
    stroke('rgb(169, 253, 34)');
    strokeWeight(3);
    rotateX(35);
    // rotateY(millis() / 1000);
    box(3 * windowWidth / 4, 3 * windowHeight / 4, 100);
    circle(0, 0, 3 * windowHeight / 16);
    line(0, -3 * windowHeight / 8, 0, 3 * windowHeight / 8);

    arc(-3 * windowWidth / 8, -3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, 0, HALF_PI);
    arc(-3 * windowWidth / 8, 3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, -HALF_PI, 0);
    arc(-2.2 * windowWidth / 8, 0, windowHeight / 8, windowHeight / 8, -PI / 2, PI / 2);

    rect(-3 * windowWidth / 8, -3 * windowHeight / 16, 3 * windowHeight / 16, 3 * windowHeight / 8);
    rect(-3 * windowWidth / 8, -3 * windowHeight / 32, 3 * windowHeight / 64, 3 * windowHeight / 16);

    arc(3 * windowWidth / 8, 3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, PI, -HALF_PI);
    arc(3 * windowWidth / 8, -3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, HALF_PI, PI);
    arc(2.2 * windowWidth / 8, 0, windowHeight / 8, windowHeight / 8, PI / 2, -PI / 2);
    rect(2.2 * windowWidth / 8, -3 * windowHeight / 16, 3 * windowHeight / 16, 3 * windowHeight / 8);
    rect(2.8 * windowWidth / 8, -3 * windowHeight / 32, 3 * windowHeight / 64, 3 * windowHeight / 16);


    noFill();
}