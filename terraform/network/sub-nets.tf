resource "azurerm_subnet" "azure_subnet_terraform" {
  name                 = "subnet-${var.service_name}"
  resource_group_name  = azurerm_resource_group.azure_resource_group_vnet.name
  virtual_network_name = azurerm_virtual_network.azure_vnet_terraform.name
  address_prefixes     = ["${var.cidr_subnet}"]
}
