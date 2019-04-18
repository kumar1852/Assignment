FROM python:2.7
MAINTAINER lkdevops27@gmail.com
RUN  easy_install pip && pip install requests
COPY . /src
EXPOSE 90
CMD ["python","/src/p.py"]

