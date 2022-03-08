({
    fireComponentEvent : function(component, event) {
        var cmpEvent = cmp.getEvent("cmpEvent");
        cmpEvent.setParams({
            "message" : "Hello " +
            "World!" });
        cmpEvent.fire();
    }
})