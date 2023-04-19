use actix_web::{get, http::StatusCode, web, App, Error, HttpResponse, HttpServer, Responder};
use aws_sdk_lambda::{
    config::{Builder, Credentials, Region},
    primitives::Blob,
    Client,
};
use serde::{Deserialize, Serialize};
use serde_json::Value;
use std::env;

#[derive(Serialize)]
struct PredictionResult {
    cancel_prob: f32,
    divert_prob: f32,
    expct_delay: f32,
}

#[derive(Serialize, Deserialize, Debug)]
struct AWSArgs {
    name: String,
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(liveness).service(predict))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}

#[get("/")]
async fn liveness() -> impl Responder {
    HttpResponse::Ok().body("Alive!")
}

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[get("/predict")]
async fn predict() -> Result<impl Responder, Error> {
    let res = PredictionResult {
        cancel_prob: 0.0,
        divert_prob: 0.0,
        expct_delay: 0.0,
    };

    let client = get_aws_client("eu-north-1").unwrap();

    let req_struct = AWSArgs {
        name: "test".to_string(),
    };

    let req_args = Blob::new(serde_json::to_string(&req_struct)?);

    let res = client
        .invoke()
        .function_name("arn:aws:lambda:eu-north-1:621272430898:function:testfunction")
        .payload(req_args)
        .send()
        .await;

    match res {
        Ok(res) => {
            let bd = res.payload.as_ref().unwrap().as_ref().to_vec();
            let body = String::from_utf8_lossy(bd.as_slice());
            let value: Value = serde_json::from_str(&body)?;

            Ok(web::Json(value))
        }
        Err(e) => {
            panic!("Error: {:#?}", e)
        }
    }
}

fn get_aws_client(reg: &str) -> Result<Client, Box<dyn std::error::Error>> {
    let key_id = env::var("AWS_ACCESS_KEY_ID").expect("AWS_ACCESS_KEY_ID must be set");
    let key_secret = env::var("AWS_ACCESS_KEY_SECRET").expect("AWS_ACCESS_KEY_SECRET must be set");

    let cred = Credentials::new(key_id, key_secret, None, None, "loaded-from-custom-env");

    let region = Region::new(reg.to_string());
    let conf_builder = Builder::new().region(region).credentials_provider(cred);
    let conf = conf_builder.build();

    let client = Client::from_conf(conf);

    Ok(client)
}
