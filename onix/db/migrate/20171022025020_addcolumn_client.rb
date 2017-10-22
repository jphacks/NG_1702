class AddcolumnClient < ActiveRecord::Migration[5.1]
  def change
    add_column :clients, :u_ad_id, :integer
  end
end
