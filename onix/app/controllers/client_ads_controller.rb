class ClientAdsController < ApplicationController
  before_action :client_authenticate!

  def client_authenticate!
    redirect_to new_client_session_url unless client_signed_in?
  end

  def index
    @ads = Ad.where(client_id: current_client.id)
  end

  def new
    @ads = Ad.new
  end

  def create
    @create_data = Ad.create(title: ad_params[:title], image: ad_params[:image], client_id: current_client.id)
  end

  def setting

  end

  private
  def ad_params
    params.require(:ad).permit(:title, :image, :client_id)
  end
end
