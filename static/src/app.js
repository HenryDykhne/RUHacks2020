$("document").ready(function(){

    $.ajax({
        type: 'get',            //Request type
        dataType: 'json',       //Data type - we will use JSON for almost everything 
        url: '/test',   //The server endpoint we are connecting to
        success: function (data) {
            /*  Do something with returned object
                Note that what we get is an object, not a string, 
                so we do not need to parse it on the server.
                JavaScript really does handle JSONs seamlessly
            */
            console.log(data); 

        },
        fail: function(error) {
            // Non-200 return, do something with error
            console.log(error); 
        }
    });

    function getEvents(id){
        $.ajax({
            type: 'POST',           //Request type
            dataType: 'json',      //Data type - we will use JSON for almost everything 
            url: '/getEvents',   //The server endpoint we are connecting to
            data: {'userID':id},
            success: function (data) {
                console.log(data); 
                return data;
            },
            fail: function(error) {
                // Non-200 return, do something with error
                console.log(error); 
            }
        });
    }

    console.log(getEvents("userID"));
});

