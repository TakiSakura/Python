#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green',
     'points': 5,'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
print("...")