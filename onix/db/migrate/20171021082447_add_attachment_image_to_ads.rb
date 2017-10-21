class AddAttachmentImageToAds < ActiveRecord::Migration[5.1]
  def self.up
    change_table :ads do |t|
      t.attachment :image
    end
  end

  def self.down
    remove_attachment :ads, :image
  end
end
