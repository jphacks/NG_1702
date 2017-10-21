class UserAdsController < ApplicationController
  before_action :authenticate_user!

  def index
    @user_ads = UserAd.find(current_user.id)

  end

  def show

  end

  def post

  end

  def setting

  end

  def coin

  end
end
