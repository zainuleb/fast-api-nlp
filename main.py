from typing import Optional

from nlp_model import nlp_text
from nlp_model import generate_query

from fastapi import FastAPI

app = FastAPI()


@app.get("/search/{str_query}")
def read_item(str_query: str):
    pred_value = nlp_text.preproc(str_query)
    return  generate_query.gen_query(pred_value)
    