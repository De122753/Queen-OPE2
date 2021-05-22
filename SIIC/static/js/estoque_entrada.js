$(document).ready(function() {
    // Insere classe no primeiro item de produto
    $('#id_estoque-0-produto').addClass('clProduto');
    $('#id_estoque-0-preco_unit').addClass('clPreco');
    $('#id_estoque-0-quantidade').addClass('clQuantidade');

    // Desabilita o primeiro campo 'Saldo'
    $('#id_estoque-0-saldo').prop('type', 'hidden');
    // Desabilita o primeiro campo 'Fabricante'
    $('#id_estoque-0-fabricante').prop('type', 'hidden');


    // Cria um span para mostrar o saldo na tela.
    $('label[for="id_estoque-0-saldo"]').append('<span id="id_estoque-0-saldo-span" class="lead" style="padding-left: 10px; color: blue; padding-right: 30px;"></span>')
        // Cria um campo com o estoque inicial.
    $('label[for="id_estoque-0-saldo"]').append('<input id="id_estoque-0-inicial" class="form-control" type="hidden" />')
    $('.clProduto').select2()

});

$('#add-item').click(function(ev) {
    ev.preventDefault();
    var count = $('#estoque').children().length;
    var tmplMarkup = $('#item-estoque').html();
    var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
    $('div#estoque').append(compiledTmpl);

    // update form count
    $('#id_estoque-TOTAL_FORMS').attr('value', count + 1);

    // Desabilita o campo 'Saldo'
    $('#id_estoque-' + (count) + '-saldo').prop('type', 'hidden');
    $('#id_estoque-' + (count) + '-fabricante').prop('type', 'hidden');

    //$('#id_estoque-' + (count) + '-DELETE').prop('type', 'hidden');

    // some animate to scroll to view our new form
    $('html, body').animate({
        scrollTop: $("#add-item").position().top - 200
    }, 800);

    $('#id_estoque-' + (count) + '-produto').addClass('clProduto');
    $('#id_estoque-' + (count) + '-preco_unit').addClass('clPreco');
    $('#id_estoque-' + (count) + '-quantidade').addClass('clQuantidade');

    // Cria um span para mostrar o saldo na tela.
    $('label[for="id_estoque-' + (count) + '-saldo"]').append('<span id="id_estoque-' + (count) + '-saldo-span" class="lead" style="padding-left: 10px; color: blue; padding-right: 30px;"></span>')
        // Cria um campo com o estoque inicial.
    $('label[for="id_estoque-' + (count) + '-saldo"]').append('<input id="id_estoque-' + (count) + '-inicial" class="form-control" type="hidden" />')
        // Select2
    $('.clProduto').select2()



});

let estoque
let saldo
let campo
let campo2
let quantidade
let preco
let campo3
let campo4

$(document).on('change', '.clProduto', function() {
    // preco_unit = $(this).val();
    let self = $(this)
    let pk = $(this).val()
    let url = '/produto/' + pk + '/json/'
    $.ajax({
        url: url,
        type: 'GET',
        enctype: 'multipart/form-data',
        success: function(response) {
            fabricante = response.data[0].fabricante
            preco_unitario = response.data[0].preco_unitario
            estoque = response.data[0].estoque
            campo3 = self.attr('id').replace('produto', 'preco_unit');
            campo4 = self.attr('id').replace('produto', 'fabricante');
            campo = self.attr('id').replace('produto', 'quantidade');
            estoque_inicial = self.attr('id').replace('produto', 'inicial');
            preco = Number(preco_unitario)
            fab = fabricante

            // Estoque inicial
            $('#' + estoque_inicial).val(estoque);
            $('#' + campo).val('');
            $('#' + campo3).val(preco.toFixed(2));
            $('#' + campo4).val(fab);


        },
        error: function(xhr) {
            // body...
        }
    })
});

$(document).on('change', '.clQuantidade', function() {
    quantidade = $(this).val();
    while (quantidade == 0) {
        alert("Informe um número maior que 0!");
        quantidade = $(this).val('');
        return quantidade;
    }
    // Aqui é feito o cálculo de soma do estoque
    saldo = Number(quantidade) + Number(estoque);
    campo = $(this).attr('id').replace('quantidade', 'saldo')
    campo_estoque_inicial = $(this).attr('id').replace('quantidade', 'inicial')
    estoque_inicial = $('#' + campo_estoque_inicial).val()
    saldo = Number(quantidade) + Number(estoque_inicial)
        // Desabilita o 'Saldo'
    $('#' + campo).prop('type', 'hidden')
        // Atribui o saldo ao campo 'saldo'
    $('#' + campo).val(saldo)
    campo2 = $(this).attr('id').replace('quantidade', 'saldo-span')
        // Atrubui o saldo ao campo 'id_estoque-x-saldo-span'
    $('#' + campo2).text(saldo)
});


$('#form').bind('submit', false);

$('button#submit').click(function() {
    $('#form').submit();
});