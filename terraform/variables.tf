variable "service_name" {
  description = "Nome dos recursos a serem criados"
  type        = string
  default     = "devbox-ai"
}

variable "azure_key_pub" {
  description = "Chave pública para a máquina na Azure"
  type        = string
}

variable "location_azure_region" {
  description = "Região onde os recursos serão criados na Azure"
  type        = string
  default     = "East US"
}
