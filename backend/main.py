from fastapi import FastAPI

klu = FastAPI(title="AI Tutor",
              description="AI Tutor pbl project",
              version="1.0.0")

@klu.get("/")
def home():
    return {"message": "Welcome to the AI Tutor project"}

@klu.get("/demo")
def demo():
    return {"message" : "KL Univerrsity"}

@klu.get("/askquestion")
def ask():
    return {"message" : "what is LLM","Answer" :"Large Language Model"}