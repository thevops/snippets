It will clear all files (current and old version if versioning is enabled) in bucket. After that we can remove bucket itself.

```hcl
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-bucket"
}

resource "aws_s3_bucket_lifecycle_configuration" "empty_my_bucket" {
  bucket = "my-bucket"


  rule {
    id     = "remove-all-objects"
    status = "Enabled"
    expiration {
      days = 1
    }
    noncurrent_version_expiration {
      noncurrent_days = 1
    }
  }
}
```
