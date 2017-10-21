class ClientAdsController < ApplicationController
  before_action :client_authenticate!

  def client_authenticate!
    redirect_to new_client_session_url unless client_signed_in?
  end

  def index
    @ads = Ad.where(client_id: current_client.id)
  end
end
