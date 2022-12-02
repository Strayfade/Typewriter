// ==UserScript==
// @name         Typing.com Organizer for Typewriter
// @version      1.0
// @description  Removes unnecessary elements from Typing.com and de-clutters the lesson page.
// @author       Strayfade
// @match        https://www.typing.com/student/lesson/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=typing.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    setInterval(function() {
        try {

            // Remove Header
            //document.getElementsByClassName("wrapper")[0].children[1].style.display = "none"

            document.getElementsByClassName("cell--l")[0].style.padding = "0px"
            document.getElementsByClassName("cell--l")[0].style.margin = "0px"
            document.getElementsByClassName("cell--l")[0].style.width = "100%"
            document.getElementsByClassName("cell--l")[0].style.height = "90vh"
            document.getElementsByClassName("cell--l")[0].style.maxWidth = "100%"
            document.getElementsByClassName("row row--o")[1].style.padding = "0px"

            document.getElementsByClassName("cell cell--l")[1].style.maxWidth = "100%"
            document.getElementsByClassName("screen screen--card screenBasic cell cell--l")[0].style.maxWidth = "100%"
            document.getElementsByClassName("cell js-keyboard-holder")[0].style.display = "none"

            document.getElementsByClassName("screen screen--card screenBasic cell cell--l")[0].style.maxHeight = "99999px"

            document.getElementsByClassName("structure")[0].style.maxHeight = "9999px"
            document.getElementsByClassName("structure")[0].style.height = "999px"

            // Remove Footer
            document.getElementsByTagName("footer")[0].style.display = "none"

            // Remove Tooltips
            document.getElementsByClassName("tooltip-wrapper")[0].style.display = "none"

        } catch {}
    }, 1000)
})();