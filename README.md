# Documentação do Sistema - Livro de Serviço Diário
## Objetivo do Sistema
O sistema será utilizado para registrar e controlar os serviços diários de uma equipe de operação. A finalidade é registrar os dados referentes ao serviço interno e externo, registrar ocorrências, controlar viaturas e elaborar boletins de ocorrência, entre outras funcionalidades.
1. Primeira Parte - Serviço Diário
1.1 Serviço Interno

a) Permanência: Registra os dados sobre a permanência dos operadores durante o serviço. Isso pode incluir turnos e horários de trabalho, controles de presença e eventos que alteram a permanência (como substituições ou mudanças de turno).

b) Alterações do Serviço Interno: Esta seção deve permitir que sejam registradas quaisquer mudanças no serviço interno, como alterações de horário ou mudanças nos turnos dos operadores.

1.2 Serviço Externo

a) Escala: Aqui, será registrado o planejamento das escalas de serviço externas. A ideia é controlar quais operadores estão designados para atividades externas e em quais horários.

1) Permutas: Caso haja troca de turnos ou escala entre os operadores.
2) Remanejamentos: Caso algum operador precise ser realocado para uma função diferente.
3) Faltas: Registro das ausências dos operadores durante o serviço.
4) Atrasos: Informações sobre atrasos nos horários de chegada.
5) Baixas: Informações sobre a baixa de operadores ou veículos do serviço.
6) Liberações: Caso algum operador ou viatura seja liberado de suas funções durante o expediente.
b) Viaturas/Mikes: Controle das viaturas e Mikes (provavelmente veículos ou equipamentos utilizados) designados para o serviço externo.

c) Boletins de Ocorrências: Registro das ocorrências que acontecem durante o serviço externo. O sistema deve permitir a geração e registro de boletins de ocorrência para todas as situações importantes.

d) Registro de Ocorrência: Como parte do boletim de ocorrência, o sistema deve permitir o registro detalhado de cada ocorrência, incluindo informações sobre o incidente, os envolvidos, e outras informações relevantes.

e) Ocorrências de Trânsito: Caso o serviço envolva controle ou monitoramento de trânsito, é necessário registrar ocorrências específicas, como acidentes, multas, infrações ou qualquer outro evento de trânsito.

f) Controle de Pasta de Termo de Ocorrência (TCO): Um sistema para controlar os Termos de Ocorrência, garantindo que todos os documentos relacionados sejam registrados corretamente e possam ser acessados quando necessário.

g) Alterações Diversas do Serviço Externo: Qualquer alteração que ocorra durante o serviço externo e que precise ser registrada, como mudanças no plano de ação, novas designações de tarefas ou outras situações imprevistas.

2. Funcionalidades e Fluxo de Trabalho
Com a estrutura acima, podemos pensar nas funcionalidades principais do sistema e como elas se conectarão entre si. Para cada um dos itens citados, o sistema deverá permitir o registro, a alteração e a consulta das informações de forma fácil e acessível.

Fluxo de Trabalho Básico
Registro de Serviço Diário:
O operador de dia de serviço será responsável por inserir os dados iniciais (como escala, viaturas, ocorrências, etc.).
Cada seção do serviço (interno e externo) poderá ser editada e acompanhada em tempo real.
Alteração de Informações:
O sistema deve permitir que o operador altere dados como faltas, remanejamentos e liberações à medida que o serviço progride.
Registro de Ocorrências e Boletins:
O operador de dia será capaz de registrar ocorrências, gerar boletins e, se necessário, registrar termos de ocorrência.
Gerenciamento de Viaturas e Equipamentos:
O sistema deve permitir o controle das viaturas e equipamentos em uso, verificando se estão disponíveis, se há algum problema ou se precisam de manutenção.

3. Documentação e Assinaturas
Além de registrar as informações no sistema, será necessário gerar um documento em PDF que será assinado pelo operador de dia de serviço. O PDF deve incluir os seguintes dados:

Identificação do operador.
Dados completos do serviço (interno e externo).
Informações sobre as ocorrências registradas e suas respectivas descrições.
Assinatura do operador responsável, validando as informações e confirmando que o serviço foi executado conforme o planejado.
