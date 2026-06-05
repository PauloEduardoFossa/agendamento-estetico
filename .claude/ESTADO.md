# Estado atual do projeto

## Data da última atualização
04/06/2026

## Módulos concluídos
- Módulo 0: Ambiente e organização (estrutura de pastas, arquivos de contexto, Git)
- Módulo 1: Conexão com Google Calendar API ✓

## Módulo em andamento
- Nenhum (pausa entre sessões)

## Próximo passo — Módulo 2: Ler e entender os dados da agenda
- Evoluir o `src/calendar_reader.py` para exibir mais campos dos eventos
  (descrição, participantes, cor do evento, recorrência)
- Explorar como o Google Calendar representa eventos recorrentes
  (campo `recurrence` com regras RRULE)
- Identificar manualmente na agenda da esposa quais clientes têm padrão quinzenal
- Preparar base para o módulo de detecção automática de padrões

## Para retomar amanhã, basta Ativar o ambiente virtual (sempre que abrir o terminal)
- .venv\Scripts\Activate.ps1

## Decisões pendentes
- Qual provedor WhatsApp usar: Z-API ou Evolution API

## Problemas em aberto
- Nenhum

## Arquivos criados até agora
- Estrutura de pastas do repositório
- Arquivos de contexto (.claude/)
- `requirements.txt` — bibliotecas do projeto
- `src/calendar_reader.py` — conecta na Google Calendar API e lista eventos
- `credentials.json` — chave OAuth do Google Cloud (não versionada)
- `token.json` — token de sessão gerado após 1º login (não versionado)
- `.gitignore` — protege arquivos sensíveis

## Ambiente configurado
- Python + .venv instalados
- Bibliotecas: google-auth, google-auth-oauthlib, google-api-python-client, python-dotenv
- Projeto Google Cloud criado: `agendamento-estetico`
- Google Calendar API ativada
- Credenciais OAuth2 criadas e funcionando
- Usuária de teste adicionada: taifossa@gmail.com
