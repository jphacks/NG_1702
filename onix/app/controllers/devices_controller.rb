class DevicesController < ApplicationController
  def create
    device = current_user.devices.find_or_initialize_by endpoint: params[:endpoint]
    device.attributes = device_params
    device.save! if device.changed?
    head :ok
    WebpushService.new.webpush_clients('hoge')
  end

  private

  def device_params
    params.require(:subscription).permit(%i(endpoint p256dh auth))
  end
end