---
permalink: /database/
title: Archive Entry Database
layout: single
classes: wide
---

<link href="{{ site.baseurl }}/assets/DataTables/datatables.min.css" rel="stylesheet">
<style>
th, td{
border: 1px solid rgb(61,64,70);
}
.dataTables_wrapper .dataTables_paginate .paginate_button.current, .dataTables_wrapper .dataTables_paginate .paginate_button.current:hover {
color: inherit !important;
border: 1px solid rgba(0, 0, 0, 0.3);
background: rgba(230,230,230,0.1);
}
.dataTables_wrapper .dataTables_paginate .paginate_button:hover {
border: 1px solid rgba(0, 0, 0, 0);
background: rgba(230,230,230,0.1);
}
.dataTables_wrapper .dataTables_length select {
  background-color: rgb(37,42,52);
}
.table-wrapper {
display: flex;
justify-content: center;
}
.table-wrapper table {
margin: 0 auto;
}
#page-title{
text-align: center;
}
article.page {
  float: left;
  width: 100%;
}
</style>

Want an easier way to copy the teleport command?
Firefox users: Just `CTRL+Click` and `CTRL+C` on the cell.
Chrome users: use the [CopyTables](https://github.com/gebrkn/copytables) extension.
{: .notice--info .text-center}
<div class="table-wrapper">
<table id="database" class="hover">
    <thead>
        <tr>
            <th>Name</th>
            <th>Author</th>
            <th>Teleport Command</th>
            <th>Notes</th>
            <th>Category</th>
            <th>Entry Type</th>
        </tr>
    </thead>
    <tfoot>
        <tr>
            <th>Name</th>
            <th>Author</th>
            <th>Teleport Command</th>
            <th>Notes</th>
            <th>Category</th>
            <th>Entry Type</th>
        </tr>
    </tfoot>
</table>
</div>

<script src="{{ site.baseurl }}/assets/DataTables/jQuery-3.7.0/jquery-3.7.0.min.js" type="text/javascript"></script>
<script src="{{ site.baseurl }}/assets/DataTables/datatables.min.js" type="text/javascript"></script>
<script>
$.noConflict();
  jQuery(document).ready(function( $ ) {
    $('#database').DataTable({
        ajax: '{{ site.baseurl }}/assets/database.json',
        dom: "lrtip",
        order: [[0, 'asc']],
        initComplete: function () {
        this.api()
            .columns()
            .every(function () {
                let column = this;
                let title = column.footer().textContent;
                let input = document.createElement('input');
                input.placeholder = title;
                column.footer().replaceChildren(input);
                input.addEventListener('keyup', () => {
                    if (column.search() !== this.value) {
                        column.search(input.value).draw();
                    }
                });
            });
    }
        });
    });
</script>
<script>
document.addEventListener("keydown", function(event) {
if (event.target.tagName.toLowerCase() === 'input' && event.target.type === 'text' || event.target.tagName.toLowerCase() === 'textarea' || event.target.isContentEditable) {
    } else {
    if(event.key === "ArrowLeft") {
        document.querySelector(".previous").click();
    } else if (event.key === "ArrowRight") {
        document.querySelector(".next").click();
    }
}
});
</script>