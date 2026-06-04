# Projeto: Agendamento Estético

## Objetivo
Sistema para automatizar agendamentos e lembretes da esposa,
que presta serviços estéticos (extensão de cílios, designer de
sobrancelhas, alongamento de unhas com gel, entre outros).

## Problema central
- Clientes com padrão de recorrência (ex: Julia vem sexta sim, sexta não)
- Lembretes manuais via WhatsApp geram esquecimentos e retrabalho

## Solução
- Leitura da Google Agenda para identificar padrões de recorrência
- Agendamento automático baseado em regras por cliente
- Envio automático de lembrete via WhatsApp no dia anterior

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
- Recorrência quinzenal: cliente vem em semanas alternadas
- Lembrete: enviar WhatsApp na véspera do atendimento (dia anterior)
- Confirmação futura: cliente responde confirmando ou remarcando
