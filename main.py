from crewai import Agent

researcher = Agent(
    role = "Resercher",
    goal = "Find useful information",
    backstory = "You are an expert AI researcher",
    verbose =True
)
print(researcher)