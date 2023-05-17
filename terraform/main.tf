provider "aws" {
  region = "ca-central-1"
}

module "base" {
  source = "./base/main"
}