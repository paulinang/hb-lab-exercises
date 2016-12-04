"use strict";


// PART 1: SHOW A FORTUNE

function showFortune(evt) {

    // TODO: get the fortune and show it in the #fortune-text div
    $.get("/fortune", function (results) {
        $('#fortune-text').html(results);
    });
}

// function replaceFortune(results) {
//     var fortune = results;
//     $('#fortune-text').html(fortune);
// }

// function showFortune(evt) {
//     $.get('/fortune', replaceFortune);
// }

$('#get-fortune-button').on('click', showFortune);


// PART 2: SHOW WEATHER

// function replaceWeather(json_weather) {
//     var forecast = json_weather.forecast;
//     $('#weather-info').html(forecast);
// }

function showWeather(evt) {
    evt.preventDefault();

    var url = "/weather.json?zipcode=" + $("#zipcode-field").val();

    // TODO: request weather with that URL and show the forecast in #weather-info
    // $.get(url, replaceWeather);

    $.get(url, function (json_weather) {
        $("#weather-info").html(json_weather.forecast);
        // To get temp + json_weather.temp
    });
}

$("#weather-form").on('submit', showWeather);




// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    // TODO: show the result message after your form
    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}

$("#order-form").on('submit', orderMelons);


