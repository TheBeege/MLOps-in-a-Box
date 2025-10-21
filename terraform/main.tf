terraform {
    required_providers {
    zenml = {
            source = "zenml-io/zenml"
        }
    }
}

provider "zenml" {
    # Configuration options will be loaded from environment variables:
    # ZENML_SERVER_URL
    # ZENML_API_KEY
    # ZENML_API_TOKEN
}
