# coding: utf-8

User.delete_all
User.create!(id:1, email: 'u@u.com', password: 'password')

Client.delete_all
Client.create!(id:1, email: 'c@c.com', name: 'タケシのケーキ - 名古屋店', password:'password')

Ad.delete_all
Ad.create!(id:1, client_id: 1, title: 'ケーキ全品300円！')
Ad.create!(id:2, client_id: 1, title: 'ショートケーキ無料')
Ad.create!(id:3, client_id: 1, title: '20:00~ ケーキ20%OFF ')

UserAd.delete_all
UserAd.create!(id:1, user_id: 1, ad_id: 1)
UserAd.create!(id:2, user_id: 1, ad_id: 3)
