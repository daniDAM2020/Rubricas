({
    handleCmpEvent: function(component, event) {
        var message = event.getParam("message");
        cmp.set("v.messageTemplate", message);
        var EventsHandled = parseInt(cmp.get("v.numberOfEvents")) + 1;
        cmp.set("v.numberOfEvents", EventsHandled);
    }
})