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
// Test from replayed transaction: https://etherscan.io/tx/0xa5458f18af5bd00d7bda4332f33af93e0f7cd7294c6715dbf5a4c143f0a1d6e3
const inputData =
  "0x02f89001078439d106808502f335de57830227ce9462de59c08eb5dae4b7e6f7a8cad3006d6965ec1680a46dbaf9ee000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeec080a0e5b528d407765077dc056f703a6b616bff83ed970eb2250615e94347846ad133a040c023c952756e5aa6d25dec78cb7f67f9ebb5f42de588d6e46c34e2976f6308";

nano_models.forEach(function (model) {
  test(
    "[Nano " + model.letter + "] Kelp Claim ETH",
    zemu(model, async (sim, eth) => {
      const serializedTx = txFromEtherscan(inputData);

      const tx = eth.signTransaction("44'/60'/0'/0", serializedTx);

      const right_clicks = model.letter === "S" ? 6 : 4;

      // Wait for the application to actually load and parse the transaction
      await waitForAppScreen(sim);
      // Navigate the display by pressing the right button `right_clicks` times, then pressing both buttons to accept the transaction.
      await sim.navigateAndCompareSnapshots(
        ".",
        testNetwork + "_kelp_claim_eth_" + model.name,
        [right_clicks, 0]
      );

      await tx;
    }),
    50000
  );
});
