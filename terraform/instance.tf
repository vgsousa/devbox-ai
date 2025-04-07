
resource "azurerm_resource_group" "azure_resource_group_instance" {
  name     = "rg-${var.service_name}"
  location = var.location_azure_region

  tags = local.default_tags
}

resource "azurerm_linux_virtual_machine" "azure_instance_terraform" {
  name                = "instance-${var.service_name}"
  resource_group_name = azurerm_resource_group.azure_resource_group_instance.name
  location            = azurerm_resource_group.azure_resource_group_instance.location
  size                = "Standard_B2s"
  admin_username      = "devbox"
  network_interface_ids = [
    module.azure_network.azure_network_interface_id,
  ]

  admin_ssh_key {
    username   = "devbox"
    public_key = var.azure_key_pub
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  tags = local.default_tags
}
