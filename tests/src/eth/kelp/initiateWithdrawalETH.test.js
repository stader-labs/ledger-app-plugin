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
// Test from replayed transaction: https://etherscan.io/tx/0x5a6a235be8865c5989bd5f604e9f4c14c442e5db0ee06b64e93a74ead5b5b14c
const inputData =
  "0x02f8b00150839402a08501ccf6aae1830a78d19462de59c08eb5dae4b7e6f7a8cad3006d6965ec1680b844c8393ba9000000000000000000000000eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee000000000000000000000000000000000000000000000000015f021397cf0000c001a0b812d5b2183bd21ccde3765da1ad02a7233f835b01bc3519db9a123f84acbf38a0761578a1e66af567e40dcf4597af674956381fc85db0f2c9881f3f95eb863726";

nano_models.forEach(function (model) {
  test(
    "[Nano " + model.letter + "] Kelp Unstake ETH",
    zemu(model, async (sim, eth) => {
      const serializedTx = txFromEtherscan(inputData);

      const tx = eth.signTransaction("44'/60'/0'/0", serializedTx);

      const right_clicks = model.letter === "S" ? 7 : 5;

      // Wait for the application to actually load and parse the transaction
      await waitForAppScreen(sim);
      // Navigate the display by pressing the right button `right_clicks` times, then pressing both buttons to accept the transaction.
      await sim.navigateAndCompareSnapshots(
        ".",
        testNetwork + "_kelp_unstake_eth_" + model.name,
        [right_clicks, 0]
      );

      await tx;
    }),
    50000
  );
});
