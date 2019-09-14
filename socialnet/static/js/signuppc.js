document.getElementById('strength').style.display = "none";
	function myFunction()
	{
		document.getElementById('strength').style.display = "block";
		var x  = document.getElementById('inp').value;
		var strengthbar = document.getElementById('strength');
		var y = 0;
		var txt = "password is "
		if(x.match(/[a-zA-z0-9][a-zA-z0-9]+/)!=null)
		{
			y += 1;
		}


		if(x.match(/[~<>?]+/)!=null)
		{
			y += 1;
		}



		if(x.match(/[!@$%^&*()]+/)!=null)
		{
			y += 1;
		}

		if(x.length>5)
		{
			y += 1;
		}

		switch(y){
			case 0:
				strengthbar.value = 20;
				txt += "too weak";
				break;
			case 1:
				strengthbar.value = 40;
				txt += "weak";
				break;
			case 2:
				strengthbar.value = 60;
				txt += "good";
				break;
			case 3:
				strengthbar.value = 80;
				txt += "strong";
				break;
			case 4:
				strengthbar.value = 100;
				txt += "very strong";
				break;


		}
		if(x.length == 0)
		{
			strengthbar.value = 0;

		}
		document.getElementById('demo').innerHTML = txt;

	}
