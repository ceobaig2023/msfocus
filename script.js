// MS Focus - shared behaviour (menu and dropdown are handled by Bootstrap)
(function () {
  // Footer year
  document.querySelectorAll(".year").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Enquiry form: opens the visitor's email app with the message filled in.
  var form = document.getElementById("enquiry-form");
  if (!form) return;

  var interest = new URLSearchParams(location.search).get("interest");
  var select = document.getElementById("interest");
  if (interest && select) {
    Array.prototype.forEach.call(select.options, function (o) {
      if (o.value === interest) select.value = interest;
    });
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    form.classList.add("was-validated");
    if (!form.checkValidity()) return;

    var f = new FormData(form);
    var subject = "Enquiry: " + f.get("interest");
    var body =
      "Name: " + f.get("name") + "\n" +
      "Email: " + f.get("email") + "\n" +
      "Phone: " + (f.get("phone") || "-") + "\n\n" +
      f.get("message");
    document.getElementById("form-status").textContent =
      "Opening your email app. If nothing opens, email focus3to12@gmail.com directly.";
    window.location.href =
      "mailto:focus3to12@gmail.com?subject=" + encodeURIComponent(subject) +
      "&body=" + encodeURIComponent(body);
  });
})();
