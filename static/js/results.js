$(document).ready(function () {
    $("#mydatatable tfoot th").each(function () {
        var title = $(this).text();
        $(this).html('<input type="text" placeholder="Filtrar.." />');
    });

    //Un div para destacar/indicar el ordenamiento solicitado en el *.pdf
    $("div.toolbar").html('<ul class="list-inline">' +
        '<li class="list-inline-item"><span class="badge badge-warning">Sobre los datos</span></li>' +
        '<li class="list-inline-item"><b>Ordenado por:</b> Nombre - </li>' +
        '<li class="list-inline-item"><b>Icono verde:</b> muestra mas datos del item - </li>' +
        '<li class="list-inline-item"><b>Icono API\'s:</b> es un hipervinculo </li></ul>');

    //Inicializo DataTables
    var table = $("#mydatatable").DataTable({
        dom: 'B<"float-left"l><"float-center"i><"float-right"f>t<"bottom"lp><"float-center"i><"clear">',
        responsive: true,
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.10.21/i18n/Spanish.json",
        },
        order: [
            [0, "asc"]
        ],
        initComplete: function () {
            this.api()
                .columns()
                .every(function () {
                    var that = this;

                    $("input", this.footer()).on("keyup change", function () {
                        if (that.search() !== this.value) {
                            that.search(this.value).draw();
                        }
                    });
                });
        },
        buttons: ["csv", "excel", "pdf"],
        pagingType: "full_numbers"
    });
});