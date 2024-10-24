from swarm import Swarm, Agent

# Initialize Swarm client
client = Swarm()


# News Agent to fetch news
plot_agent = Agent(
    name="Plot Developer Assistant",
    instructions="You are a Plot Developer for writing stories",
    model="llama3.2"
)

# Editor Agent to edit news
character_agent = Agent(
    name="Character Developer Assistant",
    instructions="You are a Character Developer for writing stories",
    model="llama3.2"
)

setting_agent = Agent(
    name="Setting Creator Assistant",
    instructions="You are a Setting Creator for writing stories",
    model="llama3.2"
)

dialogue_agent = Agent(
    name="Dialogue Writer Assistant",
    instructions="You are a Dialogue Writer for writing stories",
    model="llama3.2"
)

conflict_agent = Agent(
    name="Conflict Generator Assistant",
    instructions="You are a Conflict Generator for writing stories",
    model="llama3.2"
)

editor_agent = Agent(
    name="Editor Assistant",
    instructions="You are an Editor for writing stories",
    model="llama3.2"
)
# 3. Create workflow

def run_news_workflow(topic):
    print("Running news Agent workflow...")
    
    # Step 1: Fetch news
    news_response = client.run(
        agent=plot_agent,
        messages=[{"role": "user", "content": f"Write a story about {topic}"}],
    )
    
    raw_news = news_response.messages[-1]["content"]
    
    # Step 2: Pass news to editor for final review
    edited_news_response = client.run(
        agent=character_agent,
        messages=[{"role": "user", "content": raw_news }],
    )
    
    raw_editor_news = edited_news_response.messages[-1]["content"]
    
    # Step 2: Pass news to editor for final review
    edited_setting_response = client.run(
        agent=setting_agent,
        messages=[{"role": "user", "content": raw_editor_news }],
    )

    raw_setting_news = edited_setting_response.messages[-1]["content"]
    
    # Step 2: Pass news to editor for final review
    edited_news_response = client.run(
        agent=editor_agent,
        messages=[{"role": "user", "content": raw_setting_news }],
    )

    return edited_news_response.messages[-1]["content"]

# Example of running the news workflow for a given topic
print(run_news_workflow("In a world where magic has been outlawed, a young sorcerer discovers an ancient artifact that could change everything."))