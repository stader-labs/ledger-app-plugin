import "core-js/stable";
import "regenerator-runtime";
import {
  waitForAppScreen,
  zemu,
  nano_models,
  serializeTx,
  txFromEtherscan,
} from "../../test.fixture";

const testNetwork = "ethereum";
// Test from replayed transaction: https://etherscan.io/tx/0x31a88ec3977a4cd4ab0a105607a9ac1d350e1f2a2148345f6bdf9b583a74518b
const inputData =
  "0x02f8910181e48439d106808502c0b7a94e8302c6ad9462de59c08eb5dae4b7e6f7a8cad3006d6965ec1680a46dbaf9ee000000000000000000000000ac3e018457b222d93114458476f3e3416abbe38fc001a015b3a4d1d38f492c00322e7a1eef1f044ddfbe0f145031d80470e22ffa63dc24a07605ee5c0b3b1b0d216e10ee28a1db78cd723df9812d3ec2585beaaa9f0844e1";

nano_models.forEach(function (model) {
  test(
    "[Nano " + model.letter + "] Kelp Claim LST",
    zemu(model, async (sim, eth) => {
      const serializedTx = txFromEtherscan(inputData);

      const tx = eth.signTransaction("44'/60'/0'/0", serializedTx);

      const right_clicks = model.letter === "S" ? 6 : 4;

      // Wait for the application to actually load and parse the transaction
      await waitForAppScreen(sim);
      // Navigate the display by pressing the right button `right_clicks` times, then pressing both buttons to accept the transaction.
      await sim.navigateAndCompareSnapshots(
        ".",
        testNetwork + "_kelp_claim_lst_" + model.name,
        [right_clicks, 0]
      );

      await tx;
    }),
    50000
  );
});
