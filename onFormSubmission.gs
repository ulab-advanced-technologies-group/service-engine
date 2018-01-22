function onFormSubmission(e) {
  var url = 'http://ulab.berkeley.edu/service-engine'; 
  var itemResponses = e.response.getItemResponses();
  var data = {}
  for (var i = 0; i < itemResponses.length; i++) {
    var itemResponse = itemResponses[i];
    var title = itemResponse.getItem().getTitle();
    var response = itemResponse.getResponse();
    data[i] = response;
  }
  var options = {
    'method': 'post',
    'contentType': 'application/json',
    "payload": JSON.stringify(data)
  };
  var response = UrlFetchApp.fetch(url, options);
}
