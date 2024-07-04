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
// Test from replayed transaction: https://etherscan.io/tx/0xa44d01da432225b7ad2cc49b0160d57464439107044af3497a9b71d7677c82c7
const inputData =
  "0x02f8b001318421bef4e984dfce82df83105db09462de59c08eb5dae4b7e6f7a8cad3006d6965ec1680b844c8393ba9000000000000000000000000a35b1b31ce002fbf2058d22f30f95d405200a15b0000000000000000000000000000000000000000000000000f99f5f1987e8000c001a05dd079fce787f4a03da05f8ba68d6a1abe3d094a6985c27dab843e84eff027b9a005fc6255e49140ca4d76477e6a4f3d6ae09d61f83a56655e166e960683d3127e";

nano_models.forEach(function (model) {
  test(
    "[Nano " + model.letter + "] Kelp Unstake LST",
    zemu(model, async (sim, eth) => {
      const serializedTx = txFromEtherscan(inputData);

      const tx = eth.signTransaction("44'/60'/0'/0", serializedTx);

      const right_clicks = model.letter === "S" ? 7 : 5;

      // Wait for the application to actually load and parse the transaction
      await waitForAppScreen(sim);
      // Navigate the display by pressing the right button `right_clicks` times, then pressing both buttons to accept the transaction.
      await sim.navigateAndCompareSnapshots(
        ".",
        testNetwork + "_kelp_unstake_lst_" + model.name,
        [right_clicks, 0]
      );

      await tx;
    }),
    50000
  );
});
