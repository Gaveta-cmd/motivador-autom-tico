import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from motivador import obter_frase
from config import EMAIL, SENHA, DESTINATARIO
import schedule
import time

def enviar_email():
    frase = obter_frase()

    mensagem = MIMEMultipart()
    mensagem['From'] = EMAIL
    mensagem['To'] = DESTINATARIO
    mensagem['Subject'] = "Sua frase motivacional do dia! ✨"

    corpo = f"""
    Olá! Aqui está sua frase motivacional de hoje:

    {frase}

    Tenha um ótimo dia! 🚀
    """
    mensagem.attach(MIMEText(corpo, 'plain'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL, SENHA)
        servidor.sendmail(EMAIL, DESTINATARIO, mensagem.as_string())
        servidor.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar o email:", e)

# Agendamento diário às 08h
schedule.every().day.at("08:00").do(enviar_email)

if __name__ == "__main__":
    print("Automação iniciada. Aguardando horário para envio...")
    while True:
        schedule.run_pending()
        time.sleep(60)
