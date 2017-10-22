class UserAdsController < ApplicationController
  before_action :authenticate_user!

  def index
    @user_ads = UserAd.where(user_id: current_user.id)
  end

  def show
    @ad = Ad.find(params[:id])
  end

  def post
    uri = URI.parse("http://192.168.179.8:8000/cgi-bin/sample_1.py?uid=#{current_user.id}")
    response = Net::HTTP.start(uri.host, uri.port) do |http|
      http.get(uri.request_uri)
    end

    begin
      case response
        when Net::HTTPSuccess
          @result = JSON.parse(response.body)
        else
          @message = "HTTP ERROR: code=#{response.code} message=#{response.message}"
      end
    rescue => e
      @message = "e.message"
    end
  end

  def setting

  end

  def get_ad
    client = Client.find(params[:id])
    UserAd.create(user_id: current_user.id, ad_id: client.u_ad_id)
    redirect_to user_ads_path
  end

  def coin
    @coin = current_user.takeshi
  end
end
