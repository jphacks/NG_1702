class CreateEnableAds < ActiveRecord::Migration[5.1]
  def change
    create_table :enable_ads do |t|
      t.integer :client_id
      t.integer :beacon_id
      t.integer :ad_id
      t.timestamps
    end
  end
end