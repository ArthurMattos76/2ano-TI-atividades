// Aguarda o carregamento completo da árvore DOM antes de executar os scripts
document.addEventListener('DOMContentLoaded', function () {

    // ==========================================================================
    // 1. SAUDAÇÃO DINÂMICA
    // ==========================================================================
    
    // Função que define a saudação com base na hora atual do navegador
    function atualizarSaudacao() {
        // Obtém o elemento HTML onde a saudação será exibida
        const elementoSaudacao = document.getElementById('saudacao');
        
        // Obtém a hora atual (0 até 23)
        const horaAtual = new Date().getHours();
        
        let textoSaudacao = 'Olá!';

        // Condicional para verificar a faixa de horário
        if (horaAtual >= 5 && horaAtual < 12) {
            textoSaudacao = 'Bom dia!';
        } else if (horaAtual >= 12 && horaAtual < 18) {
            textoSaudacao = 'Boa tarde!';
        } else {
            textoSaudacao = 'Boa noite!';
        }

        // Insere a saudação calculada dentro do elemento no HTML
        if (elementoSaudacao) {
            elementoSaudacao.textContent = textoSaudacao;
        }
    }

    // Executa a função de saudação
    atualizarSaudacao();


    // ==========================================================================
    // 2. ANO ATUAL AUTOMÁTICO NO RODAPÉ
    // ==========================================================================
    
    // Obtém o elemento span do ano no rodapé
    const elementoAno = document.getElementById('ano-atual');
    if (elementoAno) {
        // Define o texto com o ano corrente (ex: 2026)
        elementoAno.textContent = new Date().getFullYear();
    }


    // ==========================================================================
    // 3. MENU HAMBÚRGUER (RESPONSIVO PARA CELULARES)
    // ==========================================================================
    
    // Seleciona o botão hambúrguer e o menu de navegação
    const btnHamburguer = document.getElementById('btn-hamburguer');
    const menuNavegacao = document.getElementById('menu-navegacao');
    const linksNav = document.querySelectorAll('.link-nav');

    if (btnHamburguer && menuNavegacao) {
        // Evento de clique para abrir ou fechar o menu
        btnHamburguer.addEventListener('click', function () {
            // Alterna a classe 'menu-ativo' no CSS
            menuNavegacao.classList.toggle('menu-ativo');

            // Verifica se o menu está visível para atualizar o atributo de acessibilidade aria-expanded
            const estaAberto = menuNavegacao.classList.contains('menu-ativo');
            btnHamburguer.setAttribute('aria-expanded', estaAberto);
        });

        // Fecha o menu mobile automaticamente ao clicar em qualquer link de seção
        linksNav.forEach(function (link) {
            link.addEventListener('click', function () {
                if (menuNavegacao.classList.contains('menu-ativo')) {
                    menuNavegacao.classList.remove('menu-ativo');
                    btnHamburguer.setAttribute('aria-expanded', 'false');
                }
            });
        });
    }


    // ==========================================================================
    // 4. ALTERNÂNCIA DE TEMA CLARO / ESCURO
    // ==========================================================================
    
    // Seleciona o botão de troca de tema e o elemento do ícone
    const btnTema = document.getElementById('btn-tema');
    const iconeTema = document.getElementById('icone-tema');

    if (btnTema && iconeTema) {
        // Evento de clique no botão de tema
        btnTema.addEventListener('click', function () {
            // Alterna a classe .tema-escuro no elemento <body>
            document.body.classList.toggle('tema-escuro');

            // Verifica se o tema escuro está ativado e altera o ícone exibido
            const ehTemaEscuro = document.body.classList.contains('tema-escuro');
            iconeTema.textContent = ehTemaEscuro ? '☀️' : '🌙';
        });
    }


    // ==========================================================================
    // 5. VALIDAÇÃO DO FORMULÁRIO DE CONTATO
    // ==========================================================================
    
    // Seleciona o formulário de contato
    const formContato = document.getElementById('form-contato');

    if (formContato) {
        // Evento de envio (submit) do formulário
        formContato.addEventListener('submit', function (evento) {
            // Impede o envio padrão da página para podermos validar com JS
            evento.preventDefault();

            // Variável para controle da validação
            let formularioValido = true;

            // Captação dos campos
            const campoNome = document.getElementById('nome');
            const campoEmail = document.getElementById('email');
            const campoMensagem = document.getElementById('mensagem');
            const campoConsentimento = document.getElementById('consentimento');

            // Captação das mensagens de erro
            const erroNome = document.getElementById('erro-nome');
            const erroEmail = document.getElementById('erro-email');
            const erroMensagem = document.getElementById('erro-mensagem');
            const erroConsentimento = document.getElementById('erro-consentimento');
            const mensagemSucesso = document.getElementById('mensagem-sucesso');

            // Limpa mensagens anteriores
            erroNome.textContent = '';
            erroEmail.textContent = '';
            erroMensagem.textContent = '';
            erroConsentimento.textContent = '';
            mensagemSucesso.style.display = 'none';

            // Validação do campo Nome (não pode estar vazio)
            if (campoNome.value.trim() === '') {
                erroNome.textContent = 'Por favor, informe seu nome completo.';
                formularioValido = false;
            }

            // Validação do campo E-mail (formato básico)
            const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (campoEmail.value.trim() === '') {
                erroEmail.textContent = 'Por favor, informe seu e-mail.';
                formularioValido = false;
            } else if (!regexEmail.test(campoEmail.value.trim())) {
                erroEmail.textContent = 'Por favor, informe um e-mail válido.';
                formularioValido = false;
            }

            // Validação do campo Mensagem (não pode estar vazio)
            if (campoMensagem.value.trim() === '') {
                erroMensagem.textContent = 'Por favor, digite sua mensagem.';
                formularioValido = false;
            }

            // Validação do Checkbox de Consentimento
            if (!campoConsentimento.checked) {
                erroConsentimento.textContent = 'Você precisa concordar com o tratamento dos dados para prosseguir.';
                formularioValido = false;
            }

            // Se todas as verificações passarem
            if (formularioValido) {
                // Exibe mensagem de sucesso
                mensagemSucesso.textContent = '✅ Mensagem validada com sucesso! (Demonstração local: nenhum dado foi enviado para um servidor exterior).';
                mensagemSucesso.style.display = 'block';

                // Limpa os campos do formulário
                formContato.reset();
            }
        });
    }

});