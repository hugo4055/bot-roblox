# VoidBot Roblox — versão inicial

Projeto inicial com menu auxiliar para Windows e NPC de exemplo para Roblox Studio.

## O que funciona
- Menu Windows em Python/Tkinter para abrir a busca de um usuário Roblox.
- Campo para colar e abrir o link de uma experiência Roblox.
- Script Lua de NPC para sua própria experiência: segue o jogador mais próximo, calcula caminhos e responde com frases predefinidas.

## Limitações importantes
- O menu **não** envia pedidos de amizade automaticamente, não verifica se um pedido foi aceito e não controla uma conta Roblox.
- O NPC só funciona em experiências que você criou ou tem permissão para editar. Ele não pode ser inserido livremente em jogos públicos de terceiros.
- A conversa nesta versão usa frases predefinidas; não é uma IA generativa.
- Nunca compartilhe senha, cookie de sessão ou token da sua conta.

## 1. Executar o menu no Windows
1. Instale Python 3: https://www.python.org/downloads/windows/
2. Baixe este repositório como ZIP e extraia-o.
3. Abra a pasta extraída.
4. Dê dois cliques em `voidbot_desktop.py`. Se não abrir, execute `python voidbot_desktop.py` em um terminal nessa pasta.
5. Digite o nome e clique em **Abrir busca de usuário**. Cole um link de experiência e clique em **Abrir experiência**.

## 2. Instalar o NPC no Roblox Studio
1. Abra o Roblox Studio e uma experiência sua.
2. Use **Avatar > Rig Builder** para criar um rig R15 ou R6.
3. No Explorer, renomeie o modelo para `VoidBotNPC` e deixe-o em `Workspace`.
4. Verifique se o modelo contém `Humanoid`, `HumanoidRootPart` e `Head`.
5. Em `ServerScriptService`, crie um objeto **Script**.
6. Copie o conteúdo de [VoidBotNPC.server.lua](VoidBotNPC.server.lua) para esse Script.
7. Clique em **Play**. Aproxime-se do NPC e use o prompt **Conversar**.
8. Teste primeiro em uma experiência privada sua.

## Documentação
- Roblox Studio: https://create.roblox.com/docs/pt-br/studio/setup
- Pathfinding: https://create.roblox.com/docs/characters/pathfinding
