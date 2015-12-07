(function ($) {
  'use strict'
  $(document).ready(function () {
    $('#hCRForm').submit(function (e) {
      // Intercept Form Submission
      e.preventDefault()

      var helloSubmit = document.getElementById('hCRSubmit')
      var dataBaseUrl = document.getElementsByTagName('Body')[0].getAttribute('data-base-url')
      var authenticator = document.getElementById('hCRAuth').value

      // Specifies that the action is in progress
      helloSubmit.value = 'Loading...'
      helloSubmit.disabled = true

      $.ajax({
        async: true,
        type: 'POST',
        url: dataBaseUrl + '/helloService',
        data: { _authenticator: authenticator },
        success: function (result) {
          helloSubmit.value = 'Room available !'
          window.location.reload()
        },
        error: function (result) {
          helloSubmit.value = 'Error'
        }
      })
    })
  })
})(jQuery)
