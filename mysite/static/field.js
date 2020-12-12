const { CENTER } = require("./p5");

function setup() {
    createCanvas(windowWidth, windowHeight, WEBGL);
}

function draw() {
    field();
}

function field() {
    background(0, 24, 4);
    stroke('rgb(169, 253, 34)');
    strokeWeight(1);
    rotateX(1000);
    box(3 * windowWidth / 4, 3 * windowHeight / 4, 0);
    circle(0, 0, 3 * windowHeight / 16);
    line(0, -3 * windowHeight / 8, 0, 3 * windowHeight / 8);

    //left soccer field
    //corners
    arc(-3 * windowWidth / 8, -3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, 0, HALF_PI);
    arc(-3 * windowWidth / 8, 3 * windowHeight / 8, windowHeight / 16, windowHeight / 16, -HALF_PI, 0);
    //half circle on goal
    arc(-9 * windowWidth / 32, 0, windowHeight / 8, windowHeight / 8, -PI / 2, PI / 2);
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


// var t1 = gsap.timeline();
gsap.from("h1.homepage-text", { duration: 1, opacity: 0.3 });