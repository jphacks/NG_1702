# coding: utf-8

User.delete_all
ActiveRecord::Base.connection.execute('ALTER TABLE users AUTO_INCREMENT = 1')
User.create!(id: 1, email: 'u@u.com', password: 'password')
User.create!(id: 2, email: 'dsadsadas@u.com', password: 'password')

ActiveRecord::Base.connection.execute('ALTER TABLE clients AUTO_INCREMENT = 1')
Client.delete_all
Client.create!(id:1, email: 'c@c.com', name: 'タケシのケーキ - 名古屋店', password:'password')
Client.create!(id:2, email: 'dsadasdsa@c.com', name: 'サトシ珈琲店 - 大須店', password:'password')

ActiveRecord::Base.connection.execute('ALTER TABLE ads AUTO_INCREMENT = 1')
Ad.delete_all
Ad.create!(id: 1, client_id: 1, title: 'ケーキ全品300円！', image: 'https://creive.me/wp-content/uploads/2016/03/tunauniversity_l.jpg')
Ad.create!(id: 2, client_id: 1, title: 'ショートケーキ無料', image: 'https://creive.me/wp-content/uploads/2015/06/making_140619_031.jpg')
Ad.create!(id: 3, client_id: 1, title: '20:00~ ケーキ20%OFF', image: 'http://talk-to-gaizin.com/WP/wp-content/uploads/2010/05/tooth.jpg')
Ad.create!(id: 4, client_id: 2, title: 'コーヒチケットプレゼントキャンペーン', image: 'http://talk-to-gaizin.com/WP/wp-content/uploads/2010/05/tooth.jpg')

ActiveRecord::Base.connection.execute('ALTER TABLE user_ads AUTO_INCREMENT = 1')
UserAd.delete_all
UserAd.create!(id: 1, user_id: 1, ad_id: 1)
UserAd.create!(id: 2, user_id: 1, ad_id: 4)
UserAd.create!(id: 3, user_id: 2, ad_id: 3)

