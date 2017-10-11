/**
 * Created by rolee on 2017-10-10.
 */
var created_date, course, username, year, name;
$(document).ready(function () {
    created_date = false;
    course = false;
    username = false;
    year = false;
    name = false;

});

function sortTable(cIndex) {
    var table, rows, switching, i, x, y, shouldSwitch, currColumn;

    switch (cIndex) {
        case 0:
            currColumn = created_date;
            created_date = !created_date;
            break;
        case 1:
            currColumn = course;
            course = !course;
            break;
        case 2:
            currColumn = username;
            username = !username;
            break;
        case 3:
            currColumn = year;
            year = !year;
            break;
        case 4:
            currColumn = name;
            name = !name;
            break;
        default:
            break;
    }

    table = document.getElementById("post_table");
    switching = true;
    while (switching) {
        switching = false;
        rows = table.getElementsByTagName("TR");
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[cIndex];
            y = rows[i + 1].getElementsByTagName("TD")[cIndex];

            if (currColumn) {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
            else {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }

        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }

}

//TODO: working on dynamic login popup


// Plugin options and our code


$(function () {
    $(".modal_trigger").leanModal({
        top: 100,
        overlay: 0.6,
        closeButton: ".modal_close"
    });
});