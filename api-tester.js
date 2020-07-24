const AWS = require('aws-sdk');
const dynamodb = AWS.DynamoDB(region:'us-west-2', apiVersion:'2012-08-10');
const table = 'Ingredients';

const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const xhr = new XMLHttpRequest(),
    method = "POST",
    // url = "https://00q70ys3xc.execute-api.us-west-2.amazonaws.com/dev/grocerylist/''";
    url = "https://00q70ys3xc.execute-api.us-west-2.amazonaws.com/dev/ingredients"
xhr.open(method, url, true);
xhr.onreadystatechange = function () {
  // In local files, status is 0 upon success in Mozilla Firefox
  if(xhr.readyState === 4) { // 0 unsent, 1 opened, 2 headers received, 3 loading, 4 done.
    var status = xhr.status;

    if (status === 0 || (status >= 200 && status < 400)) {
      // The request has been completed successfully
      console.log(`status: ${status}, response: ${xhr.responseText}`);
    }
    else
    {
      console.log(`status: ${status}, response: ${xhr.responseText}`);
      // Oh no! There has been an error with the request!
    }
  }
};
let ingredient = {
  name:"Lamb",
  type:"Meat",
  color:"red",
}

xhr.send(JSON.stringify(ingredient));

/*
let XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
let xhr = new XMLHttpRequest();
xhr.open('GET',
'https://00q70ys3xc.execute-api.us-west-2.amazonaws.com/dev/grocerylist/all');

xhr.onreadystatechange = function(event){
  console.log(event);
}
xhr.setRequestHeader('Content-type', 'application/json');
xhr.send();
*/
