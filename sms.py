from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/sms/")
async def receive_sms(request: Request):
    form_data = await request.form()
    from_number = form_data.get('From')
    body = form_data.get('Body')

    response = MessagingResponse()
    response.message("Hello World")

    return PlainTextResponse(str(response))