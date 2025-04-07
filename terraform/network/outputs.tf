output "azure_subnet_id" {
  description = "ID da Subnet criada na Azure"
  value       = azurerm_subnet.azure_subnet_terraform.id
}

output "azure_security_group_id" {
  description = "ID da Network Security Group criada na Azure"
  value       = azurerm_network_security_group.azure_nsg_terraform.id
}

output "azure_network_interface_id" {
  description = "ID da Network Interface criada na Azure"
  value       = azurerm_network_interface.azure_nic.id
}

