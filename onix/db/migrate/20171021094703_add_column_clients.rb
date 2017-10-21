class AddColumnClients < ActiveRecord::Migration[5.1]
  def change
    add_column :clients, :name, :string, :after => :email
  end
end
