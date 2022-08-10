$(document).ready(function () {

//    On click of the submit button call the function to generate new Be like Bill
    $("#blkgen").click(function(){
        generate_belike();
    });
    $('#Lovegen').click(function () {
        //generate_belike();
        love_cal();
    });

//    Function responsible for gettin user input values and refreshing the page content with updated content.
    function generate_belike() {

        var name = $('#name').val();
        var gender = $("#gender").val();
        var current_url = $(location).attr('href');
        console.log(name);
        csrf = $('input[name="csrfmiddlewaretoken"]').val()

        $.ajax({
            url: current_url,
             type: "POST",
             dataType: "json",
             data: {
                'name':name,
                'gender':gender,
                'csrfmiddlewaretoken':csrf
             },
             success : function (data) {
                url = 'https://belikebill.ga/billgen-API.php?default=1&name='+data.name+'&sex='+data.gender ;
                console.log(url);
                $("#srcapi").attr('src',url);

                      }
             });
    };


    function love_cal(){
        $("#percentage_bar").attr('style', "width:" + 0 + "%");
        $("#msg").text('Lets start the test...!')
        var fname = $('#fname').val();
        var sname = $("#sname").val();
        const settings = {
            "async": true,
            "crossDomain": true,
            "url": "https://love-calculator.p.rapidapi.com/getPercentage?fname=" + fname + "&sname=" + sname,
            "method": "GET",
            "headers": {
                "x-rapidapi-key": "ec61d573b4msh9603f02cff2f574p1bacd9jsn512e6a7c23e5",
                "x-rapidapi-host": "love-calculator.p.rapidapi.com"
            },
        };

        $.ajax(settings).done(function (response) {
            console.log(response);
            var percent = parseInt(response.percentage);
            var msg = response.result
            $("#percentage_bar").attr('style', "width:" + percent+"%");
            if (percent < 50){
                if ($("#percentage_bar.progress-bar-success").length){
                    $("#percentage_bar").removeClass("progress-bar-success");
                }
                $("#percentage_bar").addClass("progress-bar-danger");
            }
            else{
                if ($("#percentage_bar.progress-bar-danger").length){
                    $("#percentage_bar").removeClass("progress-bar-danger");
                }
                $("#percentage_bar").addClass("progress-bar-success");
            }
            $('#percentage').text(percent+"%")
            $("#msg").text(msg)
        });
    }
//    to add active class on nav items
    var path = location.pathname.split("/")[1];
    //    console.log(path)
    if(path != ""){
        $('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');
    }else{
        $('nav a[href="/"').addClass('active');
    }

});
