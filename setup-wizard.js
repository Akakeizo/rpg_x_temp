const readline = require('readline');
const fs = require('fs');
const path = require('path');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const envPath = path.resolve(__dirname, '.env');

function questionAsync(query) {
  return new Promise(resolve => rl.question(query, resolve));
}

async function runWizard() {
  console.log('=== Wizard de Configuração de Banco de Dados ===');

  const useMongo = await questionAsync('Deseja configurar MongoDB Atlas? (s/n): ');
  let mongoURI = '';
  if (useMongo.toLowerCase() === 's') {
    mongoURI = await questionAsync('Informe a URI de conexão do MongoDB Atlas: ');
  }

  const usePostgres = await questionAsync('Deseja configurar PostgreSQL? (s/n): ');
  let pgUser = '', pgHost = '', pgDatabase = '', pgPassword = '', pgPort = '';
  if (usePostgres.toLowerCase() === 's') {
    pgUser = await questionAsync('Usuário do PostgreSQL: ');
    pgHost = await questionAsync('Host do PostgreSQL: ');
    pgDatabase = await questionAsync('Database do PostgreSQL: ');
    pgPassword = await questionAsync('Senha do PostgreSQL: ');
    pgPort = await questionAsync('Porta do PostgreSQL (padrão 5432): ');
  }

  let envContent = '';

  if (mongoURI) {
    envContent += `MONGODB_URI=${mongoURI}\n`;
  }
  if (pgUser) {
    envContent += `PG_USER=${pgUser}\nPG_HOST=${pgHost}\nPG_DATABASE=${pgDatabase}\nPG_PASSWORD=${pgPassword}\nPG_PORT=${pgPort || 5432}\n`;
  }

  fs.writeFileSync(envPath, envContent);
  console.log(`Configurações salvas em ${envPath}`);

  rl.close();
}

if (require.main === module) {
  runWizard();
}

module.exports = { runWizard };
