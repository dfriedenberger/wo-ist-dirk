


var game = undefined

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}
  
function init_next_game(levels) {
    
    game = {
        keys : []
    }

    const keys = Object.keys(cards);

    while(game.keys.length < 10 && keys.length > 0) {
        var ix = getRandomInt(keys.length)
        elm_id = keys.splice(ix, 1)[0];

        if (levels.includes(cards[elm_id].level)) {
            game.keys.push(elm_id)
        } 
    }

    console.log(game)

}

function init_card() {

    id = game.keys[0]


    $("#front_text").html(cards[id].text)

    $("#statistics").text(game.keys.length+"/10")

    var flip = $("#card").data("flip-model");

    // TODO , eleganter lösen (Back-Content setzen, wenn Frontseite vollständig sichtbar ist)
    if(flip.isFlipped)
    {
        $("#card").flip(false);
        $("#card").on('flip:done',function(){
            $("#back_text").html(cards[id].translation)
        })
    }
    else
    {
        $("#back_text").html(cards[id].translation)
    }

}




function next_card(again) {


    id = game.keys.shift()
    if (again) {
        game.keys.push(id)
    }

    if (game.keys.length > 0) {
        init_card()
    } else {
        //New Game
        $("#new_game").show('slow')
    }
}

$( document ).ready(function() {

    console.log( "play ready!" );

    $("#card").flip();


    $("#result-button-again").click(function(ev){
        ev.preventDefault()
        next_card(true)
    })
    
    $("#result-button-easy").click(function(ev){
        ev.preventDefault()
        next_card(false)
    })



    $(".next_test").click(function(ev){
        ev.preventDefault()
        level = $(this).data("level").split(",")
        $("#new_game").hide('slow')
        init_next_game(level)
        init_card()
    })

    $("#new_game").hide(0)
    init_next_game(["A1","A2"])
    init_card()
});