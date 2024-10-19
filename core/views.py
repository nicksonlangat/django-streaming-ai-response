import json

from django.conf import settings
from django.http import StreamingHttpResponse
from django.shortcuts import render
from openai import OpenAI

API_KEY = settings.OPENAI_KEY
client = OpenAI(api_key=API_KEY)


def stream_opena_response(request):
    question = json.loads(request.body)["question"]

    def generate_stream():
        response_stream = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"{question}"}],
            stream=True,
        )

        for chunk in response_stream:
            if chunk.choices[0].delta.content is not None:
                yield (chunk.choices[0].delta.content)

    return StreamingHttpResponse(generate_stream(), content_type="text/plain")


def homepage(request):
    return render(request, "chat.html", {})
