odoo.define('asb_web.ListViewPatch', function(require){

var ListController = require('web.ListController')
var ListView = require('web.ListView')

ListView.include({
    init: function(...arguments){
        this._super.apply(this, arguments)
        this.controllerParams.on_create = this.arch.attrs.on_create;
    },
});

ListController.include({
    init: function(parent, model, renderer, params){
        this._super.apply(this, arguments);
        this.on_create = params.on_create;
    },

    _onCreateRecord: function(ev){
        // override the parent function if on_create in attrs list view
        if (ev) {
            ev.stopPropagation();
        }
        var state = this.model.get(this.handle, {raw: true});
        if(this.on_create && typeof this.on_create === "string"){
        // execute the given action from list view
            this.do_action(this.on_create, {
                on_close: this.reload.bind(this, {}),
                additional_context: state.context,
            });
        } else {
            return this._super(ev);
        }
    },
});

});