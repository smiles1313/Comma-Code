def comma(value)=
	sentence=""
	for i in value:
		if i != value[-1]:
			sentence+= i +', '


	return sentence