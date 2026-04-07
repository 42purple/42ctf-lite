FROM debian:trixie AS build

RUN apt update && apt install -y gcc gcc-multilib
COPY ./ /pwn
WORKDIR /pwn

RUN gcc -m32 -no-pie -fno-stack-protector -ggdb -mpreferred-stack-boundary=2 -z execstack pwn-2.c -o pwn

FROM debian:trixie

RUN apt update && apt install -y socat gcc-multilib

COPY --from=build /pwn/pwn /home/pwnme/pwn
RUN groupadd pwnme && \
    useradd -ms /bin/bash -u 1234 -g pwnme pwnme
RUN chmod +x /home/pwnme/pwn    

COPY ./flag.txt /home/pwnme/flag.txt

USER pwnme
WORKDIR /home/pwnme

CMD ["socat","-dd", "-T20", "TCP-LISTEN:9000,reuseaddr,fork", "EXEC:/home/pwnme/pwn,pty,stderr,setsid,sigint,sane"]