from crewai import Task
from textwrap import dedent

class CounsellingTasks():
    def skill_analysis_task(self, user_info):
        return Task(
            description = dedent(f"""\
                Analyze the strengths, weaknesses, skills and achievements of the user.

                input : {user_info}"""),
                
                expected_output = dedent(f"""\
                    A detailed report summarizing key findings about the user, highlighting the information
                    that could be important for the counselling"""),
                agent = agent,
                async_execution = False
        )

    def domain_analysis_task(self, user_info):
        return Task(
            description = dedent(f"""\
                Leveraging the user's strengths, skills, and achievements, recommend 
                suitable career paths within aligned domains and markets. Explore job 
                opportunities that match the user's profile and suggest promising areas
                for further exploration based on current trends and the user's interests.
                Also explore the trending skills which the user can learn which would be 
                highly beneficial with respect to the domain.

                input : {user_info}"""),
                
                expected_output = dedent(f"""\
                    An insightful analysis that identifies major trends in the market and
                    recommends the domain that aligns with the user's skillset and also suggests
                    skills and career pathways which could be beneficial for the user,
                    and can be important for the counselling"""),
                agent = agent,
                async_execution = False
        )

    def counselling_task(self, user_info):
        return Task(
            description = dedent(f"""\
                Compile the user's skill analysis, identified market/domain matches, and weaknesses
                from previous tasks. Craft a detailed report outlining suitable career paths and 
                highlighting skill gaps.  Recommend specific actions to address weaknesses and 
                bridge these gaps.  This report should motivate and empower the user to determine 
                their next career steps and confidently pursue them.
                input : {user_info}"""),
                
                expected_output = dedent(f"""\
                   Generate a comprehensive career counselling report summarizing the user's 
                   strengths, skills, and recommended career paths within suitable market sectors. 
                   Identify skill gaps and weaknesses, suggesting actionable steps to bridge
                   those gaps and empower the user to take the next steps in their career journey."""),
                agent = agent,
                async_execution = False
        )