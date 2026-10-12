(function () {
    var saved = localStorage.getItem("regweb-theme");
    document.documentElement.setAttribute(
        "data-theme",
        saved === "light" || saved === "dark" ? saved : "light"
    );
})();
