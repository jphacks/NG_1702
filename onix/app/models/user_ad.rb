class UserAd < ApplicationRecord
  belongs_to  :user
  belongs_to  :ad
end
