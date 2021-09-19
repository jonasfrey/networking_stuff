
var make_xhr = function(header_size_characters, url ){
    let xhr = new XMLHttpRequest();
    
    xhr.open('GET', ((url) ? url : window.location.href));
    
    var header_prop = "";
    
    for(var j = 0; j<header_size_characters-1; j++){
    header_prop += "1"
    
    }
    xhr.setRequestHeader(header_prop, "1");
    xhr.send();
    
    // the response is {"message": "Hello, world!"}
    xhr.onload = function() {
      let responseObj = xhr.response;
      console.log(responseObj); // Hello, world!
    };
    }