FROM baseware/python-pillow:3.7


WORKDIR /app
ADD . /app
RUN  python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt

COPY . .


