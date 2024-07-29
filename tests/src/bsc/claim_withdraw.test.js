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
// Test from replayed transaction: https://testnet.bscscan.com/tx/0x4933296ae725dbdd0e1a093fdf508f88ad22c9ae315282eccccda148405c9856
const inputData =
  "0xf84444360000000000000000000000000000000000000000000000000000000000000000";

nano_models.forEach(function (model) {
  test(
    "[Nano " + model.letter + "] Claim Withdraw BNB",
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
          testNetwork + "_bnbx_claim_withdraw_" + model.name,
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
