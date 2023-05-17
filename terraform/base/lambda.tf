resource "aws_lambda_function" "example" {
  function_name    = "media_extracor"
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.handler"
  runtime          = "python3.11"
  architecture     = "arm64"
  filename         = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")
}