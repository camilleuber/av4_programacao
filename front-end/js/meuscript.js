$(function () {
  
  function mostrarCachorros() {
    $.ajax({
      url: 'http://localhost:5000/listar_cachorros',
      method: 'GET',
      dataType: 'json',
      success: listarCachorro,
      error: function () {
        alert('erro ao ler dados, verifique o backend');
      },
    });

    function listarCachorro(cachorros) {
      $("#tableBody").empty();
      showContent("tabela-cachorro");
      var linhas = '';
  
      for (cachorro of cachorros) {
        novaLinha = `<tr id="linha_${cachorro.id}">  
                          <td>${cachorro.id}</td> 
                          <td>${cachorro.nomeDoCachorro}</td> 
                          <td>${cachorro.genero}</td> 
                          <td>${cachorro.idade}</td> 
                          <td>${cachorro.raca}</td> 
                          <td>${cachorro.porte}</td> 
                          <td>${cachorro.cor}</td> 
                          <td>${cachorro.problemaDeSaude}</td> 
                          <td>
                            <a href="#" id="deletar_${cachorro.id}" class="deletar_cachorros" title="Excluir cachorro">
                                <span class="material-icons">
                                  Deletar cachorro do sistema
                                </span>
                            </a>
                          </td>
                        </tr>`;
        linhas += novaLinha;
        $('#tableBody').html(linhas);
      }
    }
  }
  function showContent(nextPage) {
    $("#inicio").addClass("d-none");
    $("#tabela-cachorro").addClass("d-none");
    $("#tabela-veterinarios").addClass("d-none");
    $("#tabela-medicamentos").addClass("d-none");
    $(`#${nextPage}`).removeClass("d-none");
  }

  $('#link-listar').click(function() {
    mostrarCachorros();
  });

  $("#link-inicial").click(function() {
    inicio();
    showContent("inicio");
  });

  $('#nav-brand').click(function() {
    showContent("inicio");
  });

  $(document).on("click", "#btn-incluir", function() {
    const nomeDoCachorro = $('#campo-nomeDoCachorro').val();
    const genero = $('#campo-genero').val();
    const idade = $('#campo-idade').val();
    const raca = $('#campo-raca').val();
    const porte = $('#campo-porte').val();
    const cor = $('#campo-cor').val();
    const problemaDeSaude = $('#campo-problemaDeSaude').val();

    const cachorroData = JSON.stringify({
      nomeDoCachorro: nomeDoCachorro,
      genero: genero,
      idade: idade,
      raca: raca,
      porte: porte,
      cor: cor,
      problemaDeSaude: problemaDeSaude,
    });

    $.ajax({
      url: 'http://localhost:5000/inserir_cachorro',
      type: 'POST',
      contentType: 'application/json',
      dataType: 'json',
      data: cachorroData,
      success: inserirCachorro,
      error: inserirCachorroErro,
    });

    function inserirCachorro(resposta) {
      if (resposta.result == 'ok') {
          alert('Cachorro adicionado com sucesso')
          $('#campo-nomeDoCachorro').val('');
          $('#campo-genero').val('');
          $('#campo-idade').val('');
          $('#campo-raca').val('');
          $('#campo-porte').val('');
          $('#campo-cor').val('');
          $('#campo-problemaDeSaude').val('');
      } else {
          alert('Erro na adição do cachorro!')
      }
    }

    function inserirCachorroErro(resposta){
      alert('Erro na chamada do back-end')
    }
  });
  
  $('#modal-incluir').on('hidden.bs.modal', function(e) {
    if (!$('#tabela-cachorro').hasClass('invisible')) {
      mostrarCachorros();
    }
  });
  
  
  
  $(document).on("click", ".deletar_cachorros", function() {
    var component = $(this).attr("id");

    var icon_name = "deletar_";
    var cachorro_id = component.substring(icon_name.length);

    $.ajax({
      url: 'http://localhost:5000/deletar_cachorros/' + cachorro_id,
      type: "DELETE",
      dataType: "json",
      success: cachorroDeletado,
      error: cachorroDeletadoErro
    });

    function cachorroDeletado(retorno) {
      if (retorno.result == "ok") {
        $('#linha_' + cachorro_id).fadeOut(1000, function() {
          alert("Cachorro removido com sucesso!");
          mostrarCachorros();
        });
      } else {
          alert(`${retorno.result}: ${retorno.details}`);
      }
    }

    function cachorroDeletadoErro(response) {
      alert("Erro ao excluir dados, verifique o Backend!");
    }
  });

  function listar_veterinarios() {
    $.ajax({
        url: 'http://localhost:5000/listar_veterinarios',
        method: 'GET',
        dataType: 'json', 
        success: listar, 
        error: function(problema) {
            alert("erro ao ler dados, verifique o backend: ");
        }
    });
    function listar(veterinarios) {
        $('#corpoTabelaVeterinarios').empty();
        showContent("tabela-veterinarios")    
        var linhas = '';
        for (veterinario of veterinarios) { 
            novaLinha = '<tr id="linha_veterinario'+veterinario.id+'">' + 
            '<td>' + veterinario.nomeDoVeterinario + '</td>' + 
            '<td>' + veterinario.registro + '</td>' + 
            '<td>' + veterinario.clinica + '</td>' + 
            //'<td>' + veterinario.cachorro.nomeDoCachorro + '</td>' + 
            //'<td>' + veterinario.cachorro.problemaDeSaude + '</td>' + 
            '</tr>';
            linhas += novaLinha;
            $('#corpoTabelaVeterinarios').append(novaLinha);
        }
    }
  }

  $(document).on("click", "#linkListarVeterinarios", function() {
    listar_veterinarios();
  });


  function listar_medicamentos() {
    $.ajax({
        url: 'http://localhost:5000/listar_medicamentos',
        method: 'GET',
        dataType: 'json',
        success: listar,
        error: function(problema) {
            alert("erro ao ler dados, verifique o backend: ");
        }
    });
    function listar(medicamentos) {
        $('#corpoTabelaMedicamentos').empty();
        showContent("tabela-medicamentos")      
        var linhas = '';
        for (medicamento of medicamentos) { 
            novaLinha = '<tr id="linha_medicamento'+medicamento.id+'">' + 
            '<td>' + medicamento.nomeDoMedicamento + '</td>' + 
            '<td>' + medicamento.dosagem + '</td>' + 
            '<td>' + medicamento.valor + '</td>' + 
            //'<td>' + medicamento.cachorro.nomeDoCachorro+ '</td>' + 
            //'<td>' + medicamento.cachorro.problemaDeSaude+ '</td>' + 
            '</tr>';
            linhas += novaLinha;
            $('#corpoTabelaMedicamentos').append(novaLinha);
        }
    }
  }

  $(document).on("click", "#linkListarMedicamentos", function() {
    listar_medicamentos();
  });
  showContent("inicio");
});