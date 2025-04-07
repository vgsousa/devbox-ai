variable "cidr_vpc" {
  description = "Cidr para a VPC criada na Azure"
  type        = string
}

variable "cidr_subnet" {
  description = "Cidr para a Subnet criada na Azure"
  type        = string
}

variable "service_name" {
  description = "Nome dos recursos a serem criados"
  type        = string
}

variable "location_region" {
  description = "Região onde os recursos serão criados na Azure"
  type        = string
}