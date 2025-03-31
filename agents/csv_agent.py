import os
import pandas as pd
from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def create_episode_csv_agent():
    csv_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "../static/episode_info.csv"))

    df = pd.read_csv(csv_path)

    return create_pandas_dataframe_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        df=df,
        verbose=True,
        allow_dangerous_code=True,
    )
