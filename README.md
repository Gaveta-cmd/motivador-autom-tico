# 💌 Motivador Automático

> Um projeto de automação em Python que envia frases motivacionais por e-mail todos os dias às 8h da manhã. Ideal para começar o dia com inspiração ou motivar sua equipe!

---

## 🚀 Funcionalidades

✅ Conecta-se a uma API pública de frases motivacionais  
✅ Envia e-mail automaticamente para um destinatário definido  
✅ Agendamento diário com a biblioteca `schedule`  
✅ Código simples, comentado e fácil de personalizar

---

## 🧰 Tecnologias usadas

- Python 3.x  
- [requests](https://pypi.org/project/requests/) – para acessar a API de frases  
- [schedule](https://pypi.org/project/schedule/) – para agendamento de tarefas  
- `smtplib` e `email.mime` – para envio de e-mails

---

## 📂 Estrutura do Projeto

```bash
motivador-automatico/
│
├── config.py           # Configurações do e-mail (remetente, senha e destinatário)
├── main.py             # Arquivo principal com o loop de agendamento
├── motivador.py        # Módulo que acessa a API e retorna a frase
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
