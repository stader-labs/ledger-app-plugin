#include "plugin.h"

// EDIT THIS: Adapt this function to your needs! Remember, the information for tokens are held in
// `msg->token1` and `msg->token2`. If those pointers are `NULL`, this means the ethereum app didn't
// find any info regarding the requested tokens!
void handle_provide_token(ethPluginProvideInfo_t *msg) {
    context_t *context = (context_t *) msg->pluginContext;

    // FOR KELP_INITIATE_WITHDRAW, assign the ticker if available,
    // else it will be ETH, already set during init_contract
    if (msg->item1) {
        strlcpy(context->ticker, (char *) msg->item1->token.ticker, sizeof(context->ticker));
    }
    msg->result = ETH_PLUGIN_RESULT_OK;
}
