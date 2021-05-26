FROM continuumio/anaconda3:4.4.0
MAINTAINER harish, harishwar.patlolla@gmail.com
COPY . probability_predict_dockerized/
EXPOSE 5000
WORKDIR probability_predict_dockerized/
RUN pip install -r requirements.txt
CMD python prob_predict_api.py