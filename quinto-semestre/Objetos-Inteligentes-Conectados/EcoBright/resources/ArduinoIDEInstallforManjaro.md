# Guia Completo para Instalar o Arduino IDE no Manjaro via Flatpak 🚀

Este guia irá orientá-lo na instalação do Arduino IDE no Manjaro usando o Flatpak. O uso do Flatpak é uma boa opção, pois isola as dependências e facilita as atualizações. 🛠️

## Passo a Passo

1. **Instalar o Flatpak** 🖥️  
   Caso o Flatpak não esteja instalado, você pode instalá-lo usando o seguinte comando:
   ```bash
   sudo pacman -S flatpak
   ```

2. **Adicionar o repositório Flathub** 🌐  
   O repositório Flathub contém o Arduino IDE. Para adicioná-lo, execute o seguinte comando:
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **Instalar o Arduino IDE** 📦  
   Agora você pode instalar o Arduino IDE com o comando:
   ```bash
    flatpak install flathub cc.arduino.arduinoide
   ```

4. **Executar o Arduino IDE** ▶️  
   Para executar o Arduino IDE, utilize o seguinte comando:
   ```bash
   flatpak run cc.arduino.arduinoide
   ```
5. **Ou Abra a GUI com Estilo! 🎨**  
   Se preferir, você pode encontrar o Arduino IDE na sua lista de aplicativos e abri-lo diretamente pela interface gráfica do seu ambiente de trabalho. É só procurar por "Arduino" e dar um clique para começar a programar! 💻
   
## Observações ⚠️

- A versão do Flatpak do Arduino IDE pode ter algumas restrições devido ao seu isolamento. Você pode precisar conceder permissões para acessar dispositivos USB, o que é necessário para carregar código em placas Arduino. 
- Essas permissões podem ser gerenciadas com comandos adicionais do Flatpak, se necessário.

Pronto! Agora você deve ter o Arduino IDE instalado e funcionando no seu Manjaro. 🎉
