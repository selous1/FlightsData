/*
 * Test
 */

#![allow(clippy::result_large_err)]

use std::env;

use aws_sdk_lambda::{
    config::{Builder, Credentials, Region},
    primitives::Blob,
    Client,
};

use serde::{Deserialize, Serialize};
use serde_json::Value;

const AWS_REGION: &str = "eu-north-1";

#[derive(Serialize, Deserialize, Debug)]
struct AWSResponse {
    body: String,
    status_code: i32,
}

#[derive(Serialize, Deserialize, Debug)]
struct Args {
    name: String,
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    match env::var("AWS_ACCESS_KEY_ID") {
        Ok(val) => println!("{}: {}", "AWS_ACCESS_KEY_ID", val),
        Err(e) => println!("couldn't interpret {}: {}", "AWS_ACCESS_KEY_ID", e),
    }

    match env::var("AWS_ACCESS_KEY_SECRET") {
        Ok(val) => println!("{}: {}", "AWS_ACCESS_KEY_SECRET", val),
        Err(e) => println!("couldn't interpret {}: {}", "AWS_ACCESS_KEY_SECRET", e),
    }

    let a = Args {
        name: "help".to_string(),
    };
    let req_args = Blob::new(serde_json::to_string(&a)?);

    let client = get_aws_client(AWS_REGION)?;

    let res = client
        .invoke()
        .function_name("arn:aws:lambda:eu-north-1:621272430898:function:testfunction")
        .payload(req_args)
        .send()
        .await?;

    let bd = res.payload.as_ref().unwrap().as_ref().to_vec();
    let body = String::from_utf8_lossy(bd.as_slice());
    let value: Value = serde_json::from_str(&body)?;

    println!("res: {:?}", value);

    print!("its done!");

    Ok(())
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
