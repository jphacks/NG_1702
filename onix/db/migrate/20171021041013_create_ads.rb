class CreateAds < ActiveRecord::Migration[5.1]
  def change
    create_table :ads do |t|
      t.integer :client_id
      t.string  :title
      t.timestamps
    end
  end
end