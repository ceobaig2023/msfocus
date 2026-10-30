// MS Focus - shared behaviour
(function () {
  // Footer year
  document.querySelectorAll(".year").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Mobile menu
  var menuBtn = document.getElementById("menu-btn");
  var navLinks = document.getElementById("nav-links");
  if (menuBtn && navLinks) {
    menuBtn.addEventListener("click", function () {
      var open = navLinks.classList.toggle("active");
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.textContent = open ? "\u2715" : "\u2630";
    });
  }

  // Institutions dropdown
  document.querySelectorAll(".has-sub > button.drop").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var li = btn.parentElement;
      var open = li.classList.toggle("open");
      btn.setAttribute("aria-expanded", String(open));
    });
  });
  document.addEventListener("click", function () {
    document.querySelectorAll(".has-sub.open").forEach(function (li) {
      li.classList.remove("open");
      li.querySelector("button.drop").setAttribute("aria-expanded", "false");
    });
  });

  // Enquiry form: opens the visitor's email app with the message filled in.
  var form = document.getElementById("enquiry-form");
  if (form) {
    var interest = new URLSearchParams(location.search).get("interest");
    var select = document.getElementById("interest");
    if (interest && select) {
      Array.prototype.forEach.call(select.options, function (o) {
        if (o.value === interest) select.value = interest;
      });
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var subject = "Enquiry: " + f.get("interest");
      var body =
        "Name: " + f.get("name") + "\n" +
        "Email: " + f.get("email") + "\n" +
        "Phone: " + (f.get("phone") || "-") + "\n\n" +
        f.get("message");
      var status = document.getElementById("form-status");
      status.textContent = "Opening your email app. If nothing opens, email focus3to12@gmail.com directly.";
      window.location.href =
        "mailto:focus3to12@gmail.com?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);
    });
  }
})();
