/*
 * Test
 */

#![allow(clippy::result_large_err)]

use std::env;

use aws_sdk_lambda::{
    config::{Builder, Credentials, Region},
    Client,
};

const AWS_REGION: &str = "eu-north-1";

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

    let client = get_aws_client(AWS_REGION)?;

    let res = client
        .invoke()
        .function_name("arn:aws:lambda:eu-north-1:621272430898:function:testfunction")
        .send()
        .await?;

    println!("res: {:?}", res);

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
