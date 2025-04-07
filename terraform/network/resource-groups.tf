
resource "azurerm_resource_group" "azure_resource_group_vnet" {
  name     = "rg-${var.service_name}"
  location = var.location_region

  tags = local.default_tags
}