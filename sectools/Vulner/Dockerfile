FROM kalilinux/kali-rolling
RUN echo "deb http://old.kali.org/kali sana main non-free contrib" >> ./etc/apt/sources.list
RUN apt-get update && apt-get -yu dist-upgrade -y
WORKDIR /vulscanner
RUN apt-get install -y \
  python2.7 \
  wget \
  dmitry \
  dnsrecon \
  wapiti \
  nmap \
  sslyze \
  dnsenum \
  wafw00f \
  golismero \
  dirb \
  host \
  lbd \
  xsser \
  dnsmap \
  dnswalk \
  fierce \
  davtest \
  whatweb \
  nikto \
  uniscan \
  whois \
  theharvester

RUN wget -O rapidscan.py https://raw.githubusercontent.com/FakeSmileUX/VulScanner/master/vulscanner.py && chmod +x vulscanner.py
RUN ln -s /vulscanner/vulscanner.py /usr/local/bin/rapidscan
WORKDIR /reports
ENTRYPOINT ["vulscanner"]
