function openSlideMenu() {
    document.getElementById('side-menu').style.width = '250px';
    


}

function closeSlideMenu() {
    document.getElementById('side-menu').style.width = '0';
    

}

// Navigation:

const toggleButton = document.getElementById('but')
console.log(toggleButton)
const navbarlink = document.getElementById('link')
console.log(navbarlink)
toggleButton.addEventListener('click', () => {
    navbarlink.classList.toggle('active')
})

// Self Assesment:

$(document).ready(function () {
    $("#next").click(function () {
        $("#first").hide();
        $("#q1").show();
    });

    // question 1
    $("#q1b").click(function () {
        $("#q1").hide();
        $("#q2").show();
    });
    $("#q2b").click(function () {
        $("#q1").hide();
        $("#emergencyInfo").show();
    });

    // question 2
    $("#q3b").click(function () {
        $("#q2").hide();
        $("#q3").show();
    });
    $("#q4b").click(function () {
        $("#q2").hide();
        $("#q4").show();
    });

    // question 3
    $("#q5b").click(function () {
        $("#q3").hide();
        $("#unlikelySick").show();
    });

    $("#q6b").click(function () {
        $("#q3").hide();
        $("#q4").show();
    });

    // question 4
    $("#q7b").click(function () {
        $("#q4").hide();
        $("#q5").show();
    });
    $("#q8b").click(function () {
        $("#q4").hide();
        $("#callNurse").show();
    });

    // question 5
    $("#q9b").click(function () {
        $("#q5").hide();
        $("#q6").show();
    });
    $("#q10b").click(function () {
        $("#q5").hide();
        $("#callNurse").show();
    });

    // question 6
    $("#q11b").click(function () {
        $("#q6").hide();
        $("#selfIsolate").show();
    });
    $("#q12b").click(function () {
        $("#q6").hide();
        $("#callNurse").show();
    });

    $("#q2r").click(function () {
        $("#q2").hide();
        $("#q1").show();
    });
    $("#q3r").click(function () {
        $("#q3").hide();
        $("#q2").show();
    });
    $("#q4r").click(function () {
        $("#q4").hide();
        $("#q3").show();
    });
    $("#q5r").click(function () {
        $("#q5").hide();
        $("#q4").show();
    });
    $("#q6r").click(function () {
        $("#q6").hide();
        $("#q5").show();
    });
});