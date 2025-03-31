from dotenv import load_dotenv
from agents.python_execute_agent import create_python_agent
from agents.csv_agent import create_episode_csv_agent
from agents.grand_agent import create_grand_agent

load_dotenv()


def main():
    print("Start...")

    python_agent = create_python_agent()
    csv_agent = create_episode_csv_agent()
    grand_agent = create_grand_agent(python_agent, csv_agent)

    print(
        grand_agent.invoke(
            {
                "input": "which season has the most episodes?",
            }
        )
    )

    # print(
    #     grand_agent.invoke(
    #         {
    #             "input": "Generate and save in current working directory 1 qrcode that point to `https://github.com/KoKocik1",
    #         }
    #     )
    # )


if __name__ == "__main__":
    main()
