"use strict";

const fn = {
    crawlWeb : function () {
        let _url = "/craw";

        $.ajax({
            type: "POST",
            url : _url,
            async : false
        }).done(function(data, status){
            fn.crawCallback(data, status);
        });

    },
    crawCallback : function (data, status) {
        if(status == 'success'){
            $('#searchBtn').css('display', 'none');
            $('#topListDisplay').html(data);
        } else {
            alert("Fail")
        }
    }
}