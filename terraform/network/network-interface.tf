resource "azurerm_network_interface" "azure_nic" {
  name                = "nic-${var.service_name}"
  location            = azurerm_resource_group.azure_resource_group_vnet.location
  resource_group_name = azurerm_resource_group.azure_resource_group_vnet.name

  ip_configuration {
    name                          = "public-ip-${var.service_name}"
    subnet_id                     = azurerm_subnet.azure_subnet_terraform.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.azure_ip.id
  }

  tags = local.default_tags
}

# NETWORK INTERFACE SECURITY GROUP ASSOCIATION

resource "azurerm_network_interface_security_group_association" "azure_nisga" {
  network_interface_id      = azurerm_network_interface.azure_nic.id
  network_security_group_id = azurerm_network_security_group.azure_nsg_terraform.id
}
