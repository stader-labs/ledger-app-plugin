import "core-js/stable";
import "regenerator-runtime";
import {
  waitForAppScreen,
  zemu,
  nano_models,
  serializeTx,
} from "../test.fixture";

const contractAddr = "0x2f9b0eb7e7f5978c3cbe68ef897b15de15408fde";
const pluginName = "staderlabs";
const testNetwork = "bsc";
const chainID = 97;
const signedPlugin = false;
// Test from replayed transaction: https://testnet.bscscan.com/tx/0x6d0bab1856bfe96921c75132c8acfe9e24b7eb2a23afd166d3e5fc7f874a88b3
const inputData = "0x9ddb511a0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000004065313663623065316333353133303164333338656661343334656531646166336631393335386363633363666161643163386264323733663736633133313561";

nano_models.forEach(function (model) {
  test(
    "[Nano " + model.letter + "] Deposit BNB",
    zemu(
      model,
      async (sim, eth) => {
        const serializedTx = serializeTx(contractAddr, inputData, chainID);

        const tx = eth.signTransaction("44'/60'/0'/0/0", serializedTx);

        const right_clicks = model.letter === "S" ? 5 : 5;

        // Wait for the application to actually load and parse the transaction
        await waitForAppScreen(sim);
        // Navigate the display by pressing the right button `right_clicks` times, then pressing both buttons to accept the transaction.
        await sim.navigateAndCompareSnapshots(
          ".",
          testNetwork + "_bnbx_deposit_"+ model.name,
          [right_clicks, 0]
        );

        await tx;
      },
      signedPlugin,
      testNetwork
    ),
    20000
  );
});
