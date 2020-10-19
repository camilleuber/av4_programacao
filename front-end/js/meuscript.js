$(function() { 

    function exibir_cachorros() {
        $.ajax({
            url: 'http://localhost:5000/listar_cachorros',
            method: 'GET',
            dataType: 'json',
            success: listar, 
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend: ");
            }
        });
        function listar (cachorros) {
            $('#corpoTabelaCachorros').empty();
            mostrar_conteudo("tabelaCachorros");      
            for (var i in cachorros) { 
                lin = '<tr id="linha_'+cachorros[i].id+'">' + 
                '<td>' + cachorros[i].nome + '</td>' + 
                '<td>' + cachorros[i].genero + '</td>' + 
                '<td>' + cachorros[i].idade + '</td>' + 
                '<td>' + cachorros[i].raca + '</td>' + 
                '<td>' + cachorros[i].porte + '</td>' + 
                '<td>' + cachorros[i].cor + '</td>' + 
                '<td><a href=# id="excluir_' + cachorros[i].id + '" ' + 
                  'class="excluir_cachorro"><img src="img/excluir.png" '+
                  'alt="Excluir cachorro" title="Excluir cachorro"></a>' + 
                '</td>' + 
                '</tr>';
                $('#corpoTabelaCachorros').append(lin);
            }
        }
    }

    function mostrar_conteudo(identificador) {
        $("#tabelaCachorros").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        $("#"+identificador).removeClass('invisible');      
    }

    $(document).on("click", "#linkListarCachorros", function() {
        exibir_cachorros();
    });
    
    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoInicial");
    });

    $(document).on("click", "#btIncluirCachorro", function() {

        nome = $("#campoNome").val();
        genero = $("#campoGenero").val();
        idade = $("#campoIdade").val();
        raca = $("#campoRaca").val();
        porte = $("#campoPorte").val();
        cor = $("#campoCor").val();

        var dados = JSON.stringify({ nome: nome, genero: genero, idade: idade, raca: raca, porte: porte, cor: cor });

        $.ajax({
            url: 'http://localhost:5000/incluir_cachorro',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json', 
            data: dados, 
            success: cachorroIncluida, 
            error: erroAoIncluir
        });
        function cachorroIncluida (retorno) {
            if (retorno.resultado == "ok") { 
                alert("Cachorro incluída com sucesso!");
                $("#campoNome").val("");
                $("#campoGenero").val("");
                $("#campoIdade").val("");
                $("#campoRaca").val("");
                $("#campoPorte").val("");
                $("#campoCor").val("");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            alert("erro ao incluir dados, verifique o backend: ");
        }
    });

    $('#modalIncluirCachorro').on('hide.bs.modal', function (e) {
        if (! $("#tabelaCachorros").hasClass('invisible')) {
            exibir_cachorros();
        }
    });

    mostrar_conteudo("conteudoInicial");

    $(document).on("click", ".excluir_cachorro", function() {

        var componente_clicado = $(this).attr('id'); 
        var nome_icone = "excluir_";
        var id_cachorro = componente_clicado.substring(nome_icone.length);
        $.ajax({
            url: 'http://localhost:5000/excluir_cachorro/'+id_cachorro,
            type: 'DELETE', 
            dataType: 'json', 
            success: cachorroExcluido, 
            error: erroAoExcluir
        });
        function cachorroExcluido (retorno) {
            if (retorno.resultado == "ok") { 
                $("#linha_" + id_cachorro).fadeOut(1000, function(){
                    alert("Cachorro removido com sucesso!");
                });
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoExcluir (retorno) {
            alert("erro ao excluir dados, verifique o backend: ");
        }
    });
    
});