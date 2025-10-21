variable "zenml_server_url" {
    type = string
    default = "http://localhost:8080"
}

variable "zenml_api_token" {
    type = string
    sensitive = true
    default = ""
}

variable "zenml_api_key" {
    type = string
    sensitive = true
    default = ""
}
