# terraform {
#   backend "s3" {
#     bucket         = module.base.aws_s3_bucket.visda.id
#     key            = "terraform.tfstate"
#     region         = "ca-central-1"
#     dynamodb_table = module.base.aws_dynamodb_table.terraform-dynamodb-table
#   }
# }

terraform {
  backend "local" {
    path = "terraform/terraform.tfstate"
  }
}
