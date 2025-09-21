// deploy-contract.js
// 스마트 컨트랙트 배포 및 ABI 복사 스크립트
const { exec } = require('child_process');
const path = require('path');

const projectRoot = path.join(__dirname, '../../../../..'); // VOICE_NFT_TRADING 경로
const truffleDir = path.join(__dirname, '../truffle-project');
const frontendContractsDir = path.join(projectRoot, 'src/frontend/src/contracts');

const script = `
cd ${truffleDir} && \
truffle migrate --reset && \
cp build/contracts/MyAudioNFT.json ${frontendContractsDir}/
`;

console.log('🚀 스마트 컨트랙트 배포 시작...');
console.log(`📁 Truffle 디렉토리: ${truffleDir}`);
console.log(`📁 ABI 복사 대상: ${frontendContractsDir}`);

exec(script, (err, stdout, stderr) => {
  if (err) {
    console.error('❌ 스마트 컨트랙트 배포 실패:', err);
    console.error('stderr:', stderr);
    process.exit(1);
  }
  console.log('✅ 스마트 컨트랙트 배포 및 ABI 복사 완료!');
  console.log(stdout);
});
