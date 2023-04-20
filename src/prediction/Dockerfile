FROM rust

COPY ./src/prediction/prediction-ms/target/x86_64-unknown-linux-musl/release/prediction-ms /bin/docker-program

EXPOSE 8080
CMD ["/bin/docker-program"]