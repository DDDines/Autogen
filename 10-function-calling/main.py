from typing import Literal

import autogen
from typing_extensions import Annotated

config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gpt-3.5-turbo"]
    }
)

llm_config = {
    "config_list": config_list,
    "timeout": 120
}

currency_bot = autogen.AssistantAgent(
    name="currency_bot",
    system_message="For currency exchange tasks, only use the functions you have been provided with. Reply TERMINATE "
                   "when the task is done.",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5,
    code_execution_config=False
)

CurrencySymbol = Literal["USD", "EUR"]


def exchange_rate(base_currency: CurrencySymbol, quote_currency: CurrencySymbol) -> float:
    if base_currency == quote_currency:
        return 1.0
    elif base_currency == "USD" and quote_currency == "EUR":
        return 1 / 1.09
    elif base_currency == "EUR" and quote_currency == "USD":
        return 1 / 1.1
    else:
        raise ValueError(f"Unknown currencies: {base_currency}, {quote_currency}")


@user_proxy.register_for_execution()
@currency_bot.register_for_llm(description="Currency exchange calculator")
def currency_calculator(
        base_amount: Annotated[float, "Amount of currency in base_currency"],
        base_currency: Annotated[CurrencySymbol, "Base currency"] = "USD",
        quote_currency: Annotated[CurrencySymbol, "Quote currency"] = "EUR"
) -> str:
    quote_amount = exchange_rate(base_currency, quote_currency) * base_amount
    return f"{quote_amount} - {quote_currency}"


user_proxy.initiate_chat(
    currency_bot,
    message="Can you give me the answer to 2 + 2?"
)
