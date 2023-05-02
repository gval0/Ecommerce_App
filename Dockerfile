FROM python:3.11

ADD product_info.py .
ADD product_data_base.py . 
ADD main.py .

CMD [ "python", "./main.py" ]