// _static/turtini-banner.js
(function () {
  const banner = document.createElement("div");
  banner.className = "turtini-banner";
  banner.innerHTML =
    '<strong>Turtini Docs</strong> — Federal-focused guidance for secure, governed delivery. ' +
    '<span style="opacity:.9">Questions? </span>' +
    '<a href="https://turtini.com/contact" target="_blank" rel="noopener">Contact us</a>.';

  // Insert banner at the top of the content wrapper
  const body = document.querySelector("body");
  if (body) body.prepend(banner);
})();
