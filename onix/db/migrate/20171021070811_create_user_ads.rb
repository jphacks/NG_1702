class CreateUserAds < ActiveRecord::Migration[5.1]
  def change
    create_table :user_ads do |t|
      t.integer :user_id
      t.integer :adra_id
      t.timestamps
    end
  end
end
