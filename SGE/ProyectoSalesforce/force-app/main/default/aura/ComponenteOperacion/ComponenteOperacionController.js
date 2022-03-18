({
    calculando : function(component, event, helper) {
        var operando1 = component.find("operando1").getElement().value;
        var operando2 = component.find("operando2").getElement().value;
        var simbolo = component.find("simbolo").getElement().value;

        var appevent =$A.get("e.c:EventoOperacion");
        appevent.setParams({"operando1":operando1, "operando2": operando2, "simbolo": simbolo});

        appevent.fire();
    }
})