"""
Módulo 1 - Leitura do Google Calendar
Objetivo: conectar na API e listar os próximos agendamentos
"""

import os
import webbrowser
from datetime import datetime, timezone

# google-auth-oauthlib: cuida do login OAuth2 (igual a um TLogin do Delphi)
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Permissões que vamos pedir ao Google
# "readonly" = só leitura, não modificamos nada na agenda
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# Caminhos dos arquivos de credencial
# credentials.json = chave do app (baixada do Google Cloud)
# token.json       = salvo automaticamente após o 1º login; evita logar toda vez
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"


def autenticar():
    """
    Faz o login OAuth2 com o Google.
    Na 1ª execução: abre o navegador para autorizar.
    Nas próximas: usa o token.json salvo automaticamente.
    """
    creds = None

    # Se já existe um token salvo de uma sessão anterior, carrega ele
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # Se não tem token, ou o token expirou, precisa fazer login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Token expirado mas renovável (como um "refresh session" do Delphi)
            creds.refresh(Request())
        else:
            # Abre o Chrome para o usuário autorizar o app
            # open_browser=False porque vamos abrir manualmente com o Chrome
            webbrowser.register(
                "chrome",
                None,
                webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"),
            )
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0, browser="chrome")

        # Salva o token para não precisar logar da próxima vez
        with open(TOKEN_FILE, "w") as token_file:
            token_file.write(creds.to_json())

    return creds


def listar_proximos_eventos(quantidade=10):
    """
    Lista os próximos N eventos do Google Calendar.
    Padrão: 10 eventos.
    """
    creds = autenticar()

    # "build" cria o objeto de acesso à API (como instanciar um componente no Delphi)
    service = build("calendar", "v3", credentials=creds)

    # Pega o horário atual no formato que a API do Google espera (ISO 8601 com timezone)
    agora = datetime.now(timezone.utc).isoformat()

    print(f"\nBuscando os próximos {quantidade} eventos...\n")

    # Chama a API do Google para buscar eventos futuros
    resultado = (
        service.events()
        .list(
            calendarId="primary",   # calendário principal da conta
            timeMin=agora,          # só eventos a partir de agora
            maxResults=quantidade,  # limite de resultados
            singleEvents=True,      # expande eventos recorrentes em ocorrências individuais
            orderBy="startTime",    # ordena por data de início
        )
        .execute()
    )

    # "items" é a lista de eventos retornada pela API (como um TDataSet.RecordCount no Delphi)
    eventos = resultado.get("items", [])

    if not eventos:
        print("Nenhum evento encontrado.")
        return

    for evento in eventos:
        # Eventos podem ter data+hora ("dateTime") ou só data ("date") para eventos de dia inteiro
        inicio = evento["start"].get("dateTime", evento["start"].get("date"))
        titulo = evento.get("summary", "(sem título)")
        print(f"  {inicio}  |  {titulo}")


# Ponto de entrada do script
# Equivale ao "begin ... end." do programa principal no Delphi
if __name__ == "__main__":
    listar_proximos_eventos()
