terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.26.0"
    }
  }

  backend "container" {  }
}

module "azure_network" {
  source = "./network"

  cidr_vpc        = "10.0.0.0/16"
  cidr_subnet     = "10.0.1.0/24"
  service_name    = var.service_name
  location_region = var.location_azure_region
}