# Changelog

## 2.0

Replace the `_onchange_builder_id` method (implementation) by a new method `_get_builder_domain`.\
This due to refactoring in the base Forms (`formio`) module, to solve a deprecation warning,
regarding a domain that may not be returned by an onchange method.

## 1.2

Add cascade delete on `crm_lead_id` field in `formio.form` model.

### 1.1

- Fix computed fields: access rights (compute_sudo).
- Fix Forms button in CRM Lead form: access right.

### 1.0

- Remove function `_onchange_partner_id` from `crm.lead` model. 
  If needed, this should be implemented upon write of `partner_id`.
  Issue: [\#147](https://github.com/novacode-nl/odoo-formio/issues/147)

### 0.1 until 0.4

Initial versions
