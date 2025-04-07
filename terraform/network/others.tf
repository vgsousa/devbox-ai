resource "azurerm_public_ip" "azure_ip" {
  name                = "public-ip-${var.service_name}"
  resource_group_name = azurerm_resource_group.azure_resource_group_vnet.name
  location            = azurerm_resource_group.azure_resource_group_vnet.location
  allocation_method   = "Dynamic"
  sku                 = "Basic"
  
  tags = local.default_tags
}
