import google.generativeai as genai
import json
import time


genai.configure(api_key="")




model = genai.GenerativeModel('gemini-1.5-flash')


def analyze_startup(description):
  clean_desc=description.encode('utf-8', 'ignore').decode('utf-8')
  prompt = """
  Act as a Latin America-focused startup strategist and implementation expert, Only for hispanic countries. I will describe a startup idea to you, and your only output must be a JSON with the following structure:

  {{
    "feasibility_analysis": "A brief assessment of how this startup idea can be built and tailored for the Latin American market, including key considerations like market size, cultural nuances, and economic factors.",
    "implementation_plan": {{
      "technical_complexity": "A score from 0 to 10, evaluating the complexity of the technical requirements to build this solution in Latin America, where 0 represents very complex technologies or infrastructure challenges and 10 represents straightforward implementation.",
      "market_adaptability": "A score from 0 to 10, assessing how well this idea aligns with Latin American market dynamics, including demand, accessibility, and regional preferences. For example, 0 could represent a startup heavily reliant on advanced robotics in a region with limited technological infrastructure, while 10 could represent a simple, high-demand service like food delivery tailored to local tastes and customs. If the product is developer-oriented, the score should be a lot lower, reflecting the smaller target audience and potential market size in the region.",
      "mvp": "A concise description of how to test or validate this idea as a minimum viable product (MVP) in the Latin American market."
    }}
  }}
  Key definitions:

  technical_complexity: Measures the challenge in developing or scaling the technical aspects of the solution in Latin America, considering infrastructure, talent, and tools. Only for spanish speaking countries.
  market_adaptability: Reflects the alignment of the startup's value proposition with Latin American market trends and needs.
  mvp: A clear and practical approach to creating a minimum viable product (MVP) to test or validate the idea with minimal resources.

  Your response must strictly adhere to this JSON format and nothing else. Now, here is the startup description: {}
  """.format(clean_desc)

  print(clean_desc)
  print('-----')
  
  response = model.generate_content(prompt)
  print(response.text)

  print("-----------------------------------------------")
  return response.text



descripti="""
        "description": "0\u00a0http://www.pearsonlabs.aiAI agents to automate corporate transactionsPearson builds AI agents to automate corporate transactions. Large law firms use us to run gigantic books of businesses with AI, reducing their cost of delivery 40-60%. We work with Orrick as our first design partner, starting with M&A due diligence and financings. $3-6T dollars flow through corporate transactions a year and lawyers take home 1-3% as their cut for every transaction ($150B / year). In the long run, we will capture 50% of the corporate transaction market with the top 30 law firms. We will then provide our AI to companies so they can execute these transactions themselves.Pearson LabsFounded:2024Team Size:2Location:San FranciscoGroup Partner:Nicolas DessaigneActive FoundersStephanie Young, FounderCofounder and CEO at Pearson, AI to automate corporate legal transactions (M&A, IPOs, financings). Previously built Riva, AI bots to help employees negotiate job offers with the mission to even gender and racial pay gaps. Went through a M&A with that company which inspired this company. ex-Google, Lyft, Stanford (4 degrees from Stanford in just over 6 years).Stephanie YoungPearson Labs\u00a0Qi Yang, FounderQi is the Co-Founder and CTO of Pearson Labs. MIT PhD and former Meta AI researcher, led Themis AI's research team with a focus on mitigating hallucinations in AI systems.Qi YangPearson Labs\u00a0Company LaunchesPearson Labs - we build AI agents to help law firms execute corporate transactionsTL;DR \u2014 Hey everyone! We\u2019re Steph and Qi, and we\u2019re building Pearson - AI agents to help law firms and companies execute corporate transactions. We help rainmakers at law firms run gigantic books of businesses with AI. AI Researcher & Exited Founder Steph got 4 degrees from Stanford including CS+MBA from Stanford in just over 6 years  Product at Google and Lyft Built and sold an AI company, which inspired Pearson  Qi is MIT PhD, and Meta AI researcher  Then joined an MIT startup, Themis, to do research in reducing hallucinations in LLMs   (Moving to sunny SF for YC \ud83d\ude0a, but yet it\u2019s still cold \ud83e\udd76)  Unique Insight  Clients  Are increasingly unhappy with law firms charging them $1500-2000 an hour Refuse to talk to their law firms out of fear of being charged thousands of dollars for a single question Increasingly rotate work between several law firms leaving law firms out of the loop   Law Firms  Hourly rates increase every year and yet clients are asking in reduction in prices Have to write off hours and slash rates in order to win and retain clients Many corporate transactions are done at a loss to the law firm in order to win relationships and future business    Pearson AI: Built around corporate documents + agents for different transactions What you see below is our agent executing a M&A due diligence. This would normally have taken an associate days to weeks to do manually and would still have mistakes but we can perform the task in a few hours.  Come talk to us! stephanie@pearsonlabs.ai and qi@pearsonlabs.ai "

"""

analyze_startup(description=descripti)




with open('companies_with_description.json', 'r') as infile:
    data = json.load(infile)





counter =0


for item in data:
  if counter ==3:
    break
  elif "description" in item:
      time.sleep(4)
      counter += 1
      print(counter)
      result = analyze_startup(item["description"])
      item["all"] = result
      print(counter)
  

# Save the updated data to a JSON file
with open("companies_score.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print("Data saved to companies_score.json")

"""
falta
1. extraer json y return de feasibility_analysis,.....
"""