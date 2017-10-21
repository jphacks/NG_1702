class AddColumnUsers < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :takeshi,:integer, default: 0
  end
end
