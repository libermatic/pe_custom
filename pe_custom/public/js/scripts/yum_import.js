async function save(frm) {
  await frm.save();
  frm.refresh();
}

export default {
  refresh: function(frm) {
    frm.disable_save();
    const { sales, status } = frm.doc;
    if (sales && !status) {
      frm.page.set_primary_action(__('Start Import'), function() {
        frm.savesubmit();
      });
    }
  },
};
