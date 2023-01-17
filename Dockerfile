FROM python:3.8

WORKDIR '/app'
COPY . /app

RUN pip install streamlit

EXPOSE 8501
EXPOSE 8080

CMD ["streamlit", "run", "Code_Smashers.py"]