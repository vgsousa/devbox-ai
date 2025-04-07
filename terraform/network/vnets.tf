resource "azurerm_virtual_network" "azure_vnet_terraform" {
  name                = "vnet-${var.service_name}"
  location            = var.location_region
  resource_group_name = azurerm_resource_group.azure_resource_group_vnet.name
  address_space       = ["${var.cidr_vpc}"]

  tags = local.default_tags
}