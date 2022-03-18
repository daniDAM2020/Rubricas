({
    calculo : function(component, event, helper) {
        var operando1 = event.getParam("operando1");
        var operando2 = event.getParam("operando2");
        var simbolo = event.getParam("simbolo");

        if(simbolo == "+")
            component.find("resultado").getElement().value = parseInt(operando1) + parseInt(operando2);
        else if(simbolo == "-")
            component.find("resultado").getElement().value = operando1 - operando2;
        else if(simbolo == "*")
            component.find("resultado").getElement().value = operando1 * operando2;
        else if(simbolo == "/")
            component.find("resultado").getElement().value = operando1 / operando2;
        
        
    }

})