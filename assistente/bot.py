FALLBACK = "Desculpe, não entendi. Pode reformular a pergunta?"


def responder(pergunta):
    texto = pergunta.lower()

    if "horário" in texto or "horario" in texto:
        return "Nosso atendimento funciona de segunda a sexta, das 9h às 18h."
    if "saldo" in texto:
        return "Para consultar seu saldo, acesse o aplicativo ou o internet banking."
    if "senha" in texto:
        return "Nunca pedimos sua senha por telefone, e-mail ou mensagem."
    if "limite" in texto:
        return "Seu limite é de R$ 5.000,00."
    return FALLBACK