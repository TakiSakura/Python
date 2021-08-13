def describe_pet(pet_name,animal_type='dog'):
    #一条名为Willie的小狗
    describe_pet('willie')
    describe_pet(pet_name='willie')
    #一只名为Haryy的仓鼠
    describe_pet('harry','hamster')
    describe_pet(pet_name='harry',animal_type='hamster')
    describe_pet(animal_type='hamster',pet_name='harry')