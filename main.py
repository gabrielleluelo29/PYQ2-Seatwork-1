from pyscript import document, display

def checkName(e);
    
    pas_ssers= ["Gabrielle Luelo", "Maiselle Marin", "Tanya Amortizado", "Lexie Cunanan", "Carlos David"]

    First_name=document.getElementbyId("First name:").value
    name= "Gabrielle Luelo"
    
    confirm_pas = First_name in pas_ssers

    message = (f'Congratulations {Candidates name}! You are now part of the Rainbow Catering Club.') 
    message = (f'Sorry {Candidates name}, your name is not on the list.')

    document.getElementbyId("acm").innerHTML =
    message[confirm_pas]