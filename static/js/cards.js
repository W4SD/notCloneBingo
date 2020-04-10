function decAmount() {

    var elem = document.getElementById('amount');

    if (parseInt(elem.innerHTML) > 1) {
        elem.innerHTML = parseInt(elem.innerHTML) - 1
    }

    // console.log(elem.innerHTML);
}


function addAmount() {

    var elem = document.getElementById('amount');

    if (parseInt(elem.innerHTML) < 3) {
        elem.innerHTML = parseInt(elem.innerHTML) + 1
    }
}

function generateCards() {
    var value = parseInt(document.getElementById('amount').innerHTML);


    $.ajax({
        url: '/',
        data: JSON.stringify(value),
        contentType: 'application/json;charset=UTF-8',
        type: 'POST',
        success: function (response) {
            $("#game").html(response);
            console.log(response);
            $('.game-cell').bind('click', handleCellClick);
        },
        error: function (error) {
            console.log(error);
        }
    });

    // console.log(value);
}