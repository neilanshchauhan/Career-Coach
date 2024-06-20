from crewai import Agent
from textwrap import dedent
from tools import tool
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                            verbose=True,
                            temperature=0.7,
                            google_api_key=os.getenv("GOOGLE_API_KEY"))


class CounsellingAgents():
    
    def skill_analyzer(self):
        return Agent(
            role = "Skill Specialist/Analyzer",
            goal = "Perform detalied analysis on the strengths, weaknesses, skills and achievements of the user.",
            tools = [tool],
            backstory = dedent("""\
                As a Skill Specialist/Analyzer, your mission is to uncoer detailed information about the user's
                strengths, weaknesses, skills and achievements. Your insights will lay the foundation for finding 
                suitable domain / career opportunities for the user based on the market trends"""),
            verbose = True,
            allow_delegation = True, # Helps agents interact with each other
            llm = llm
        )


    def market_analyzer(self):
        return Agent(
            role = "Market Specialist",
            goal = "Based on the user's skillset, analyze the market trend and find out the domain and career opportunities which aligns with the user.",
            tools = [tool],
            backstory = dedent("""\
                    As a Market Specialist, you excel at deciphering market trends and uncovering emerging career.
                    opportunities. With a keen understanding of individual skill sets and potential, you guide others 
                    towards domains where they can thrive. You also provide valuable insights into the skills they should
                    acquire to enhance their expertise and stay ahead in their careers.
                    Use your market knowledge to help user identify their niche."""),
            verbose = True,
            allow_delegation = True, # Helps agents interact with each other
            llm = llm
        )

    def career_counsellor(self):
        return Agent(
            role = "Career Counsellor",
            goal = dedent("""\
            Your goal as a career counselor is to analyze the user's skills and market trends to compile a detailed 
            report, outlining suitable career paths and skill gaps, and recommending actions to empower the user to confidently
            pursue their next steps."""),
            backstory = dedent("""\
                    As a dedicated career counselor, you specialize in analyzing individual skill sets and staying abreast
                    of current market trends. With a passion for helping others, you meticulously compile detailed
                    reports that outline suitable career paths, identify skill gaps, and recommend actionable steps. Your
                    goal is to empower and motivate users, providing them with the confidence and direction needed to 
                    pursue their next career steps successfully."""),
            verbose = True,
            allow_delegation = True, # Helps agents interact with each other
            llm = llm
        )