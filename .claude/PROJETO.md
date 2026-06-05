# Projeto: Agendamento Estético

## Objetivo
Sistema para automatizar agendamentos e lembretes da esposa,
que presta serviços estéticos (extensão de cílios, designer de
sobrancelhas, alongamento de unhas com gel, entre outros).

## Problema central
- Clientes com padrão de recorrência variado (quinzenal, 20 dias, mensal)
- Agendamentos criados manualmente um a um na agenda
- Lembretes manuais via WhatsApp geram esquecimentos e retrabalho

## Solução
No último dia do mês, a esposa aperta um botão. O sistema:
1. Lê os últimos 3 meses do Google Calendar
2. Identifica o padrão de frequência de cada cliente
3. Agenda automaticamente os atendimentos previstos para o próximo mês
4. Envia lembrete via WhatsApp na véspera de cada atendimento

## Padrões de frequência das clientes
- **Quinzenal (15 dias):** cliente vem a cada 15 dias, qualquer dia da semana
  - Exemplos: Julia IEQ, Julia B
- **A cada 20 dias com dia fixo:** cliente vem a cada 20 dias sempre no mesmo dia da semana
  - Exemplo: Ju do Cledi vem sempre na segunda-feira a cada 20 dias
- **Mensal (1x por mês):** cliente vem aproximadamente uma vez ao mês, sem dia fixo

## Tipos de serviço — definidos pela cor do evento no Google Calendar
| colorId (API) | Cor no Google Calendar | Serviço |
|---|---|---|
| 5 | Banana (amarelo) | Manutenção de cílios |
| 6 | Tanjerina (laranja) | Esmaltação em gel |
| 10 | Manjericão (verde) | Designer de sobrancelhas |
| 11 | Tomate (vermelho) | Aplicação de cílios |

**Regra de filtro:** apenas eventos com colorId em {5, 6, 10, 11} são atendimentos do salão.
Eventos pessoais (Consagração, Culto, Aniversário, etc.) usam outros colorIds e são ignorados.

**Observação:** o colorId é por evento, não por cliente. A mesma cliente pode ter
serviços diferentes em visitas distintas (ex: Karol vem para esmaltação e sobrancelhas).

## Stack definida
- Linguagem: Python (aprendendo durante o projeto)
- Agendador de tarefas: APScheduler
- Banco de dados: PostgreSQL (local por enquanto)
- Integração calendário: Google Calendar API
- Integração WhatsApp: Z-API ou Evolution API (decidir no módulo 4)
- Interface futura: painel web em React

## Ambiente
- Windows local
- VS Code + extensão Claude Code
- GitHub para versionamento
- Desenvolvido com auxílio do Claude (PRO)

## Regras de negócio conhecidas
- Agendamentos NÃO são cadastrados como recorrentes no Google Calendar —
  cada atendimento é criado manualmente pela esposa
- Padrão é detectado analisando o histórico dos últimos 3 meses
- Para clientes com dia fixo (ex: sempre segunda), o próximo agendamento
  deve cair no dia da semana correto, não só na data calculada
- Lembrete: enviar WhatsApp na véspera do atendimento (dia anterior)
- Confirmação futura: cliente responde confirmando ou remarcando
