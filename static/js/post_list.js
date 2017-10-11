/**
 * Created by rolee on 2017-10-10.
 */

function sortTable(cIndex) {
        var table, rows, switching, i, x, y, shouldSwitch;
        table = document.getElementById("post_table");
        if (table !== null)
            console.log("Table is found");
        switching = true;
        while (switching) {
            switching = false;
            rows = table.getElementsByTagName("TR");
            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("TD")[cIndex];
                y = rows[i+1].getElementsByTagName("TD")[cIndex];

                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i+1], rows[i]);
                switching = true;
            }
        }
    }