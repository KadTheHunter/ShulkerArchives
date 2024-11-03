---
permalink: /database-v1/
title: v1 Archive Entry Database
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
#database > tfoot > tr > th > select {
background-color: rgb(37,42,52);
color: rgb(143,146,150)
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

This database is for the v1.0.0-v1.4.0 releases.
If you are using a newer release (v2.0.0 or later), please refer to the [v2 Database]({{ site.baseurl }}/database/) instead.
{: .notice--danger .text-center}
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
jQuery(document).ready(function($) {
    $('#database').DataTable({
        ajax: '{{ site.baseurl }}/assets/database-v1.json',
        dom: "lrtip",
        order: [
            [0, 'asc']
        ],
        initComplete: function() {
            this.api().columns().every(function() {
                let column = this;
                let title = column.footer().textContent;
                let input = document.createElement('input');
                input.placeholder = title;
                column.footer().replaceChildren(input);
                input.addEventListener('keyup',() => {
                        if (column.search() !== this.value) {
                            column.search(input.value).draw();
                        }
                    });
            });
            this.api().columns([4, 5]).every(function() {
                let column = this;
                let select = document.createElement('select');
                let title = column.header().textContent;
                select.id = title.split(' ').map((word, index) => index === 0 ? word.toLowerCase() : word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join('');
                select.add(new Option(title, ''));
                column.footer().replaceChildren(select);
                select.addEventListener('change', function() {
                    column.search(select.value, {
                        exact: true
                    }).draw();
                });
                column.data().unique().sort().each(function(d, j) {
                    select.add(new Option(d));
                });
                let firstOption = select.querySelector('option:first-child');
                firstOption.style.fontWeight = 'bold';
            })
        }
    });
});
</script>
<script>
document.addEventListener("keydown", function(event) {
    if (event.target.tagName.toLowerCase() === 'input' && event.target.type === 'text' || event.target.tagName.toLowerCase() === 'textarea' || event.target.isContentEditable) {}
    else {
        if (event.key === "ArrowLeft") {
            document.querySelector(".previous").click();
        }
        else if (event.key === "ArrowRight") {
            document.querySelector(".next").click();
        }
    }
});
</script>