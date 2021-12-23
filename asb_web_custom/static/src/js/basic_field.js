odoo.define('asb_web.BasicFields', function(require){
    "use strict";

    const BasicFields = require('web.basic_fields')
    const core = require('web.core')

    const parameters = core._t.database.parameters;
    const NumericField = BasicFields.NumericField;
    const MonetaryField = BasicFields.FieldMonetary;
    const FloatField = BasicFields.FieldFloat;

    NumericField.include({
        init: function(){
            this._super.apply(this, arguments);
            this.thousands_sep = parameters.thousands_sep || ",";
            this.decimal_point = parameters.decimal_point || ".";
            this.reg_exp = new RegExp("[^" + this.decimal_point + "-\\d]", "g");
        },
    })

    MonetaryField.include({
        _onInput: function(){
            this._super()
            $(this.$input).val( (i, value) => {
                let origin_value = value.replace(this.reg_exp, "").replace(/\B(?=((\d{3})+(?!\d)))/g, this.thousands_sep)
                let new_value = origin_value.split(this.decimal_point)
                const re = new RegExp("\\" + this.thousands_sep, "g")
                if(new_value.length > 1){
                    new_value = new_value[0] + this.decimal_point + new_value[1].replace(re, "")
                }
                return new_value;
            })
        },
    })

    FloatField.include({
        _onInput: function(){
            this._super()
            if(this.formatType !== "float"){
                return;
            }
            $(this.$input).val( (i, value) => {
                let origin_value = value.replace(this.reg_exp, "").replace(/\B(?=((\d{3})+(?!\d)))/g, this.thousands_sep)
                let new_value = origin_value.split(this.decimal_point)
                const re = new RegExp("\\" + this.thousands_sep, "g")
                if(new_value.length > 1){
                    new_value = new_value[0] + this.decimal_point + new_value[1].replace(re, "")
                }
                return new_value;
            })
        },
    })
})