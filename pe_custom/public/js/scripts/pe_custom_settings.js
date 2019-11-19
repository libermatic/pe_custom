export default {
  refresh: function(frm) {
    frm.page.add_menu_item('Setup Defaults', async function() {
      try {
        await frappe.call({
          method: 'pe_custom.api.setup.setup_defaults',
          freeze: true,
          freeze_message: __('Setting up defaults...'),
        });
        frm.reload_doc();
        frappe.show_alert({
          message: __('Defaults setup successfully'),
          indicator: 'green',
        });
      } catch (e) {
        frappe.throw(__('Something happened. Unable to setup defaults.'));
      }
    });
  },
};
