from pydantic import BaseModel
from langgraph.graph.message import add_messages
from typing import Annotated ,TypedDict

class RagToolScheme(BaseModel):
    question: str

class QuestionRequest(BaseModel):
    question: str



if __name__=="__main__":
    
    x=RagToolScheme(question= 'Hi')
    print(x)
    print(type(x))
    print(x.question)