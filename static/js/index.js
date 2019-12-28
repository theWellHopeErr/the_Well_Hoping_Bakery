function formToJSON(formObj) {
  var obj = {};
  var elements = formObj.querySelectorAll("input, select, textarea");
  for (var i = 0; i < elements.length; ++i) {
    var element = elements[i];
    var name = element.name;
    var value = element.value;
    obj[name] = value;
  }

  return JSON.stringify(obj);
}

function sign_up(e) {
  e.preventDefault()
  var body = formToJSON(this)
  var config = {
    headers: { 'Content-Type': 'application/json' },
  };
  console.log('/signup');
  
  axios.post('/signup', body, config)
    .then(function (response) {
      console.log(response);
    })
    .catch(function (err) {
      console.log(err);
    })
}

var sign_up_form = document.getElementById('signUpForm')
sign_up_form.addEventListener('submit', sign_up, false)