def findNext(number):

    # On accepte seulement l'ensemble des entiers
    if not isinstance(number, int) :
        return False

    # Conversion vers un "string"
    number_s = str(number)
    processing_negative_number = False
    swap_1 = None
    swap_2 = None

    # Si nombre entier negatif
    if number < 0 :
        number_s = str(abs(number))[::-1]
        processing_negative_number = True

    for i in range(len(number_s)- 1, 0, -1):
        if i != 0 :
            if number_s[i] > number_s [i-1]:
                swap_1 = i
                swap_2 = i-1
                break
 
    # Si aucun "swap" possible est detecte
    if not swap_1 :
        return number

    # Interchange les chiffres
    number_as_list = list(number_s)
    number_as_list[swap_1], number_as_list[swap_2] = number_as_list[swap_2], number_as_list[swap_1]
    number_s = ''.join(number_as_list)
    
    # Si on avait un entier negatif au depart
    if processing_negative_number :
        return int(number_s[::-1]) * -1
    
    # We might have a true here
    try:
        return int(number_s)
    except:
        return False