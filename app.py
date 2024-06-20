from crewai import Crew
from tasks import CounsellingTasks
from agents import CounsellingAgents
from dotenv import load_dotenv

def main():
    load_dotenv()

    print("Welcome to Career Coach")
    user_info = input("Tell me about your skills, strengths and weaknesses")

    tasks = CounsellingTasks()
    agents = CounsellingAgents()

    # Create Agents
    skill_analyzer = agents.skill_analyzer()
    market_analyzer = agents.market_analyzer()
    career_counsellor = agents.career_counsellor()

    # Create Tasks
    skill_analysis_task = tasks.skill_analysis_task(skill_analyzer, user_info)
    domain_analysis_task = tasks.domain_analysis_task(market_analyzer, user_info)
    counselling_task = tasks.counselling_task(career_counsellor, user_info)

    domain_analysis_task.context[skill_analysis_task]
    counselling_task.context[skill_analysis_task,domain_analysis_task]

    # Create Crew

    crew = Crew(
        agents = [
            skill_analyzer,
            market_analyzer,
            career_counsellor
        ],
        
        tasks = [
            skill_analysis_task,
            domain_analysis_task,
            counselling_task
        ]
    )

    result = cre.kickoff()
    print(result)

if __name__ == "__main__":
    main()

