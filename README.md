# Cisco ACI Ansible playground
Repo for testing Ansible playbooks on the ACI simulator.

## Provisioning the sandbox
1. Run __sandbox-bootstrap-register-switches.yml__: This will register the switches as the APIC discovers them. It will then create a snapshot and modify the bootstrap-fabric playbook with the name of the snapshot file.
2. Run __sandbox-bootstrap-fabric.yml__: This will create the following:
    * Leaf switch profiles
    * Leaf interface profiles
    * One IPG for single ports and one for a vPC
    * One access port selector on each switch
    * One vPC port selector on the shared leaf interface profile
3. Run __sandbox-bootstrap-tenant.yml__: This will create three tenants, VRFs, BDs, APs, EPGs, and static path bindings.

```
ansible-playbook sandbox-bootstrap-register-switches.yml --extra-vars "apic=aci-sandbox"

# running this playbook
ansible-playbook sandbox-bootstrap-control.yml --extra-vars "apic=aci-sandbox"

# is equivalent to running these two playbooks
ansible-playbook sandbox-bootstrap-fabric.yml --extra-vars "apic=aci-sandbox"
ansible-playbook sandbox-bootstrap-tenant.yml --extra-vars "apic=aci-sandbox"
```
