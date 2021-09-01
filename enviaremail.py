#!/usr/bin/python
#encoding: utf-8

#Criado por Gsouza1
#https://github.com/gsouza1

from acesso import SENHA, USUARIO #Coloquei seu usuario e senha do gmail no aquivo acesso.py 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')


PARA = ["destino01@gmail.com","destino02@gmail.com","destino03@gmail.com"] # Coloquei os destinatarios separados por virgula 
EU = "Seu Nome <seugmail@gmail.com>" #Seu nome é o que aparece no recebida DE: 
ASSUNTO = "⭐ Coloque o assunto aqui✔️" #Assunto (Possivel colocar emoji)
x = 1
for i in PARA: #Laço de repetição para trocar o destino após envio
    #Template HTML para email 
    email_content ="""
        <html>
            <head></head>
                <body>
                    <p>Teste<br>
                        Teste pula linha?<br>
                        clique aqui <a href="http://www.google.com.br">link aqui</a> para sei la oque.
                    </p>
                </body>
        </html>
    """
    
    msg = email.message.Message()
    destino = i #Troca o destino após envio
    msg['Subject'] = ASSUNTO
    msg['From'] = EU
    msg['To'] = destino
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(USUARIO, SENHA)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())