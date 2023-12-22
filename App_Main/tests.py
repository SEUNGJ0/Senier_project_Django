from App_Main.models import Pet_daily_feeding,Pet_info
import random 

def test_write_db():
    Choko = Pet_info.objects.get(id=9)
    for i in range(1,26):
        Pet_daily_feeding.objects.create(
            pet_name = Choko,
            feed_date = '2023-12-'+str(i).zfill(2),
            feed_time = '08:00:00',
            feed_amount = '83',
            remain_amount = random.randint(0,5),
            feed_index = True
        )
        Pet_daily_feeding.objects.create(
            pet_name = Choko,
            feed_date = '2023-12-'+str(i).zfill(2),
            feed_time = '13:00:00',
            feed_amount = '83',
            remain_amount = random.randint(0,5),
            feed_index = True
        )
        Pet_daily_feeding.objects.create(
            pet_name = Choko,
            feed_date = '2023-12-'+str(i).zfill(2),
            feed_time = '20:00:00',
            feed_amount = '83',
            remain_amount = random.randint(0,5),
            feed_index = True
        )

    
test_write_db()