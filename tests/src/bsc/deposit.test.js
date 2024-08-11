import "core-js/stable";
import "regenerator-runtime";
import {
  waitForAppScreen,
  zemu,
  nano_models,
  serializeTx,
} from "../test.fixture";

const contractAddr = "0x3b961e83400d51e6e1af5c450d3c7d7b80588d28";
const pluginName = "staderlabs";
const testNetwork = "bsc";
const chainID = 56;
const signedPlugin = false;
// Test from replayed transaction: https://bscscan.com/tx/0x9b712c0500b22839ce9f01952fc1d4237bf33277552ea5501f3dd8e3d419bd0f
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
