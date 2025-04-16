const { Builder, By } = require("selenium-webdriver");
require('chromedriver');

(async function testeHanked() {
    //pega url que vai ser utilizada no teste e seleciona o chrome como browser
  const url = "https://www.hankeds.com.br/prova/login2.html";
  let driver = await new Builder().forBrowser("chrome").build();

  try {

    await driver.get(url);
    await driver.sleep(2000);

    //seta variaveis com o ID dos elementos HTML de usuario e senha
    const username = await driver.findElement(By.id("username"));
    const password = await driver.findElement(By.id("password"));
    
    //encontra o botao pelo path
    const botao = await driver.findElement(
      By.xpath("//button[contains(text(),'Entrar')]")
    );

    //escreve "admin" no campo de username
    for (const letra of "admin") {
      await username.sendKeys(letra);
      await driver.sleep(250);
    }

    //tempo de espera
    await driver.sleep(1000);

    //escreve "admin123456" no campo de senha
    for (const letra of "admin123456") {
      await password.sendKeys(letra);
      await driver.sleep(250);
    }

    //tempo de espera e click no botao de "Entrar"
    await driver.sleep(1000);
    await botao.click();

    //tempo de espera
    await driver.sleep(4000);

    //pega URL atual da página do driver(https://www.hankeds.com.br/prova/login2.html)
    const urlAtual = await driver.getCurrentUrl();
    //se na URL conter "destino.html" teste passou, caso não tenha teste falhou
    if (urlAtual.includes("destino.html")) {
      console.log(" Teste passou: redirecionado corretamente.");
    } else {
      console.log(" Teste falhou: não houve redirecionamento.");
    }

    //tempo de espera
    await driver.sleep(5000);
    //se exister algum erro, mostra o erro no console
  } catch (err) {
    console.error(" Erro durante o teste:", err);
    //finaliza o programa
  } finally {
    await driver.quit();
  }
})();
