FROM python:3.11

WORKDIR /Auto-Filter-Bot

COPY . /Auto-Filter-Bot

RUN pip install -r requirements.txt
RUN python -m spacy download fr_core_news_md


CMD ["python", "bot.py"]
