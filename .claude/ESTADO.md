# Estado atual do projeto

## Data da última atualização
04/06/2026

## Módulos concluídos
- Módulo 0: Ambiente e organização (estrutura de pastas, arquivos de contexto, Git)
- Módulo 1: Conexão com Google Calendar API ✓
- Módulo 2: Exploração e entendimento dos dados da agenda ✓

## Módulo em andamento
- Nenhum (pausa entre sessões)

## Próximo passo — Módulo 3: Detecção de padrão de frequência por cliente
- Buscar os últimos 3 meses de eventos do Google Calendar
- Filtrar apenas atendimentos do salão (colorId em: 5, 6, 10, 11)
- Agrupar eventos por nome de cliente
- Calcular intervalo médio entre visitas de cada cliente
- Classificar o padrão detectado:
  - ~15 dias → quinzenal
  - ~20 dias com mesmo dia da semana → "20 dias com dia fixo"
  - ~30 dias → mensal
- Exibir o resultado no terminal: "Camila: quinzenal | Ju do Cledi: 20 dias (segunda)"

## Para retomar, basta ativar o ambiente virtual no terminal
- `.venv\Scripts\Activate.ps1`

## Decisões pendentes
- Qual provedor WhatsApp usar: Z-API ou Evolution API

## Problemas em aberto
- Nenhum

## Arquivos criados até agora
- Estrutura de pastas do repositório
- Arquivos de contexto (.claude/)
- `requirements.txt` — bibliotecas do projeto
- `src/calendar_reader.py` — conecta na Google Calendar API, lista e inspeciona eventos
- `credentials.json` — chave OAuth do Google Cloud (não versionada)
- `token.json` — token de sessão gerado após 1º login (não versionado)
- `.gitignore` — protege arquivos sensíveis

## Conhecimento adquirido
- Agendamentos NÃO são recorrentes no Google Calendar — criados manualmente um a um
- Padrão deve ser detectado analisando histórico, não campo `recurrence`
- Filtro de atendimentos: colorId 5 (Banana), 6 (Tanjerina), 10 (Manjericão), 11 (Tomate)
- Mesmo cliente pode ter serviços diferentes em visitas distintas
