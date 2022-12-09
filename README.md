# Cisco ACI Ansible playground
Repo for testing Ansible playbooks on the ACI simulator.

## Provisioning the sandbox
1. Run __sandbox-bootstrap-register-switches.yml__: This will discover the switches as the APIC discovers them.
2. Run __sandbox-bootstrap-register-fabrid.yml__: This will create the following:
  * Leaf switch profiles
  * Leaf interface profiles
  * One IPG for single ports and one for a vPC
  * One access port selector on each switch
  * One vPC port selector on the shared leaf interface profile
3. Run __sandbox-bootstrap-register-tenant.yml__: This will create a tenant, VRF, BD, AP, EPG, and one static path binding per access port selector (three total)

```
ansible-playbook sandbox-bootstrap-register-switches.yml --extra-vars "apic=aci.vm.jm"

ansible-playbook sandbox-bootstrap-fabric.yml --extra-vars "apic=aci.vm.jm"

ansible-playbook sandbox-bootstrap-tenant.yml --extra-vars "apic=aci.vm.jm"
```
