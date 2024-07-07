# Importar a biblioteca chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criar um novo chatbot chamado Norman
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Criar o treinador e treinar o bot com algumas frases
trainer = ListTrainer(bot)

# Apresentação e Saudações:
trainer.train([
    'Olá!',
    'Olá! Seja bem-vindo. Como posso te ajudar hoje?',
    'Qual o seu nome?',
    'Meu nome é Norman. Posso te ajudar com diversas tarefas, como responder perguntas, fornecer informações e realizar ações.',
])

#  Informações e Suporte:
trainer.train([
    'Qual o horário de funcionamento da loja?',
    'A loja funciona de segunda a sexta das 9h às 18h e aos sábados das 9h às 14h.',
    'Como faço para trocar um produto?',
    'Para trocar um produto, você precisa trazer o produto com nota fiscal para a loja em até 7 dias após a compra.',
    'Qual a garantia dos produtos?'
    'A garantia dos produtos varia de acordo com a marca e o tipo de produto. Você pode encontrar mais informações sobre a garantia no site da loja ou no manual do produto.',
])

# Agendamento e Reservas:
trainer.train([
    'Gostaria de agendar um horário para o cabeleireiro.',
    'Claro! Qual dia e horário você prefere?',
    'Preciso de um horário na terça-feira às 10h.',
    'Verificando disponibilidade... Ótimo, tenho um horário disponível para você na terça-feira às 10h. Confirma?',
    'Sim, por favor.',
    'Sua reserva está confirmada! Você receberá um email de confirmação com os detalhes.',
])

# Vendas e Promoções:
trainer.train([
    'Quais são os produtos em promoção hoje?',
    'Temos diversas promoções em vigor hoje. Você pode encontrar uma lista completa das promoções no nosso site ou no app.',
    'Estou interessado em comprar um novo celular. Qual é o melhor modelo para mim?',
    'Para te ajudar a escolher o melhor celular, preciso saber mais sobre suas necessidades e orçamento. Você prefere um celular com boa câmera, bateria durável ou tela grande?',
    'Quero um celular com boa câmera e bateria durável. Meu orçamento é de até R$ 1.500,00.',
    'Com base nas suas informações, recomendo o modelo [Nome do Celular]. Ele possui uma ótima câmera, bateria de longa duração e está dentro do seu orçamento.',
])

# Entretenimento e Jogos:
trainer.train([
    'Conte uma piada.',
    'Qual é o animal que come com o rabo?',
    'Qual?',
    'Todos, porque ninguém tira o rabo para comer!',
    'Você sabe algum jogo legal?',
    'Sim! Eu posso te contar um desafio, adivinhar um animal ou até mesmo jogar um jogo de perguntas e respostas. Qual te interessa?',
])

# Feedback e Sugestões:
trainer.train([
    'Gostei muito do atendimento do chatbot.',
    'Obrigado pelo feedback positivo! Fico feliz em saber que pude te ajudar.',
    'Você poderia adicionar mais opções de pagamento na loja online?',
    'Sua sugestão foi anotada e será repassada à equipe responsável. Agradecemos por contribuir para a melhoria da nossa loja!',
])

# Conversas Criativas e Informais:
trainer.train([
    'O que você acha do tempo hoje?',
    'O dia está lindo! Perfeito para um passeio no parque ou uma tarde na praia.',
    'Qual o seu filme favorito?',
    'Meu filme favorito é [Nome do Filme]. Gosto muito da história e dos personagens.',
    'Você acredita em alienígenas?',
    'A existência de alienígenas ainda é um mistério, mas acho fascinante pensar na possibilidade de vida em outros planetas.',
])

# Personalização e Interação Individual:
trainer.train([
    'Qual o seu nome?',
    'Meu nome é [Nome do Chatbot]. Você pode me chamar de [Apelido].',
    'De onde você é?'
])

# Loop para conversar com o bot
while True:
    try:
        user_input = input("Você: ")
        bot_response = bot.get_response(user_input)
        print("Norman:", bot_response)
        
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
