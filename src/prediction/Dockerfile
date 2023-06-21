FROM rust:latest AS builder

RUN rustup target add x86_64-unknown-linux-musl
RUN apt update && apt install -y musl-tools musl-dev
RUN update-ca-certificates

# Create appuser
ENV USER=doc
ENV UID=10001

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"

WORKDIR /doc

COPY ./src/prediction/prediction-ms/  .

RUN cargo build --target x86_64-unknown-linux-musl --release

RUN ls -R

# ---- 

FROM scratch

# Import from builder.
# https://stackoverflow.com/questions/65297751/docker-container-with-golang-http-get-error-certificate-signed-by-unknown-autho
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

USER doc:doc

WORKDIR /doc

# Copy our build
COPY --from=builder /doc/target/x86_64-unknown-linux-musl/release/prediction-ms ./

USER doc:doc

CMD ["/doc/prediction-ms", ">>", "/proc/1/fd/1"]

# docker build -t prediction:latest -f src/prediction/Dockerfile .
# docker tag prediction jbrazf/predict:v1.0
# docker push jbrazf/predict:v1.0
# docker run --name pred -p 5000:5000 -d prediction:latest
# https://serverfault.com/questions/599103/make-a-docker-application-write-to-stdout
# https://stackoverflow.com/questions/30494050/how-do-i-pass-environment-variables-to-docker-containers
#docker run -p 5000:5000 -d -e AWS_ACCESS_KEY_ID="$(cat .secrets/AWS_ACCESS_KEY_ID.txt)" -e AWS_ACCESS_KEY_SECRET="$(cat .secrets/AWS_ACCESS_KEY_SECRET.txt)" -e AWS_REGION='eu-north-1' -e AWS_FUNCTION_NAME='arn:aws:lambda:eu-north-1:621272430898:function:testfunction' --name pred prediction:latest