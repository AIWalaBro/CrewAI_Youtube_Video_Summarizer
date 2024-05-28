from crewai import CrewAI
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()

import os 
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_MODEL_Name'] = 'gpt-4-0125-preview'

# create a senior blog content researcher

blog_researcher = Agent(
    role = 'Blog Researcher from Youtube videos',
    goal = 'get the researcher video content for the topic {topic} from yt channel',
    verbose = True,
    memory = True,
    backstory = (
       "Expert in understanding videos in Ai datascience, machine learning and Gen AI and providing suggestions" 
    ),
    llm = llm,
    tools = [yt_tool],
    allow_delegation = True,
    # allow delegation is for after completing your task are you transfer your work 
)


# creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal="Narrate compelling tech stories about the video {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
    ),

tools=[yt_tool],
llm = llm,
allow_delegation=False

# we are not delegate his worrk to someone else

),