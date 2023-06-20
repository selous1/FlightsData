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

FROM ubuntu:latest

# Import from builder.
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