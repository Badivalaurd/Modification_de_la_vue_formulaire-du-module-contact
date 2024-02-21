odoo.define('custom_contact', function (require) {
    "use strict";

    var core = require('web.core');
    var ContactForm = require('contacts.form');

    var CustomContactForm = ContactForm.extend({
        /**
         * Ajoute des événements aux champs CNI et NUI.
         */
        init: function () {
            this._super.apply(this, arguments);

            this.$el.find('[name="cni"]').on('change', this._onCniChange.bind(this));
            this.$el.find('[name="niu"]').on('change', this._onNiuChange.bind(this));
        },

        /**
         * Vérifie le format du numéro CNI.
         */
        _onCniChange: function () {
            var cni = this.$el.find('[name="cni"]').val();
            if (cni.length != 11) {
                this.do_warn(_("Le numéro CNI doit comporter 11 caractères."));
            }
        },

        /**
         * Vérifie le format du numéro NUI.
         */
        _onNiuChange: function () {
            var niu = this.$el.find('[name="niu"]').val();
            if (niu.length != 14) {
                this.do_warn(_("Le numéro NUI doit comporter 14 caractères."));
            }
        },
    });

    core.action_registry.add('custom_contact_form', CustomContactForm);

    return CustomContactForm;
});
