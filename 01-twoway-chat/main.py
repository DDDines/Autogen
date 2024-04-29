import autogen


def main():
    config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
    )

    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list": config_list
        }
    )

    user_proxy = autogen.UserProxyAgent(
        name="user",
        human_input_mode="TERMINATE",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False
        }
    )

    user_proxy.initiate_chat(assistant, message="Give a chart of the number of huskies adopted in london")


if __name__ == "__main__":
    main()