resource "azurerm_network_security_group" "azure_nsg_terraform" {
  name                = "nsg-${var.service_name}"
  location            = var.location_region
  resource_group_name = azurerm_resource_group.azure_resource_group_vnet.name

  security_rule {
    name                       = "SSH"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

   security_rule {
    name                       = "Jupyter"
    priority                   = 101
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "8888"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  tags = local.default_tags
}

resource "azurerm_subnet_network_security_group_association" "azure_snsga_terraform" {
  subnet_id                 = azurerm_subnet.azure_subnet_terraform.id
  network_security_group_id = azurerm_network_security_group.azure_nsg_terraform.id
}
