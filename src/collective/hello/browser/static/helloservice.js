(function () {
    "use strict";
    document.addEventListener("DOMContentLoaded", function () {
        var hCRForm = document.getElementById("hCRForm");
        if((typeof hCRForm != "undefined") && (hCRForm != null)) {
            hCRForm.addEventListener("submit", function (e) {
                // Intercept Form Submission
                e.preventDefault();

                var helloSubmit = document.getElementById("hCRSubmit");
                var dataBaseUrl = document.getElementsByTagName("Body")[0].getAttribute("data-base-url");
                var authenticator = document.getElementById("hCRAuth").value;

                // Specifies that the action is in progress
                helloSubmit.value = "Loading...";
                helloSubmit.disabled = true;

                fetch(dataBaseUrl+"/helloService", {
                	method: "POST",
                	headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                	},
                  credentials: 'same-origin',
                  body: JSON.stringify({ _authenticator: authenticator})
                }).then(function (response) {
                    helloSubmit.value = "Room available !";
                    console.log(response);
                    response.json().then(function(r) {
                        window.open("https://hello.firefox.com/" + r.roomToken);
                    });
                }).catch(function (error) {
                    helloSubmit.value = "Error";
                });

                return false;
            })
        }
    });
})();
