terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

# Configure the GitHub Provider

provider "github" {
  token = "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"
  owner = "rakesh4145"
}

resource "github_repository" "github-repo-1" {
  name        = "terraform-demo-1"
  description = "My awesome codebase"

  visibility = "public"
}
